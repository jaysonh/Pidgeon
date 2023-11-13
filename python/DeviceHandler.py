import json
from typing import List
from Device import Device
from DeviceOutControl import DeviceOutControl

class DeviceHandler:
    devices = {}

    def __init__(self, devices_json_out : json, devices_json_in : json ):
        

        for json_device in devices_json_out:
            key = json_device["id"]
            self.devices[key] = Device(json_device)
            print(f"adding device {key}: {self.devices[key]}")
        pass

    def get(self, keyID : str ) -> DeviceOutControl:
        return self.devices[keyID]
        pass

    def getAction(self, keyID : str):
        pass