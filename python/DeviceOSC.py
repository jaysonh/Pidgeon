import json
from pythonosc import udp_client
from pythonosc import osc_bundle_builder
from pythonosc import osc_message_builder

from DeviceOutControl import DeviceOutControl

class DeviceOSC(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )
        self.port = json_data["port"]
        self.host = json_data["host"]
        self.addr = json_data["address"]

        print(f"creating device OSC at {self.host}, {self.port}")        

        self.client =   udp_client.SimpleUDPClient(self.host, self.port)
        
        pass

    def sendData(self, data : []):
        
        self.values = self.range.clamp(data)
        print(f"osc sending data: {self.values}")
        self.client.send_message(self.addr, self.values)  
        
        # send a bundle of data
        #bundle = osc_bundle_builder.OscBundleBuilder(osc_bundle_builder.IMMEDIATELY)
        #msg = osc_message_builder.OscMessageBuilder(address=self.addr)
        #for i in range(0,len(data)):
        #    print(f"OSC: adding data to bundle: {data[i]}")
        #    msg.add_arg( data[i] )
        #bundle.add_content(msg.build())
        #
        #bundle = bundle.build()
        #self.client.send_message(self.addr, bundle )

        pass
