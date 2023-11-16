import json
import asyncio
from pyartnet import ArtNetNode
from DeviceOutControl import DeviceOutControl

class DeviceArtnet(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        self.port = json_data["port"]
        self.host = json_data["host"]

        print(f"creating device ArtNet at {self.host}, {self.port}")    
        self.node = ArtNetNode( self.host, self.port )   
        self.universe = self.node.add_universe(0) 

        self.universe.add_channel(start=0, width=255, channel_name='Dimmer1')

        # access is then by name
        self.channel = universe['Dimmer1']
        self.channel = universe.get_channel('Dimmer1')
        

        self.client = udp_client.SimpleUDPClient(self.host, self.port)
        
        pass

    def sendData(self, v : int):
        print(f"sendData Artnet: {v}")
        self.value = v
        # need to implement this
        #self.channel.set
        pass
