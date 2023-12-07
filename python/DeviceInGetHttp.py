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

class DeviceInGetHttp(DeviceInControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        print("creating sensor Rest HTTP")
        
        self.request_addr = json_data["requestAddr"]
        self.api_key = json_data["apiKey"]

        pass

    def update(self):       
                
        url = self.request_addr
        headers={"x-api-key" : self.api_key}
        response = requests.get(self.request_addr, headers=headers)

        resultJson = response.json()
        print( resultJson )

        pass

    def on_message(client, userdata, msg):
        #print(f"Message received [{msg.topic}]: {msg.payload}")
        pass

    def getData(self) ->float :
        pass
    
    def sendData(self, v : float):
        self.value = v
        #print(f"sendData MQTT: {v}")
        #self.mqtt.send_msg( self.topic, str(v) )
        pass
