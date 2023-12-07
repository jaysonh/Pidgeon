import json
from typing import List
from DeviceIn import *

class DeviceInHandler:
    sensors = {}

    def __init__(self, json_data : json):

        for json_device in json_data:
            key = json_device["id"]
            self.sensors[key] = DeviceIn(json_device)
            print(f"added sensor {key}: {self.sensors[key]}")
        pass

