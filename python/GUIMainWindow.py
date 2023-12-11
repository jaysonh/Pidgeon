
from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
from GUIDisplayDeviceOut import *
from GUIDisplayDeviceIn import *
from ttkthemes import ThemedTk

class GuiMainWindow( ):
    def __init__(self, jsonSettings : json, devicesJson : json, sensorsJson : json ):
        #jsonSettings : json, devicesJson : json, sensorsJson : json):
        print(jsonSettings)
        #self.root = tk.Tk()
        self.root = ThemedTk(theme="clam")

        self.devices = devicesJson
        self.sensors = sensorsJson

        self.tabControl = ttk.Notebook(self.root) 
        self.title  = jsonSettings[0]["title"]
        self.width  = jsonSettings[0]["width"]
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
        
        self.tabControl.pack(fill ="both")

        self.devicesListBox = self.createDevicesListBox(self.tabList[0], devicesJson, self.tabList[0], self.onListboxSelectDevices) 
        self.sensorsListBox = self.createDevicesListBox(self.tabList[1], sensorsJson, self.tabList[1], self.onListboxSelectSensors) 
        
        self.deviceTab = GUIDisplayDeviceOut(self.tabList[0], devicesJson[0])
        self.sensorTab = GUIDisplayDeviceIn (self.tabList[1], sensorsJson[0])

        self.root.mainloop()

    def createDevicesListBox( self, root : Tk, items : json, frame : Frame, func ) -> ttk.Treeview:
        listbox = ttk.Treeview(root, selectmode="extended",show='headings')
        listbox.pack()
        
        listbox = ttk.Treeview(root, columns=("Column1"))
        listbox.pack(side="bottom", fill="both", expand=True)
               
        contacts = []
        for i in items:     
            contacts.append(i["id"])

        # add data to the treeview
        for contact in contacts:
            listbox.insert('', tk.END, values=contact)
 
        listbox.bind("<<TreeviewSelect>>", func )

        return listbox

    
    def onListboxSelectDevices(self, evt):
        selection = self.devicesListBox.selection()
        current_idx = self.devicesListBox.index(selection)
        print("selection: " +  str(current_idx)) 
        
        self.deviceTab.destroy()
        self.deviceTab = GUIDisplayDeviceOut(self.tabList[0], self.devices[current_idx])
        
        
        #curItem = self.devicesListBox.focus()

    def onListboxSelectSensors(self, evt):
        selection = self.sensorsListBox.selection()
        current_idx = self.sensorsListBox.index(selection)
        print("selection: " +  str(current_idx))
        self.sensorTab.destroy()
        self.sensorTab = GUIDisplayDeviceOut(self.tabList[1],  self.sensors[current_idx])
        #curItem = self.devicesListBox.focus()
