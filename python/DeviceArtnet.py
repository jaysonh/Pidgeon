import json
import asyncio
from pyartnet import ArtNetNode
from DeviceOutControl import DeviceOutControl
from Logging import *
from MQTTHandler import *

class DeviceArtnet(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        self.port = json_data["port"]
        self.host = json_data["host"]
        self.mqttTopic  = json_data["mqttTopic"]
        self.universeID = json_data["universe"]
        logger.info(f"Creating device ArtNet at {self.host}, {self.port}")    
        self.fade_time = 100
        m = MQTTHandler.getInstance()
        self.mqtt = m.add_broker( json_data["broker"]  )
        
        self.mqtt.subscribe( self.mqttTopic, self.mqttAction )
       
    def mqttAction(self, v : []):
        self.sendData(v[0])
        pass

    async def asyncSend(self, v : float):
        self.node = ArtNetNode(self.host, self.port )
        self.universe = self.node.add_universe(self.universeID) 

        logger.debug(f"sending channel: {self.id} data: {v}")
        self.universe.add_channel(start=1, width= self.numChannels, channel_name=self.id)

        # access is then by name
        self.channel = self.universe[self.id]
        self.channel = self.universe.get_channel(self.id)
        self.value = v
        
        send_data = []
        for i in range(self.numChannels):
            send_data.append(self.value)
        self.channel.add_fade(send_data, self.fade_time)
        await(self.channel)
        pass

    def sendData(self, v : float):
        logger.debug(f"sendData Artnet: {v}")
        asyncio.run(self.asyncSend(v))

        # this can be used to wait till the fade is complete
        #await channel.wait_till_fade_complete() # problem

