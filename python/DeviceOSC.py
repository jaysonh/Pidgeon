import json
from pythonosc import udp_client

from DeviceOutControl import DeviceOutControl

class DeviceOSC(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        self.port = json_data["port"]
        self.host = json_data["host"]
        self.addr = json_data["address"]

        print(f"creating device OSC at {self.host}, {self.port}")        

        self.client = udp_client.SimpleUDPClient(self.host, self.port)
        
        pass

    def sendData(self, v : int):
        print(f"sendData OSC: {v}")
        self.value = v
        self.client.send_message(self.addr, v)
        pass
