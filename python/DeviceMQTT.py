import json
import paho.mqtt.client as mqtt 
from MQTTHandler import MQTTHandler

from DeviceOutControl import DeviceOutControl

class DeviceMQTT(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        print("creating device MQTT")
        self.mqtt = MQTTHandler( json_data["broker"] )
        self.topic = json_data["topic"]
        pass

    def sendData(self, v = [] ):
        self.value = v[0]
        print(f"sendData MQTT: {self.value}")
        self.mqtt.send_msg( self.topic, str(self.value) )
        pass
