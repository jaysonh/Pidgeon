import json

class JsonParams:
    def __init__(self, json_data : json,key : str):

        self.json_data = json_data
        self.key = key
        pass

    def getJson(self) -> json:
        return self.json_data
    
    def getKey(self) -> str:
        return self.key
    
    # add this json item to the array at key
    def add(self, key : str, json_data : json): 
        if key == self.key:
            self.json_data.append( json_data )            
        else: 
            print(f"Cannot find key: {key}")
            raise KeyError
        pass

