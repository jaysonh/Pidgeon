import json
import paho.mqtt.client as mqtt 
from MQTTHandler import MQTTHandler
from SensorControl import *

class SensorMQTT(SensorControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        print("creating device MQTT")
        self.mqtt = MQTTHandler( json_data["broker"] )
        self.topic = json_data["topic"]
        pass

    def sendData(self, v : float):
        self.value = v
        print(f"sendData MQTT: {v}")
        self.mqtt.send_msg( self.topic, str(v) )
        pass
