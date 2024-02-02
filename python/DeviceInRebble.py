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

class DeviceInRebble(DeviceInControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        
        self.request_addr = json_data["addr"]
        self.receiveTopic = json_data["receiveTopic"]

        logger.info("creating sensor Rebble:")

    def update(self):       

        response = requests.get(self.request_addr)
        if response.status_code == 200:
            response_json = response.json()

            #need to implement this in python to get data 
            #println("Getting data from address: " + remoteAddr, true);
            #GetRequest get = new GetRequest("http://" + remoteAddr + "/status_all.json");
            #get.send();
            #
            #if(get.getContent() != null)
            #{
            #    String     data = get.getContent();      
            #    JSONObject json = parseJSONObject(data);        
            #    JSONObject fixs = json.getJSONObject("fixtures");
            #    
            #    String idPrefix = "id" + str(channel);
            #    
            #    JSONObject fixStatus = fixs.getJSONObject(idPrefix).getJSONObject("status");
            #    
            #    status.dimLevel = fixStatus.getFloat("dim_level");
            #    status.current  = fixStatus.getFloat("current");
            #    status.temp     = fixStatus.getFloat("temperature") / 100;  

    def stop(self):
        
        pass

    def on_message(client, userdata, msg):
        #print(f"Message received [{msg.topic}]: {msg.payload}")
        pass

    def getData(self) ->float :
        pass
    
    def sendData(self, v : float):
        self.value = v
