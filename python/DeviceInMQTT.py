import json
import paho.mqtt.client as mqtt 
from MQTTHandler import MQTTHandler
from DeviceInControl import *
from Logging import *

class DeviceInMQTT(DeviceInControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        logger.info("Creating sensor MQTT")
        
        # connect to MQTT client
        m = MQTTHandler.getInstance()
        self.mqtt = m.add_broker( json_data["broker"]  )
        self.request_topic = json_data["requestTopic"]
        self.receive_topic = json_data["receiveTopic"]
        self.mqtt.subscribe(self.receive_topic,self.update)

    def stop(self):
        self.mqtt.disconnect()
        pass

    def update(self):
        self.mqtt.send_msg( self.request_topic, "")
        
    def on_message(client, userdata, msg):
        logger.info(f"Message received [{msg.topic}]: {msg.payload}")

    def getData(self) ->float :
        pass
    
    def sendData(self, v : float):
        self.value = v
        logger.debug(f"sendData MQTT: {v}")
