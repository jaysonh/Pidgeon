import json
from typing import List
from ConfigFile import ConfigFile

class Configuration:

    # Constructor
    # opens a list of json file names, stores these in a dict
    def __init__(self, config_files : List[str] ):
        self.config_json = {}

        try:
            for file_name in config_files:
                if not file_name:
                    raise FileExistsError
                
                with open(file_name) as f:
                    json_data = json.load(f)
                key = list(json_data.keys())[0]              
                
                self.config_json[key] = json_data[key]   
                print(f"Saved json conifg for key: {key}: {self.config_json[key]}")  
        except IndexError:
            print("Error: Invalid config file list")
        except FileExistsError:
            print("Error: problem opening file")
 
    def get(self, key : str):
        return self.config_json[key]

if __name__ == "__main__":
    print("testing Configuration.py")