import json
from typing import List
from MQTTHandler import *
from SensorMQTT import *

class Sensor:

    def __init__(self, json_data : json):
        self.type = json_data["type"]
        if( self.type == "mqtt"):
            self.device = SensorMQTT(json_data  )

        pass
