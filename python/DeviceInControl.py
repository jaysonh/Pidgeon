import json


class DeviceInControl:
    
    value = 0.0

    def __init__(self, json_data : json ):
        pass

    def sendData(self, v : float ):
        pass

    def getValue(self) -> int:
        return self.value
        

    def update(self):    
        pass