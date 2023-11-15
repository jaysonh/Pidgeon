import json
from crontab import CronTab
from DeviceHandler import DeviceHandler
from DeviceOutControl import DeviceOutControl
from ActionSet import ActionSet
from ActionRamp import ActionRamp
from DeviceMQTT import DeviceMQTT
import threading
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
     
def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()   

def job():
    print(f"running job ", str(datetime.now()))

def hello_world( name : str ):
        print(f"hello world {name}")
        
class ScheduleAction:
    deviceID = ""
    
    def __init__(self, deviceID : str,  d :DeviceOutControl, a : ActionSet ):
        self.deviceID = deviceID
        self.action = a
        self.device = d

    def hello(self):
        print(f"setting {self.action.get()} from: {self.deviceID} ")
        
        action.start()
        while action.is_running():
            self.device.outputDevice.sendData( self.action.get() )
       
class Scheduler:
    devices = {}        
    scheduleActions = {}    
    def __init__(self, schedule_json : json, devices : DeviceHandler ):

        print("starting scheduler")
        self.scheduler = BackgroundScheduler()
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

        self.scheduler.start()

    def getTimeStr( self, cron_time : str ):

        sec  = cron_time.split(" ")[5]
        min  = cron_time.split(" ")[4]
        hour = cron_time.split(" ")[3] 
        dayMonth = cron_time.split(" ")[2]
        month = cron_time.split(" ")[2]
        dayWeek = cron_time.split(" ")[1]

        pass

    def parse_cron( self, cron_time : str, action : ScheduleAction ):
        try:
            # all these are numbers represented as strings
            secCron  = cron_time.split(" ")[5]
            minCron  = cron_time.split(" ")[4]
            hourCron = cron_time.split(" ")[3] 
            dayMonthCron = cron_time.split(" ")[2]
            monthCron = cron_time.split(" ")[2]
            dayWeekCron = cron_time.split(" ")[1]
                         
            self.scheduler.add_job(job, 'cron', second=secCron, minute=minCron, hour=hourCron, day_of_week=dayWeekCron, month=monthCron )

        except IndexError:
            print("Error: Invalid cron time format")

    
#    "id" : "s00001",
#               "time" : "0 * * * *",
#               "deviceID" : "00000001",
#               "data" : [ 0 ]