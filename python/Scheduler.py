import json
import schedule
from crontab import CronTab


def hello_world( name : str ):
        print(f"hello world {name}")
        

class Scheduler:
    
    def __init__(self, schedule_json : json ):
        self.devices = {}
        
        for schedule_item in schedule_json:
            id = schedule_item["id"]
            device = schedule_item["deviceID"]
            #data = schedule_item["data"]

            self.parse_cron( schedule_item["time" ])
    
    def parse_cron( self, cron_time : str):
        try:
            # all these are numbers represented as strings
            sec  = cron_time.split(" ")[0]
            min  = cron_time.split(" ")[1]
            hour = cron_time.split(" ")[2] 
            dayMonth = cron_time.split(" ")[3]
            month = cron_time.split(" ")[4]
            dayWeek = cron_time.split(" ")[5]
            
            if dayWeek == "*":
                if month == "*":
                    if dayMonth == "*": # everyday
                        if hour == "*":
                            if min == "*":
                                if sec == "*":
                                    pass
                                else:
                                    timeStr = ":" + sec
                                    print(f"Scheduling every second at {timeStr}")
                                    schedule.every().minute.at(timeStr).do(hello_world, "jack")
                            else:
                                timeStr = ":" + min
                                print(f"Scheduling every minute at {timeStr}")
                                schedule.every().hour.at(timeStr).do(hello_world, "jack")
                                pass
                        else:
                            if min == "*":
                                minStr = "00"
                            if sec == "*":
                                secStr = "00"
                            timeStr = hour + ":" + minStr + ":" + secStr
                            print(f"Scheduling every day at {timeStr}")
                            schedule.every().day.at(timeStr).do(hello_world, "jack")
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