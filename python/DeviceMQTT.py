import json
import paho.mqtt.client as mqtt 

from DeviceOutControl import DeviceOutControl

class DeviceMQTT(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        pass
