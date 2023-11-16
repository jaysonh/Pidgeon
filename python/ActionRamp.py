import time
from Action import Action
from DeviceOutControl import DeviceOutControl
from MathHelper import *

class ActionRamp(Action):
    v = 0
    started = False

    def __init__(self, min : int, max : int, timeLength : float, intervalTime : float) -> None:
        self.min = min
        self.max = max
        self.timeLength = timeLength
        self.intervalTime = intervalTime
        pass

    def start(self) -> None:
        started = True
        pass

    
    def run(self, device : DeviceOutControl):
        print("run ActionRamp")

        t_start = time.time()
        t_end   = t_start + self.timeLength
        
        # loop over time
        while time.time() < t_end:
            val = MapData( time.time(), t_start, t_end, self.min, self.max )
            device.sendData( val )
            time.sleep( self.intervalTime )

        device.sendData( self.max )
        print("finished ramp")
        pass