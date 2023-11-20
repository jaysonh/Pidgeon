import time
from Action import Action
from DeviceOutControl import DeviceOutControl
from MathHelper import *

# similiar to the ActionRamp fucntion except that this will go from the initial value to a target
class ActionRampTarget(Action):
    v = 0
    started = False

    def __init__(self, target : [], timeLength : float, intervalTime : float) -> None:
        self.target = target
        self.timeLength = timeLength
        self.intervalTime = intervalTime
        self.numVals = len(self.target) 

        pass

    def start(self) -> None:
        started = True
        pass

    # not working...
    def run(self, device : DeviceOutControl ):
        print("run ActionRampTarget")

        t_start = time.time()
        t_end   = t_start + self.timeLength
        
        startVals = device.getValues()

        while time.time() < t_end:
            vals = []
            for i in range(0, self.numVals):
                vals.append( MapData( time.time(), t_start, t_end, startVals[i], self.target[i] ) )
            device.sendData( vals )
            time.sleep( self.intervalTime )

        vals = []
        for i in range(0, self.numVals):
            vals.append( self.target[i] )
        device.sendData( vals )

        #self.min = device.getValue()
        #self.max = self.target
        #while time.time() < t_end:
        #    val = MapData( time.time(), t_start, t_end, self.min, self.max )
        #    device.sendData([ val ])
        #    time.sleep( self.intervalTime )
        #device.sendData( [self.max] )
        #print("Finished RampTarget")
        pass