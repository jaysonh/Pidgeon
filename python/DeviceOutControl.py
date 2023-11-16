import json


class DeviceOutControl:
    
    value = 0

    def __init__(self, json_data : json ):
        self.numChannels = json_data["numChannels"]

    def sendData(self, v : int):
        pass

    def getValue(self) -> int:
        return self.value
        
