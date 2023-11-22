import json
import paho.mqtt.client as mqtt 
from MQTTHandler import MQTTHandler

from DeviceOutControl import DeviceOutControl

class DeviceMQTT(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        print("creating device MQTT")
        #self.mqtt = MQTTHandler( json_data["broker"] )
        #self.mqtt = MQTTHandler
        m = MQTTHandler.getInstance()
        self.mqtt = m.add_broker( json_data["broker"]  )
        self.topic = json_data["topic"]
        pass

    def sendData(self, v = [] ):
        self.vals = v

        if len(self.vals) == 1:
            print(f"sendData MQTT: {self.vals[0]}")
            self.mqtt.send_msg( self.topic, str(self.vals[0]) )
        else:
            print(f"sendData MQTT: {self.vals}")
            self.mqtt.send_msg( self.topic, str(self.vals) )
        pass
