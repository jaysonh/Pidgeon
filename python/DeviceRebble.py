import json
import requests
from DeviceOutControl import DeviceOutControl

class DeviceRebble(DeviceOutControl):
    def __init__(self, json_data : json    ):
        super().__init__( json_data)
        self.remoteAddr = json_data["remoteAddr"] #"192.168.1.101"

    def sendData(self, v : float ):
        print(f"sendData Rebble: {v}")
        self.value = int(v)

        url = "http://" + self.remoteAddr + "/set_single.html?value=" + str(self.value) + "&id=4"

        response = requests.get(url)
        response_json = response.json()
        print(response_json)

        pass

        
