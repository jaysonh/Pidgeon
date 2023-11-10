import json
from typing import List
from Device import Device

class DeviceHandler:

    def __init__(self, json_str : json ):
        self.devices = {}

        for json_device in json_str:
            key = json_device["id"]
            self.devices[key] = Device(json_device)
            print(f"adding device {key}: {self.devices[key]}")
        pass
