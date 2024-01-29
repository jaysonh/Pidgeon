import json
import paho.mqtt.client as mqtt
import random
from Logging import *

def hello( client, userdata, msg):
    print(f"hello Message received [{msg.topic}]: {msg.payload}")
    pass
class MQTTBroker:

    subscribe_list = []

    def __init__(self, mqtt_json : json):
        
        self.port = mqtt_json.get( "port" )
        self.addr = mqtt_json.get( "addr" )

        self.actionDict = {}

        logger.info(f"connecting to broker {self.addr} {self.port}")
        client_id = f'subscribe-{random.randint(0, 100)}'
        self.broker = mqtt.Client(client_id)
        def on_connect(client, userdata, flags, rc):
           if rc == 0:
               logger.info("Connected to MQTT Broker!")
           else:
               logger.error("Failed to connect, return code %d\n", rc)
        #self.broker.on_message = self.on_message
        self.broker.on_connect = on_connect
        self.broker.connect(self.addr, self.port)        
        self.broker.loop_start()
        
    def getJson(self) -> json:

        json_data = {"address" : self.addr, "port" : self.port}

        return json.dumps(json_data)
    
    def subscribe( self, topic : str, action ):
        def on_message(client, userdata, msg):
            logger.debug(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            v = [ float(msg.payload.decode()) ]
            self.actionDict[msg.topic](v)
        logger.info(f"subscribed to topic: {topic}")
        self.broker.subscribe( topic )
        self.broker.on_message = on_message

        self.actionDict[topic] = action
        pass


    def send_msg( self, topic : str, value : str):
        logger.debug(f"Sending MQTT msg: {topic} {value}")
        self.broker.publish(topic, value)
        pass

    def disconnect(self):
        logger.debug(f"Disconnecting from MQTT server {self.addr}:{self.port}")
        self.broker.disconnect()
    