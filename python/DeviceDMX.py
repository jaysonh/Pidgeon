import json
from DeviceOutControl import DeviceOutControl

class DeviceDMX(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        pass

    def sendData(self, v : float):
        self.value = v
        pass
