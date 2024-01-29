import json
import paho.mqtt.client as mqtt 
from MQTTHandler import MQTTHandler
from DeviceOutControl import DeviceOutControl
from Logging import *

class DeviceMQTT(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        logger.info("creating device MQTT")
        
        m = MQTTHandler.getInstance()
        self.mqtt = m.add_broker( json_data["broker"]  )
        self.topic = json_data["topic"]
        
    def stop(self):
        self.mqtt.disconnect()
        pass

    def sendData(self, v = [] ):
        self.vals = v

        if len(self.vals) == 1:
            logger.debug(f"sendData MQTT: {self.vals[0]}")
            self.mqtt.send_msg( self.topic, str(self.vals[0]) )
        else:
            logger.debug(f"sendData MQTT: {self.vals}")
            self.mqtt.send_msg( self.topic, str(self.vals) )
        