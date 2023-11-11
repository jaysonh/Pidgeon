import json
import paho.mqtt.client as mqtt

class MQTTHandler:
    def __init__(self ,mqtt_json : json):
        
        # Create an MQTT client
        self.client = mqtt.Client()

        # Connect to the MQTT broker
        self.port = mqtt_json[0].get("broker_port");
        self.addr = mqtt_json[0].get("broker_addr");

        print(f"connecting to broker {self.addr} {self.port}")
        self.client.connect(self.addr, self.port)

        # Publish a message to a topic
        #self.client.publish("my_topic", "Hello, MQTT!")

