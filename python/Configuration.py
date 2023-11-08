from typing import List
from ConfigFile import ConfigFile

class Configuration:

    def __init__(self, config_files: List[str] ):
        try:
            for file in config_files:
                if not file:
                    raise FileExistsError
                        
                self.devices_file  = config_files[0]
                self.schedule_file = config_files[1]
            
            self.printValues()
        except IndexError:
            print("Error: Invalid config file list")
        except FileExistsError:
            print("Error: problem opening file")

    def printValues(self):
        print(f"{self.devices_file}, {self.schedule_file}")

    def get(self, key : str):
        pass

    # This method adds the annual interest to the balance of the account
    #def add_interest(self):
    #    self.balance += self.balance * self.annual_interest


if __name__ == "__main__":
    print("testing Configuration.py")