import time
from Action import Action
from DeviceOutControl import DeviceOutControl
from MathHelper import *

class ActionRamp(Action):
    v = 0
    started = False

    def __init__(self, start : [], end : [], timeLength : float, intervalTime : float ) -> None:
        self.start = start
        self.end = end
        self.timeLength = timeLength
        self.intervalTime = intervalTime
        if len(self.start) != len(self.end):
            raise Exception("start and end arrays must be the same length")
        self.numVals = len(self.start) 
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
            vals = []
            for i in range(0, self.numVals):
                vals.append( MapData( time.time(), t_start, t_end, self.start[i], self.end[i] ) )
            device.sendData( vals )
            time.sleep( self.intervalTime )

        vals = []
        for i in range(0, self.numVals):
            vals.append(self.end[i])
        device.sendData( vals )
        pass