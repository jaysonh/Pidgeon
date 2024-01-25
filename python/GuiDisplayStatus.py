from Scheduler import Scheduler
import tkinter as tk
from tkinter import ttk
from tkinter import *
import json
from Logging import *
from Event import *
import threading
import time
from datetime import datetime

class GuiDisplayStatus:
    deviceID = ""
    
    def __init__(self, root : tk ):
        self.start_time = time.time()

        logger.info("Initialising GuiStatusDisplay")
        self.parent = root
        
        # current time label
        frame_name_input = Frame(self.parent, bg="gray71")
        frame_name_input.pack(pady=2)
        self.current_time_label = tk.Label( frame_name_input, text="Current Time: ")
        self.current_time_label.grid(row=0, column=1)

        # uptime label
        frame_name_input = Frame(self.parent, bg="gray71")
        frame_name_input.pack(pady=2)
        self.uptime_label = tk.Label( frame_name_input, text="Uptime: ")
        self.uptime_label.grid(row=0, column=1)
        
        uptimeThread = threading.Thread(target=self.updateUpTime)
        self.runningUptime = True
        uptimeThread.start()
        
        currentTimeThread = threading.Thread(target=self.updateCurrentTime)
        self.runningCurrentTime = True
        currentTimeThread.start()

        self.bottomframe = Frame(root)
        self.bottomframe.pack( side = BOTTOM )

        self.addButton = Button(self.bottomframe, text ="ok")
        self.addButton.pack(side="right", fill="none", expand=False)

    def getUpTime(self)->str:
        elapsed_time = time.time() - self.start_time
        secs = int(elapsed_time) % 60
        min  = int(int(elapsed_time) / 60)% 60
        hour  = int(int(elapsed_time) /3600)% 24

        padding_lambda = lambda x,length: x if len(str(x)) >= length else f"0{x}"

        timeStr = padding_lambda(hour,24) + ":" + padding_lambda(min,60) + ":" + padding_lambda(secs,60)
        return timeStr
    def updateUpTime(self):
        while self.runningUptime:
            # Code to be executed in the thread
            new_label = "Uptime: " + self.getUpTime()
            self.uptime_label.config(text=new_label)
            time.sleep(1)

    def updateCurrentTime(self):
        while self.runningCurrentTime:
            # Code to be executed in the thread
            current_time = datetime.now()
            new_label = "Current Local Time: " + current_time.strftime("%H:%M:%S")
            self.current_time_label.config(text=new_label)           
            time.sleep(1)
        