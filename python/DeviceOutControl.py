import json


class DeviceOutControl:
    
    def __init__(self, json_data : json ):
        self.numChannels = json_data["numChannels"]

    def sendData(self, v : int):
        pass
        
