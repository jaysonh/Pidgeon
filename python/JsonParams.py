import json
from tkinter.filedialog import asksaveasfile
from Logging import *

class JsonParams:
    def __init__(self, json_data : json,key : str):

        self.json_data = json_data
        self.key = key
        logger.info(f"Saved JsonParam for key: {key}")
        pass

    def GetNumData(self) -> int:
        return len(self.json_data) 

    def getJson(self) -> json:
        return self.json_data
    
    def getKey(self) -> str:
        return self.key
    
    def addWithoutKey(self, json_data : json):
        self.json_data.append( json_data )
    
    def remove(self, indx):
        del self.json_data[indx]
        pass

    # add this json item to the array at key
    def add(self, key : str, json_data : json): 
        if key == self.key:
            self.json_data.append( json_data )            
        else: 
            print(f"Cannot find key: {key}")
            raise KeyError
        pass

    def save_file(self):
        file = asksaveasfile(initialfile = 'settings.json',
        defaultextension=".json",filetypes=[("All Files","*.*"),("JSON","*.json")])
        if file is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        
        json.dump(self.json_data, file)


