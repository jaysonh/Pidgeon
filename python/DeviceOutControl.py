import json

class DeviceOutControl:
    
    value = 0.0

    def __init__(self, json_data : json ):
        self.numChannels = json_data["numChannels"]

    def sendData(self, data = [] ):
        self.vals = data
        pass

    #def sendData(self, v : json ):
    #    pass

    def getValues(self) -> []:
        return self.vals
    
    def getValue(self) -> int:
        return self.value
        
