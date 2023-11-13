from Action import Action

class ActionRamp(Action):
    v = 0
    running = False
    
    def __init__(self, min : int, max : int, timeLength : float) -> None:
        self.min = min
        self.max = max
        self.timeLength = timeLength
        pass

    def start(self) -> None:
        pass

    def get(self) -> int:
        return 0