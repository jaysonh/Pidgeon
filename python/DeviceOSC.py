import json
from pythonosc import udp_client

from DeviceOutControl import DeviceOutControl

class DeviceOSC(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        print("creating device OSC")
        
        pass

    def sendData(self, v : int):
        
        pass
