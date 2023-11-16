import json
from DeviceOutControl import DeviceOutControl

class DeviceRebble(DeviceOutControl):
    def __init__(self, json_data : json    ):
        super().__init__( json_data)

    def sendData(self, v : int):
        print(f"sendData Rebble: {v}")
        self.value = v
        pass

        
