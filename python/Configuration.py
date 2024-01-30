import json
from typing import List
from JsonParams import *
from Logging import *

class Configuration:

    # Constructor
    # opens a list of json file names, stores these in a dict
    def __init__(self, config_files : List[str] ):

        self.params = {}

        try:
            for file_name in config_files:
                
                logger.info(f"Loading config file {file_name}")
                if not file_name:
                    logger.error(f"Loading config file {file_name}")
                    raise FileExistsError
                
                # load json data
                with open(file_name) as f:
                    json_data = json.load(f)
                key = list(json_data.keys())[0]              
                
                self.params[key] = JsonParams(json_data[key],key)
                  
        except IndexError:
            logger.error(f"Error: Invalid config file list")
            
        except FileExistsError:
            logger.error(f"Error: problem opening file")
 
    def get(self, key : str):
        return self.params[key]

if __name__ == "__main__":
    logger.info("Testing Configuration.py")