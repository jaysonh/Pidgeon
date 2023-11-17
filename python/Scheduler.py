import json
from DeviceHandler import DeviceHandler
from SensorHandler import SensorHandler
from DeviceOutControl import DeviceOutControl
from ActionSet import ActionSet
from ActionRamp import ActionRamp
from ActionRampTarget import *
from DeviceMQTT import DeviceMQTT
import threading
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
             
class ScheduleAction:
    deviceID = ""
    
    def __init__(self, deviceID : str,  d :DeviceOutControl, a : ActionSet ):
        self.deviceID = deviceID
        self.action = a
        self.device = d

    def hello(self):
        self.time = str(datetime.now())
        self.action.run( self.device )
        #print(f"{self.time}setting {self.action.get()} from: {self.deviceID} ")  
        #self.device.sendData( self.action.get() )      
       
class Scheduler:
    devices = {}        
    scheduleActions = {}    
    def __init__(self, schedule_json : json, devices : DeviceHandler, sensors : SensorHandler ):

        print("starting scheduler")
        self.scheduler = BackgroundScheduler()
        for schedule_item in schedule_json:
            id = schedule_item["id"]
            deviceID = schedule_item["deviceID"]
            
            action = None
            if schedule_item["action"]["type"] == "setData":
                action = ActionSet( schedule_item["action"]["value"] )
            elif schedule_item["action"]["type"] == "setRamp":
                action = ActionRamp( schedule_item["action"]["start"], schedule_item["action"]["end"], schedule_item["action"]["duration"], schedule_item["action"]["interval"] )
            elif schedule_item["action"]["type"] == "setRampTarget":
                action = ActionRampTarget( schedule_item["action"]["target"], schedule_item["action"]["duration"], schedule_item["action"]["interval"] )
            else:
                print("ERROR invalid action type")

            if action != None:
                self.scheduleActions[ id ] = ScheduleAction( schedule_item["deviceID"], devices.get( deviceID ), action) #ActionRampTarget( schedule_item["action"]["target"], schedule_item["action"]["duration"], schedule_item["action"]["interval"] )  )
            
            self.parse_cron( schedule_item["time"], self.scheduleActions[ id ].hello )

        self.scheduler.start()

    def getTimeStr( self, cron_time : str ):

        sec      = cron_time.split(" ")[5]
        min      = cron_time.split(" ")[4]
        hour     = cron_time.split(" ")[3] 
        dayMonth = cron_time.split(" ")[2]
        month    = cron_time.split(" ")[2]
        dayWeek  = cron_time.split(" ")[1]

    def parse_cron( self, cron_time : str, action : ScheduleAction ):
        try:
            # all these are numbers represented as strings
            secCron  = cron_time.split(" ")[5]
            minCron  = cron_time.split(" ")[4]
            hourCron = cron_time.split(" ")[3] 
            dayMonthCron = cron_time.split(" ")[2]
            monthCron = cron_time.split(" ")[2]
            dayWeekCron = cron_time.split(" ")[1]
                         
            self.scheduler.add_job(action, 'cron', second=secCron, minute=minCron, hour=hourCron, day_of_week=dayWeekCron, month=monthCron )

        except IndexError:
            print("Error: Invalid cron time format")

    