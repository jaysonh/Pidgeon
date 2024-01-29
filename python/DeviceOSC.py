import json
from pythonosc import udp_client
from pythonosc import osc_bundle_builder
from pythonosc import osc_message_builder
from DeviceOutControl import DeviceOutControl
from Logging import *

class DeviceOSC(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )

        self.port = json_data["port"]
        self.host = json_data["host"]
        self.addr = json_data["address"]

        logger.info(f"creating device OSC at {self.host}, {self.port}, {self.addr}")        

        self.client =   udp_client.SimpleUDPClient(self.host, self.port)
        
    def stop(self):
        self.client.disconnect()
        pass

    def sendData(self, data : []):
        
        self.values = self.range.clamp(data)

        logger.debug(f"osc sending data: {self.values}")
        self.client.send_message(self.addr, self.values)  
        