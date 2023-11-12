import json
import paho.mqtt.client as mqtt

class MQTTHandler:
    def __init__(self ,mqtt_json : json):
        
        self.funcList = []

        # Create an MQTT client
        self.client = mqtt.Client()

        # Connect to the MQTT broker
        self.port = mqtt_json[0].get("broker_port");
        self.addr = mqtt_json[0].get("broker_addr");

        print(f"connecting to broker {self.addr} {self.port}")
        self.client.connect(self.addr, self.port)

    def send_msg( self, topic : str, msg : str):
        self.client.publish(topic, msg)
        
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    def subscribe( self, topic : str, func):
        

        self.client.subscribe(topic)
        self.funcList.append( func)

