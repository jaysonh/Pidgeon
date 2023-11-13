class ActionRamp:
    v = 0
    
    def __init__(self, min : int, max : int, timeLength : float) -> None:
        self.min = min
        self.max = max
        self.timeLength = timeLength
        pass

    def get(self) -> int:
        return 0