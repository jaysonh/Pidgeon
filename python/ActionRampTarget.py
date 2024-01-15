import time
import json
from Action import Action
from DeviceOutControl import DeviceOutControl
from MathHelper import *
from Logging import *

# similiar to the ActionRamp fucntion except that this will go from the initial value to a target
class ActionRampTarget(Action):
    v = 0

    def __init__(self, json_data : json) -> None:

        self.duration = json_data["duration"]
        self.interval = json_data["interval"]

        target = json_data["target"]
        logger.info(f"Creating ActionRampTarget {self.target} {self.duration} {self.interval}")

        if type(target) != list:
            v = target
            self.target = [ v ]
        else:
            self.target = target
        self.numVals = len(self.target) 


    def run(self, device : DeviceOutControl ):
        logger.info("Running ActionRampTarget")

        t_start = time.time()
        t_end   = t_start + self.duration
        
        startVals = device.getValues()

        while time.time() < t_end:
           
            logger.debug(f"self.numVals: {self.numVals}, startVals: {startVals} self.target: {self.target}")
            
            device.sendData( [map_data( time.time(), t_start, t_end, startVals[i], self.target[i] ) for i in range(0, len(self.target))] )
            time.sleep( self.interval )

        device.sendData( self.target )      
        