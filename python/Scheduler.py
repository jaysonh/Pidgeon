import json
import schedule
from crontab import CronTab
from DeviceHandler import DeviceHandler
from DeviceOutControl import DeviceOutControl
from ActionSet import ActionSet
from ActionRamp import ActionRamp
from DeviceMQTT import DeviceMQTT

def hello_world( name : str ):
        print(f"hello world {name}")
        
class ScheduleAction:
    deviceID = ""
    
    def __init__(self, deviceID : str,  d :DeviceOutControl ,a : ActionSet,):
        self.deviceID = deviceID
        self.action = a
        self.device = d


    def hello(self):
        print(f"setting {self.action.get()} from: {self.deviceID} ")
        self.device.outputDevice.sendData( self.action.get() )
       
class Scheduler:
    devices = {}        
    scheduleActions = {}    
    def __init__(self, schedule_json : json, devices : DeviceHandler ):

        
        for schedule_item in schedule_json:
            id = schedule_item["id"]
            deviceID = schedule_item["deviceID"]
            #data = schedule_item["data"]

            # need to find device with id = device
            
            if schedule_item["action"]["type"] == "setData":
                action = ActionSet( schedule_item["action"]["value"] )
            elif schedule_item["action"]["type"] == "setRamp":
                action = ActionRamp( schedule_item["action"]["start"], schedule_item["action"]["end"], schedule_item["action"]["duration"] )
            
            self.scheduleActions[ id ] = ScheduleAction( schedule_item["deviceID"], devices.get( deviceID ), action  )

            self.parse_cron( schedule_item["time"], self.scheduleActions[ id ])
    
    def parse_cron( self, cron_time : str, action : ScheduleAction ):
        try:
            # all these are numbers represented as strings
            sec  = cron_time.split(" ")[5]
            min  = cron_time.split(" ")[4]
            hour = cron_time.split(" ")[3] 
            dayMonth = cron_time.split(" ")[2]
            month = cron_time.split(" ")[2]
            dayWeek = cron_time.split(" ")[1]

            print(f"adding schedule item for time: {cron_time}")
            
            if dayWeek == "*":
                if month == "*":
                    if dayMonth == "*": # everyday
                        if hour == "*":
                            if min == "*":
                                if sec == "*":
                                    pass
                                else:
                                    if int(sec) < 10:
                                        timeStr = ":0" + sec
                                    else:
                                        timeStr = ":" + sec
                                    print(f"Scheduling every second at {timeStr}")
                                    schedule.every().minute.at(timeStr).do( action.hello )
                            else:
                                timeStr = ":" + min
                                print(f"Scheduling every minute at {timeStr}")
                                schedule.every().hour.at(timeStr).do( action.hello )
                                pass
                        else:
                            if min == "*":
                                minStr = "00"
                            if sec == "*":
                                secStr = "00"
                            timeStr = hour + ":" + minStr + ":" + secStr
                            print(f"Scheduling every day at {timeStr}")
                            schedule.every().day.at(timeStr).do(action.hello )
                            pass
                    else:
                        pass
                        #if min == "*":
                        #    minStr = "00"
                        #if sec == "*":
                        #    secStr = "00"
                        #if hour == "*":
                        #    hourStr = "00"
                        #timeStr = hourStr + ":" + minStr + ":" + secStr
                        #print(f"Scheduling every dayOfMonth at {timeStr}")
                else:
                    pass
            else:
                 if dayWeek == "0": # monday
                     pass
            

        except IndexError:
            print("Error: Invalid cron time format")

    
#    "id" : "s00001",
#               "time" : "0 * * * *",
#               "deviceID" : "00000001",
#               "data" : [ 0 ]