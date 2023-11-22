import json
import paho.mqtt.client as mqtt

class MQTTBroker:
    def __init__(self, mqtt_json : json):
        
        self.port = mqtt_json.get( "port" )
        self.addr = mqtt_json.get( "addr" )
        
        print(f"connecting to broker {self.addr} {self.port}")
        self.broker = mqtt.Client()
        self.broker.connect(self.addr, self.port)
        
        pass  

    def send_msg( self, topic : str, value : str):
        self.broker.publish(topic, value)
        pass