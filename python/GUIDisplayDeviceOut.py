
from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
from tkinter.filedialog import asksaveasfile
from JsonParams import *

class GUIDisplayDeviceOut:

    def __init__(self, root : Tk, json_data_parent : JsonParams, addJsonFunc = None, saveJsonFunc = None, removeJsonFunc = None):

        logger.info("creating GUIDisplayDeviceOut")
        
        self.parent = root
        self.addJsonFunc = addJsonFunc
        self.removeJsonFunc = removeJsonFunc
        self.devices = json_data_parent
        self.bottomframe = Frame(root)
        self.bottomframe.pack( side = BOTTOM )
        
        self.topframe = Frame(root)
        self.topframe.pack( side = BOTTOM )

        self.addButton = Button(self.bottomframe, text ="add", command = self.openAddDeviceOutDialog)
        self.addButton.pack(side="right", fill="none", expand=False)
        
        self.removeButton = Button(self.bottomframe, text ="remove", command = self.removeDeviceOutItem)
        self.removeButton.pack(side="left", fill="none", expand=False)

        self.saveButton = Button(self.bottomframe, text ="save", command = saveJsonFunc)
        self.saveButton.pack(side="left", fill="none", expand=False)

        self.tree = ttk.Treeview(self.topframe)
        self.tree["columns"]=("paramName","paramValue")
        self.tree.column("paramName", width=100 )
        self.tree.column("paramValue", width=100)
        self.tree.heading("paramName", text="Name")
        self.tree.heading("paramValue", text="Value")

        if json_data_parent.GetNumData() > 0:
            json_data = json_data_parent.getJson()[0]
            self.tree.insert("" , "end",    text="Line 1", values=("Name",json_data["name"]))
            self.tree.insert("" , "end",    text="Line 1", values=("ID",json_data["id"]))
            self.tree.insert("" , "end",    text="Line 1", values=("Type",json_data["type"]))
            self.tree.insert("" , "end",    text="Line 1", values=("Num Channels",json_data["numChannels"]))
        else:
            self.tree.insert("" , "end",    text="Line 1", values=("Name",""))
            self.tree.insert("" , "end",    text="Line 1", values=("ID",  ""))
            self.tree.insert("" , "end",    text="Line 1", values=("Type",""))
            self.tree.insert("" , "end",    text="Line 1", values=("Num Channels",""))
    
        self.tree.pack(side=TOP, fill="both", expand=True)

        self.createDevicesListBox(root, json_data_parent.getJson(), root, self.onListboxSelectDevices ) 


    def onListboxSelectDevices(self, evt):
        
        selection = self.devicesListBox.selection()
        current_idx = self.devicesListBox.index(selection)        
        self.fromJson(self.devices.getJson()[current_idx] )

    def createDevicesListBox( self, root : Tk, items : json, frame : Frame, func ):
        self.midframe = Frame(root)
        self.midframe.pack( side = TOP )
        
        self.devicesListBox = ttk.Treeview(self.midframe, columns=("Column1"))
        self.devicesListBox.pack(side="left", fill="both", expand=True)
            
        contacts = []
        for i in items:     
            contacts.append(i["id"])
        # add data to the treeview
        for contact in contacts:
            self.devicesListBox.insert('', tk.END, values=contact)
        self.devicesListBox.bind("<<TreeviewSelect>>", func )

    def replaceDevicesListBox(self, items : json):
        
        # clear treeview
        self.devicesListBox.delete(*self.devicesListBox.get_children())

        # add data to the treeview
        for i in items:
            self.devicesListBox.insert('', tk.END, values=i["id"])             
        pass

    def fromJson(self, json_data : json):
                
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.tree.insert("" , "end",    text="Line 1", values=("Name",json_data["name"]))
        self.tree.insert("" , "end",    text="Line 1", values=("ID",json_data["id"]))
        self.tree.insert("" , "end",    text="Line 1", values=("Type",json_data["type"]))
        self.tree.insert("" , "end",    text="Line 1", values=("Num Channels",json_data["numChannels"]))

    def openAddDeviceOutDialog(self):
        #global pop
        self.pop = Toplevel(self.parent)
        self.pop.title("Add Input Device")
        self.pop.geometry("450x450")
        self.pop.config(bg="white")

        
        # device name input
        frame_name_input = Frame(self.pop, bg="gray71")
        frame_name_input.pack(pady=2)
        name_label = tk.Label( frame_name_input, text="name")
        name_label.grid(row=0, column=1)
        self.name_input = tk.Text(frame_name_input, 
                   height = 1, 
                   width = 20)
        self.name_input.grid(row=0, column=2)

        
        # device id input
        frame_id_input = Frame(self.pop, bg="gray71")
        frame_id_input.pack(pady=2)
        id_label = tk.Label( frame_id_input, text="id")
        id_label.grid(row=0, column=1)
        self.id_input = tk.Text(frame_id_input, 
                   height = 1, 
                   width = 20)
        self.id_input.grid(row=0, column=2)

        
        # Add a Frame
        frameBtns = Frame(self.pop, bg="gray71")
        frameBtns.pack(pady=10)
        # Add Button for making selection
        button1 = Button(frameBtns, text="add", command=self.okDialog, bg="grey", fg="white")
        button1.grid(row=0, column=1)
        button2 = Button(frameBtns, text="cancel", command= self.closeDialog, bg="grey", fg="white")
        button2.grid(row=0, column=2)

        pass

    def removeDeviceOutItem(self):
        
        selection = self.devicesListBox.selection()
        self.removeJsonFunc( self.devicesListBox.index(selection) )
        self.devicesListBox.delete( selection )

    def closeDialog(self):
        self.pop.destroy()
        self.pop.update()

    def okDialog(self):

        json_data = { "name" : self.name_input.get("1.0", 'end-1c'), "id" : self.id_input.get("1.0", 'end-1c') }
        logger.info(f"saving deviceOut json: {json_data}")
       
        self.addJsonFunc( json_data )
        # update the listbox
        self.replaceDevicesListBox(self.devices.getJson())

        self.pop.destroy()
        self.pop.update()