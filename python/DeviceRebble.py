import json
import requests
from DeviceOutControl import *
from MQTTHandler import MQTTHandler
from MathHelper import *
from Logging import *

class DeviceRebble(DeviceOutControl):
    def __init__(self, json_data : json    ):
        super().__init__( json_data)
        logger.info("Creating Device Rebble")
        self.remoteAddr = json_data["remoteAddr"] #"192.168.1.101"
        self.mqttTopic  = json_data["mqttTopic"]

        m = MQTTHandler.getInstance()
        self.mqtt = m.add_broker( json_data["broker"]  )
        self.mqtt.subscribe( self.mqttTopic, self.mqttAction )

        self.timeout = 15 # second timeout
       
    def mqttAction(self, v : []):
        self.sendData(v[0])
        pass

    def stop(self):
        self.mqtt.disconnect()
        
        pass

    def sendData(self, v : [] ):
        if len(v) > 0:
            self.value = int(self.range.clamp(v[0]))
            logger.info(f"sendData Rebble: {v[0]}")

            url = "http://" + self.remoteAddr + "/set_single.html?value=" + str(self.value) + "&id=4"

            logger.debug(f"Sending URL request to: {url}")
            try:
                response = requests.get(url, timeout= self.timeout )
                response_json = response.json()
                logger.debug(f"Response from HTTP: {response_json}")
            except requests.exceptions.Timeout:
                logger.error("HTTP Request timeout")
        else:
            raise("Invalid input ")
        
