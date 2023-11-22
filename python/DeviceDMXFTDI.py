import json
from DeviceOutControl import DeviceOutControl
from dmx import Colour, DMXInterface, DMXLight3Slot, DMXUniverse

class DeviceDMXFTDI(DeviceOutControl):
    
    def __init__(self, json_data : json):
        super().__init__( json_data )

        self.host = json_data["host"]
        with DMXInterface("FT232R") as interface:
            # Create a universe
            self.interface = interface
            self.universe = DMXUniverse()
            self.light = DMXLight3Slot(address=0)
            self.universe.add_light(self.light)
            self.interface.set_frame(self.universe.serialise())
            self.interface.send_update()

            pass

    def sendData(self, v : []):
        self.value = v[0]

        self.interface.set_frame(self.universe.serialise())
        self.interface.send_update()
        
        pass
