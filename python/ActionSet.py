from Action import Action

class ActionSet(Action):

    v = 0
    
    def __init__(self, value : int) -> None:
        self.v = value
        pass

    def get(self) -> int:
        return self.v