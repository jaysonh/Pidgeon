import json
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

        key = json.dumps(mqtt_json, separators=(',', ':'))

        if key in self.broker_list:
            print("MQTT broker alread found")
        else:
            print("adding broker: ", mqtt_json)
            # Connect to the MQTT broker
            self.broker_list[ key ] = MQTTBroker( mqtt_json )

        return self.broker_list[key]

    def send_msg( self, topic : str, msg : str):
        self.client.publish(topic, msg)
        
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    def subscribe( self, topic : str, func):
        

        self.client.subscribe(topic)
        self.funcList.append( func)
