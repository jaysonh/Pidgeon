import json
from DeviceOutControl import DeviceOutControl

class DeviceRebble(DeviceOutControl):
    def __init__(self, json_data : json    ):
        super().__init__( json_data)
        
