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

        self.client = udp_client.SimpleUDPClient(self.host, self.port)
        
        pass

    def sendData(self, data : []):
        #print(f"sendData OSC: {v}")
        #self.value = v[0]
        #self.client.send_message(self.addr, v[0])

        # send a bundle of data
        bundle = osc_bundle_builder.OscBundleBuilder(osc_bundle_builder.IMMEDIATELY)
        msg = osc_message_builder.OscMessageBuilder(address=self.addr)

        for i in range(0,len(data)):
            msg.add_arg( data[i] )
            bundle.add_content(msg.build())
        
        bundle = bundle.build()
        self.client.send_message( bundle )

        pass
