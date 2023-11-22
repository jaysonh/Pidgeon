import json
import subprocess
from DeviceOutControl import DeviceOutControl

class DeviceCommandLine(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )

        self.command = json_data["command"].split(" ")
        pass

    def sendData(self, v : []):
        print(f"running subprocess.command: {self.command[0]} ")
        subprocess.run([self.command[0]], shell=True, check=True) 
        self.value = v[0]
        
        pass
