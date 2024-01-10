import json
import paho.mqtt.client as mqtt
import random

def hello( client, userdata, msg):
    print(f"hello Message received [{msg.topic}]: {msg.payload}")
    pass
class MQTTBroker:

    subscribe_list = []

    def __init__(self, mqtt_json : json):
        
        self.port = mqtt_json.get( "port" )
        self.addr = mqtt_json.get( "addr" )
        
        print(f"connecting to broker {self.addr} {self.port}")
        client_id = f'subscribe-{random.randint(0, 100)}'
        self.broker = mqtt.Client(client_id)
        
        #self.broker.on_message = self.on_message


        self.broker.connect(self.addr, self.port)
        self.broker.on_connect = self.on_connect
        pass  


    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    def subscribe( self, topic : str ):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        print(f"subscribed to topic: {topic}")
        self.broker.subscribe( topic )
        #self.broker.on_message = self.on_message
        self.broker.on_message =on_message
        pass


    def send_msg( self, topic : str, value : str):
        self.broker.publish(topic, value)
        pass
    #def on_message(client, userdata, msg):
    #        print(f"Client: {client} Received `{msg.payload.decode()}` from `{msg.topic}` topic")
