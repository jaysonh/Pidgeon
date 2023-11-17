import json
import paho.mqtt.client as mqtt 
from MQTTHandler import MQTTHandler

from DeviceOutControl import DeviceOutControl

class DeviceKKC(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        print("creating device MQTT")
        self.mqtt = MQTTHandler( json_data["broker"] )
        self.topic = json_data["topic"]
        pass   

    def sendData(self, data = []):
        
        print("data: ", data)
        idata = []
        for x in data:
            idata.append(hex(int(x)))

        send_arr = ['0xa5', '0x01'] + idata
        byte_arr = bytes([int(x,0) for x in send_arr])

        print(f"sendData KKC MQTT: {data} as bye array: {byte_arr} to {self.topic}")

        self.mqtt.send_msg( self.topic, byte_arr )
        pass
