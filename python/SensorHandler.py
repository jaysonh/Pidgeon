import json
from typing import List
from Sensor import *

class SensorHandler:
    sensors = {}

    def __init__(self, json_data : json):

        for json_device in json_data:
            key = json_device["id"]
            self.sensors[key] = Sensor(json_device)
            print(f"adding sensor {key}: {self.sensors[key]}")
        pass

