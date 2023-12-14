import json
from ActionSet import ActionSet
from ActionRamp import ActionRamp
from ActionRampTarget import *
from ScheduleAction import *

from apscheduler.schedulers.background import BackgroundScheduler

class LogicUnit:
    def __init__(self, json_data : json):
        self.name = json_data["name"]
        self.id   = json_data["id"]
        self.inputDeviceID = json_data["inputDevice"]   # : "sens00000004",
        self.outputDeviceID = json_data["outputDevice"] # : "00000010",
        self.jsonLogic = json_data["logic"] # : { ">": [{"var": "temp"}, 30]},
        self.updateCronTime = json_data["updateTime"]
        self.action = self.selectAction(json_data["action"], self.updateCronTime)
        pass

    def selectAction(self, json_data : json, updateTime ):
        if json_data["type"] == "setData":
            self.action = ActionSet( json_data )
        elif json_data["type"] == "setRamp":
            self.action = ActionRamp( json_data )
        elif json_data["type"] == "setRampTarget":
            self.action = ActionRampTarget( json_data )
        else:
            self.action = None
            print("ERROR invalid action type")
        #if action != None:
        #    self.scheduleActions[ id ] = ScheduleAction( schedule_item["deviceID"], devices.get( deviceID ), action) #ActionRampTarget( schedule_item["action"]["target"], schedule_item["action"]["duration"], schedule_item["action"]["interval"] )  )
        #
        self.parse_cron( updateTime, self.action.run )

    def parse_cron( self, cron_time : str, action : ScheduleAction ):
        try:
            # all these are numbers represented as strings
            self.secCron  = cron_time.split(" ")[5]
            self.minCron  = cron_time.split(" ")[4]
            self.hourCron = cron_time.split(" ")[3] 
            self.dayMonthCron = cron_time.split(" ")[2]
            self.monthCron = cron_time.split(" ")[2]
            self.dayWeekCron = cron_time.split(" ")[1]
                         
            #self.scheduler.add_job(action, 'cron', second=secCron, minute=minCron, hour=hourCron, day_of_week=dayWeekCron, month=monthCron )

        except IndexError:
            print("Error: Invalid cron time format")

    def add_cron(self, scheduler : BackgroundScheduler):
        scheduler.add_job(self.action, 'cron', second=self.secCron, minute=self.minCron, hour=self.hourCron, day_of_week=self.dayWeekCron, month=self.monthCron )