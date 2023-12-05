
from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
from GUIDisplayDevice import *
from GUIDisplaySensor import *

class GuiMainWindow( ):
    def __init__(self, jsonSettings : json, devicesJson : json, sensorsJson : json ):
        #jsonSettings : json, devicesJson : json, sensorsJson : json):
        print(jsonSettings)
        self.root = tk.Tk()

        self.devices = devicesJson
        self.sensors = sensorsJson

        self.tabControl = ttk.Notebook(self.root) 
        self.title = jsonSettings[0]["title"]
        self.width = jsonSettings[0]["width"]
        self.height = jsonSettings[0]["height"]
        dimStr = str(self.width) + "x" + str(self.height)
        print(f"Creating window with title {self.title}")
        self.root.title( self.title)
        self.root.geometry( dimStr)

        tabListJson = jsonSettings[0]["tabs"]

        print("num tabs: " + str(len(tabListJson)))

        self.tabList = []
        for tabJson in tabListJson:
            tab = ttk.Frame(self.tabControl)
            self.tabList.append(tab)
            self.tabControl.add(tab, text =tabJson["title"]) 
            print(f"adding tab {tabJson['title']}")
        
        self.tabControl.pack(expand = 1, fill ="both") 

        self.createDevicesListBox(self.tabList[0], devicesJson, self.tabList[0], self.onListboxSelectDevices) #self.left_frame)
        self.createDevicesListBox(self.tabList[1], sensorsJson, self.tabList[1], self.onListboxSelectSensors) #self.right_frame)
        
        self.deviceTab = GUIDisplayDevice(self.tabList[0], devicesJson[0])
        self.sensorTab = GUIDisplaySensor(self.tabList[1], sensorsJson[0])

        self.root.mainloop()

    def createDevicesListBox( self, root : Tk, items : json, frame : Frame, func ):
        
        self.listbox = Listbox(frame, height = 10, 
                    width = 15, 
                    bg = "grey",
                    activestyle = 'dotbox', 
                    font = "Helvetica",
                    fg = "yellow")
        
        #self.listbox.bind( '<<ListboxSelect>>', self.onListboxSelectDevices )
        self.listbox.bind( '<<ListboxSelect>>', func )
        
        for i in items:
            print("inserting " + i["id"] + " to listbox")
            self.listbox.insert(END, i["id"])
            
        self.listbox.pack()
    
    def onListboxSelectDevices(self, evt):
        w = evt.widget
        if len(w.curselection()) >= 0:
            index = int(w.curselection()[0])
            value = w.get(index)
            self.deviceTab.destroy()
            self.deviceTab = GUIDisplayDevice(self.tabList[0], self.devices[index])

            print('You selected item %d: "%s"' % (index, value))

    def onListboxSelectSensors(self, evt):
        w = evt.widget
        if len(w.curselection()) >= 0:
            index = int(w.curselection()[0])
            value = w.get(index)
            self.sensorTab.destroy()
            self.sensorTab = GUIDisplaySensor(self.tabList[1], self.sensors[index])

            print('You selected item %d: "%s"' % (index, value))
