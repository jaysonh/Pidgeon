
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

       #self.left_frame = Frame(self.root, width=self.width/2, height=self.height, bg='grey')
       #self.left_frame.grid(row=0, column=0, padx=10, pady=5)

       #self.right_frame = Frame(self.root, width=self.width/2, height=self.height, bg='grey')
       #self.right_frame.grid(row=0, column=1, padx=10, pady=5)



        self.deviceTab = GUIDisplayDevice(self.tabList[0], devicesJson[0])
        self.sensorTab = GUIDisplaySensor(self.tabList[1], sensorsJson[0])
        self.createDevicesListBox(self.tabList[0], devicesJson, self.root) #self.left_frame)
        self.createDevicesListBox(self.tabList[1], sensorsJson, self.root) #self.right_frame)

        #tabControl = ttk.Notebook(self.root) 

        #button = tk.Button(r, text='Stop', width=25, command=r.destroy)
        #button.pack()
        self.root.mainloop()

    def createDevicesListBox( self, root : Tk, items : json, frame : Frame ):
        
        self.listbox = Listbox(frame, height = 10, 
                    width = 15, 
                    bg = "grey",
                    activestyle = 'dotbox', 
                    font = "Helvetica",
                    fg = "yellow")
        
        self.listbox.bind( '<<ListboxSelect>>', self.onListboxSelectDevices )
        
        for i in items:
            print("inserting " + i["id"] + " to listbox")
            self.listbox.insert(END, i["id"])
            
        self.listbox.pack()
    
    def onListboxSelectDevices(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.deviceTab.destroy()
        self.deviceTab = GUIDisplayDevice(self.tabList[0], self.devices[index])

        print('You selected item %d: "%s"' % (index, value))
