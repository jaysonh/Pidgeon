import json
import paho.mqtt.client as mqtt 
from MQTTHandler import MQTTHandler

from DeviceOutControl import DeviceOutControl

class DeviceRunScript(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        print("creating device RunSctipt")
        self.topic = json_data["topic"]
        pass

    def sendData(self, v : int):
        #self.mqtt.send_msg( self.topic, str(v) )
        pass
