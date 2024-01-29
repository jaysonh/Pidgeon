import json
from typing import List
from Device import Device
from DeviceOutControl import DeviceOutControl
from JsonParams import *

class DeviceHandler:
    devices = {}

    #def __init__(self, devices_json_out : json ):
    def __init__(self, devices_json_out : JsonParams ):
        for json_device in devices_json_out.getJson():
            key = json_device["id"]
            self.devices[key] = Device(json_device)
            logger.info(f"adding device {key}: {self.devices[key]}")
        
    def get(self, keyID : str ) -> DeviceOutControl:
        return self.devices[keyID]

    def getAction(self, keyID : str):
        pass

    def stopAll(self):
        for key in self.devices:
            
            self.devices[key].stop()