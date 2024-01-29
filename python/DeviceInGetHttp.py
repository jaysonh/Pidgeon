# {
#    "name" : "Siggrow 44192",
#    "id"   : "00044192",
#    "type" : "httpGet",
#    "requestAddr" : "https://app.sigrow.com/api/v2/remote/44192/data",
#    "apiKey" : "c61e7d20-3ab1-43f9-ad32-b04e3fd9a822"
# }

import json
from MQTTHandler import MQTTHandler
from DeviceInControl import *
import urllib.request
from Logging import *

class DeviceInGetHttp(DeviceInControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        
        self.request_addr = json_data["requestAddr"]
        self.api_key = json_data["apiKey"]
        logger.info("creating sensor Rest HTTP: {self.request_addr}")

    def update(self):       
                
        headers={"x-api-key" : self.api_key}
        response = requests.get(self.request_addr, headers=headers)

        resultJson = response.json()
        logger.debug(f"Result from HTTP: {resultJson}" )


    def stop(self):
        
        pass

    def on_message(client, userdata, msg):
        #print(f"Message received [{msg.topic}]: {msg.payload}")
        pass

    def getData(self) ->float :
        pass
    
    def sendData(self, v : float):
        self.value = v
