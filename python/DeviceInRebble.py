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
from Logging import *
import requests
import time
class DeviceInRebble(DeviceInControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        
        self.request_addr = json_data["addr"]
        self.receiveTopic = json_data["receiveTopic"]
        self.channel = 4

        
        # connect to MQTT client
        m = MQTTHandler.getInstance()
        self.mqtt = m.add_broker( json_data["broker"]  )
        
        logger.info("creating sensor Rebble:")

    def update(self):       

        response = requests.get(self.request_addr)
        if response.status_code == 200:
            response_json = response.json()
            #logger.debug(f"{response_json}")
            id = "id" + str(self.channel)
            temp = response_json["fixtures"][id]["status"]["temperature"] / 100.0
            current = response_json["fixtures"][id]["status"]["current"]
            dim_level = response_json["fixtures"][id]["status"]["dim_level"]

                
            
            self.mqtt.send_msg(self.receiveTopic + "/temp",  temp)
            self.mqtt.send_msg(self.receiveTopic  + "/current", current)
            self.mqtt.send_msg(self.receiveTopic  + "/dimmer",  dim_level)
            self.mqtt.send_msg(self.receiveTopic  + "/time",    int(time.time()))     
            
            logger.debug(f"temp: {temp} current: {current} dimlevel: {dim_level}")
            
            # now send to mqtt

    def stop(self):
        
        pass

    def on_message(client, userdata, msg):
        #print(f"Message received [{msg.topic}]: {msg.payload}")
        pass

    def getData(self) ->float :
        pass
    
    def sendData(self, v : float):
        self.value = v
