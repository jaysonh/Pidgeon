import paho.mqtt.client as mqtt
from MQTTBroker import *
from Logging import *

class MQTTHandler():

    __instance = None
    broker_list = {}

    @staticmethod 
    def getInstance():
      """ Static access method. """
      if MQTTHandler.__instance == None:
         MQTTHandler()
      return MQTTHandler.__instance

    def __init__(self):
      """ Virtually private constructor. """
      if MQTTHandler.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         MQTTHandler.__instance = self
    
    def add_broker(self, mqtt_json : json) -> MQTTBroker:
        key = mqtt_json["addr"] #json.dumps(mqtt_json, separators=(',', ':'))
        
        logger.info(f"Searching for broker {key}")
        logger.info(f"mqtt key: {key}")
        if key in self.broker_list:
            logger.info(f"MQTT broker already found")
        else:
            logger.info(f"adding broker: {mqtt_json}") 
            # Connect to the MQTT broker
            self.broker_list[ key ] = MQTTBroker( mqtt_json )

        return self.broker_list[key]
