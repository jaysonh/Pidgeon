import json
from typing import List
from DeviceIn import *
from JsonParams import *
from Logging import *

class DeviceInHandler:
    sensors = {}

    #def __init__(self, json_data : json):
    def __init__(self, json_data : JsonParams):
        for json_device in json_data.getJson():
            key = json_device["id"]
            self.sensors[key] = DeviceIn(json_device)
            logger.info(f"added sensor {key}: {self.sensors[key]}")
        pass

