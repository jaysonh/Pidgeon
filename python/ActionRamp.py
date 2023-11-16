import time
from Action import Action
from DeviceOutControl import DeviceOutControl

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

    def get(self) -> int:
        return 0
    def run(self, device : DeviceOutControl):
        print("run ActionRamp")

        t_end = time.time() + self.timeLength
        while time.time() < t_end:
            print(f"ActionRamp setting: {self.max} at {time.time()}")
            device.sendData( self.max )
            time.sleep( self.intervalTime )
        print("finished ramp")
        pass