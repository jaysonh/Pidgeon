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
        self.mqtt.subscribe( self.mqttTopic )
       
    def sendData(self, v : float ):
        self.value = int(self.range.clamp(v))
        logger.info(f"sendData Rebble: {v}")

        url = "http://" + self.remoteAddr + "/set_single.html?value=" + str(self.value) + "&id=4"

        logger.debug(f"Sending URL request to: {url}")
        response = requests.get(url)
        response_json = response.json()

        logger.debug(f"Response from HTTP: {response_json}")
        
