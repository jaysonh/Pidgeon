import json
import requests
from DeviceOutControl import *
from MQTTHandler import MQTTHandler
from MathHelper import *
from Logging import *
import time
import threading

class DeviceRebble(DeviceOutControl):
    def __init__(self, json_data : json    ):
        super().__init__( json_data)
        logger.info("Creating Device Rebble")
        self.remoteAddr = json_data["remoteAddr"] #"192.168.1.101"
        self.mqttTopic  = json_data["mqttTopic"]

        m = MQTTHandler.getInstance()
        self.mqtt = m.add_broker( json_data["broker"]  )
        self.mqtt.subscribe( self.mqttTopic, self.mqttAction )
        self.timeout = 10 # second timeout

        self.message_queue = []
        self.message_thread_running = True
        self.message_thread = threading.Thread(target=self.message_queue_thread)
        self.message_thread.start()
       
    def message_queue_thread(self):

        while self.message_thread_running == True:

            if len(self.message_queue) > 0:
                request_url = self.message_queue.pop(0)
                try:
                    logger.debug(f"sending request: {request_url}")
                    response = requests.get(request_url, timeout= self.timeout )
                    logger.debug(f"response code: {response.status_code}")
                    #if response.status_code == 200:
                    #    response_json = response.json()
                    #    logger.debug(f"Response from HTTP: {response_json}")
                    #    logger.debug(f"ended http request thread")
                except requests.exceptions.Timeout:
                    logger.error("HTTP Request timeout or null response")                    

            time.sleep(0.01)
        
    def mqttAction(self, v : []):
        self.sendData(v)
        
    def stop(self):
        self.message_thread_running = False
        self.message_thread.join()
        self.mqtt.disconnect()
        
    def sendData(self, v : [] ):
        if len(v) > 0:
            self.value = int(self.range.clamp(v[0]))
            logger.info(f"sendData Rebble: {v[0]}")

            url = "http://" + self.remoteAddr + "/set_single.html?value=" + str(self.value) + "&id=4"
            self.message_queue.append( url )
            logger.debug(f"Adding URL to queue: {url}")
        else:
            raise(f"Invalid input: {v}")
        
