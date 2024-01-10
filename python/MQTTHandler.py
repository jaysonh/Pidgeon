import paho.mqtt.client as mqtt
from MQTTBroker import *

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

        print(f"mqttJson: {mqtt_json}")
        key = mqtt_json["addr"] #json.dumps(mqtt_json, separators=(',', ':'))
        print(f"mqtt key: {key}")
        if key in self.broker_list:
            print("MQTT broker already found")
        else:
            print("adding broker: ", mqtt_json)
            # Connect to the MQTT broker
            self.broker_list[ key ] = MQTTBroker( mqtt_json )

        return self.broker_list[key]
