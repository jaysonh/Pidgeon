import time
import json
from Action import Action
from DeviceOutControl import DeviceOutControl
from MathHelper import *

class ActionRamp(Action):
    v = 0
    started = False

    def __init__(self, json_data : json ) -> None:
        self.start = json_data["start"]
        self.end = json_data["end"]
        self.timeLength = json_data["timeLength"]
        self.intervalTime =json_data[" intervalTime"]
        if len(self.start) != len(self.end):
            raise Exception("start and end arrays must be the same length")
        self.numVals = len(self.start) 
        pass

    def start(self) -> None:
        started = True
        pass

    #def sendDataArr( self, data : []):
    #    for i in range(0, len(data) ):
    #        vals.append( MapData( time.time(), t_start, t_end, self.start[i], self.end[i] ) )
    #    device.sendData( vals )
    #    pass

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

        device.sendData( self.end[i] )
        pass