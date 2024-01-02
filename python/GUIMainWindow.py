
from tkinter import *
from tkinter import ttk
import tkinter as tk
import json

from GUIDisplayDeviceOut import *
from GUIDisplayDeviceIn import *
from GuiScheduleDisplay import *
from GuiDisplayLogic import *
from JsonParams import *
from ttkthemes import ThemedTk

class GuiMainWindow( ):
    #def __init__(self, jsonSettings : json, devicesJson : json, sensorsJson : json , scheduleJson : json, logicJson : json):
    def __init__(self, ui_settings : JsonParams, devicesJson : JsonParams, sensorsJson : JsonParams , scheduleJson : JsonParams, logicJson : JsonParams):
         
        self.root = ThemedTk(theme="clam")

        self.devices = devicesJson
        self.sensors = sensorsJson
        self.logic   = logicJson

        self.tabControl = ttk.Notebook(self.root) 
        self.title  = ui_settings.getJson()[0]["title"]
        self.width  = ui_settings.getJson()[0]["width"]
        self.height = ui_settings.getJson()[0]["height"]
        dimStr = str(self.width) + "x" + str(self.height)
        print(f"Creating window with title {self.title}")

        self.root.title( self.title)
        self.root.geometry( dimStr)

        tabListJson = ui_settings.getJson()[0]["tabs"]

        print("num tabs: " + str(len(tabListJson)))

        self.tabList = []
        for tabJson in tabListJson:
            tab = ttk.Frame(self.tabControl)
            self.tabList.append(tab)
            self.tabControl.add(tab, text =tabJson["title"]) 
            print(f"adding tab {tabJson['title']}")
        
        self.tabControl.pack(fill ="both")

        #self.devicesListBox = self.createDevicesListBox(self.tabList[0], devicesJson.getJson(), self.tabList[0], self.onListboxSelectDevices ) 
        #self.sensorsListBox = self.createDevicesListBox(self.tabList[1], sensorsJson.getJson(), self.tabList[1], self.onListboxSelectSensors) 
        #self.logicListBox = self.createDevicesListBox(self.tabList[3], logicJson.getJson(), self.tabList[3], self.onListboxSelectLogic) 
        
        self.deviceTab = GUIDisplayDeviceOut ( self.tabList[0], devicesJson.getJson()[0], devicesJson, devicesJson.addWithoutKey, devicesJson.save_file )
        self.sensorTab = GUIDisplayDeviceIn  ( self.tabList[1], sensorsJson.getJson()[0], sensorsJson, sensorsJson.addWithoutKey, sensorsJson.save_file )
        self.scheduleTab = GuiScheduleDisplay( self.tabList[2], scheduleJson.getJson(), scheduleJson.addWithoutKey, scheduleJson.save_file)
        self.logicTab = GuiDisplayLogic      ( self.tabList[3], logicJson.getJson()[0], logicJson, logicJson.addWithoutKey, logicJson.save_file)


        self.root.mainloop()
