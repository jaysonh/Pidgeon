from Configuration import Configuration
from DeviceHandler import DeviceHandler

version = "0.0.1"

if __name__ == "__main__":
    print(f"Pigeon version {version}")

    configuration = Configuration( ["../data/config/devices.json", "../data/config/schedule.json"] )
    device_handler = DeviceHandler( configuration.get("devices") )
   