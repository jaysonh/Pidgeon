import json
from typing import List
from Device import Device

class DeviceHandler:

    def __init__(self, devices_json_out : json, devices_json_in : json ):
        self.devices = {}

        for json_device in devices_json_out:
            key = json_device["id"]
            self.devices[key] = Device(json_device)
            print(f"adding device {key}: {self.devices[key]}")
        pass
