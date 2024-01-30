import json
import subprocess
from DeviceOutControl import DeviceOutControl
from Logging import *

class DeviceCommandLine(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )

        self.command = json_data["command"].split(" ")
        logger.info(f"creating device CommandLine: {self.command}")

    def stop(self):
        pass

    def sendData(self, v : []):
        logger.debug(f"running subprocess.command: {self.command} ")

        # run command on the command line
        subprocess.run(self.command, shell=True, check=True) 
        
