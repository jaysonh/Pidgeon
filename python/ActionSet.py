from Action import Action
from DeviceOutControl import DeviceOutControl
import json

class ActionSet(Action):

    v = 0
    
    def __init__(self, json_data : json ) -> None:
        self.data = json_data["value"]
        pass

    #def __init__(self, data = []) -> None:
    #    self.data = data
    #    pass

    def run(self, device : DeviceOutControl):
        print(f"run ActionSet: {self.data}")
        if type(self.data) is list:
            device.sendData(self.data )
        else:
            print("sending list")
            device.sendData([ self.data] )
        pass