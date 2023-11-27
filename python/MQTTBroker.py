import json
import paho.mqtt.client as mqtt


def hello( client, userdata, msg):
    print(f"hello Message received [{msg.topic}]: {msg.payload}")
    pass
class MQTTBroker:
    def __init__(self, mqtt_json : json):
        
        self.port = mqtt_json.get( "port" )
        self.addr = mqtt_json.get( "addr" )
        
        print(f"connecting to broker {self.addr} {self.port}")
        self.broker = mqtt.Client()
        self.broker.on_message = hello
        self.broker.connect(self.addr, self.port)
        
        pass  

    def subscribe( self, topic : str ):
        print(f"subscribed to topic: {topic}")
        self.broker.subscribe( topic )
        #self.broker.on_message = self.hello
        pass


    def send_msg( self, topic : str, value : str):
        self.broker.publish(topic, value)
        pass
