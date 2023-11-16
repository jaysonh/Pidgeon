from Action import Action
from DeviceOutControl import DeviceOutControl

class ActionSet(Action):

    v = 0
    
    def __init__(self, value : int) -> None:
        self.v = value
        pass

    def get(self) -> int:
        return self.v
    def run(self, device : DeviceOutControl):
        print(f"run ActionSet: {self.v}")
        device.sendData( self.v )
        pass