import json
from DeviceOutControl import DeviceOutControl
from DeviceMQTT import DeviceMQTT


class Action:
    
    def __init__(self, json_data : json ):
        pass

    def is_running(self) -> bool:
        return False
    
    def sendData(self, v : int):
        pass

    def run(self, device : DeviceOutControl):
        
        pass
        
