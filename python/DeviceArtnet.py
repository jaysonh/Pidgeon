import json
import asyncio
from pyartnet import ArtNetNode
from DeviceOutControl import DeviceOutControl
from Logging import *

class DeviceArtnet(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        self.port = json_data["port"]
        self.host = json_data["host"]

        logger.info(f"Creating device ArtNet at {self.host}, {self.port}")    
        self.node = ArtNetNode( self.host, self.port )   
        #await self.node.start() #problem?
        self.universe = self.node.add_universe(0) 

        self.universe.add_channel(start=0, width=255, channel_name='Dimmer1')

        # access is then by name
        self.channel = self.universe['Dimmer1']
        self.channel = self.universe.get_channel('Dimmer1')

    def sendData(self, v : float):
        logger.debug(f"sendData Artnet: {v}")
        self.value = v
        channel.add_fade([255,0,0], 5000)

        # this can be used to wait till the fade is complete
        #await channel.wait_till_fade_complete() # problem

