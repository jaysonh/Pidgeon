
from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
from JsonParams import *
from Logging import *

class GUIDisplayDeviceIn:

    def __init__(self, root : Tk,  json_data_parent : JsonParams, addJsonFunc = None, saveJsonFunc = None, removeJsonFunc = None):

        
        logger.info("creating GUIDisplayDeviceIn")
        
        self.parent = root
        self.addJsonFunc = addJsonFunc
        self.removeJsonFunc = removeJsonFunc
             
        self.sensors = json_data_parent

        self.bottomframe = Frame(root)
        self.bottomframe.pack( side = BOTTOM )
        self.addButton = Button(self.bottomframe, text ="add", command = self.openAddDeviceInDialog)
        self.addButton.pack(side="right", fill="none", expand=False)
        self.removeButton = Button(self.bottomframe, text ="remove", command = self.removeDeviceInItem)
        self.removeButton.pack(side="left", fill="none", expand=False)
        self.saveButton = Button(self.bottomframe, text ="save", command = saveJsonFunc)
        self.saveButton.pack(side="left", fill="none", expand=False)

        self.tree = ttk.Treeview(root, columns=2, show=["headings"])
        self.tree["columns"]=("paramName","paramValue")
        self.tree.column("paramName", width=100 )
        self.tree.column("paramValue", width=100)
        self.tree.heading("paramName", text="Name")
        self.tree.heading("paramValue", text="Value")

        if json_data_parent.GetNumData() > 0:
            json_data = json_data_parent.getJson()[0]
            self.tree.insert("" , "end",     values=("Name",json_data["name"]))
            self.tree.insert("" , "end",     values=("ID",json_data["id"]))
            self.tree.insert("" , "end",     values=("Type",json_data["type"]))
        else:
            self.tree.insert("" , "end",     values=("Name","" ))
            self.tree.insert("" , "end",     values=("ID",  "" ))
            self.tree.insert("" , "end",     values=("Type","" ))
        
        self.tree.pack(side="top", fill="both", expand=True)
        self.createDevicesListBox(root, json_data_parent.getJson(), root, self.onListboxSelectSensors ) 
        
        
    def replaceDevicesListBox(self, items : json):
        
        # clear treeview
        self.sensorsListBox.delete(*self.sensorsListBox.get_children())

        # add data to the treeview
        for i in items:
            self.sensorsListBox.insert('', tk.END, values=i["id"])             
        pass

    def createDevicesListBox( self, root : Tk, items : json, frame : Frame, func ):

        self.midframe = Frame(root)
        self.midframe.pack( side = TOP )
        
        self.sensorsListBox = ttk.Treeview(self.midframe, columns=("Column1"))
        self.sensorsListBox.pack(side="left", fill="both", expand=True)
        contacts = []
        for i in items:     
            contacts.append(i["id"])
        # add data to the treeview
        for contact in contacts:
            self.sensorsListBox.insert('', tk.END, values=contact)
        self.sensorsListBox.bind("<<TreeviewSelect>>", func )

        #
        #listbox = ttk.Treeview(root, selectmode="extended",show='headings')
        #listbox.pack()
        #
        #listbox = ttk.Treeview(root, columns=("Column1"))
        #listbox.pack(side="bottom", fill="both", expand=True)
        #       
        #contacts = []
        #for i in items:     
        #    contacts.append(i["id"])
        ## add data to the treeview
        #for contact in contacts:
        #    listbox.insert('', tk.END, values=contact)
        #listbox.bind("<<TreeviewSelect>>", func )
        #return listbox    

    def onListboxSelectSensors(self, evt):

        if len(self.sensors.getJson()) > 0:
            selection = self.sensorsListBox.selection()
            current_idx = self.sensorsListBox.index(selection)
            self.fromJson(self.sensors.getJson()[current_idx] )    

    def fromJson(self, json_data : json):
                
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.tree.insert("" , "end", values=("Name",json_data["name"]))
        self.tree.insert("" , "end", values=("ID",json_data["id"]))
        self.tree.insert("" , "end", values=("Type",json_data["type"]))


    def openAddDeviceInDialog(self):
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

        # device type input
        frame_type_input = Frame(self.pop, bg="gray71")
        frame_type_input.pack(pady=2)
        type_label = tk.Label( frame_type_input, text="type")
        type_label.grid(row=0, column=1)
        self.type_input = tk.Text(frame_type_input, 
                   height = 1, 
                   width = 20)
        self.type_input.grid(row=0, column=2)
                
        # Add a Frame
        frameBtns = Frame(self.pop, bg="gray71")
        frameBtns.pack(pady=10)
        # Add Button for making selection
        button1 = Button(frameBtns, text="add", command=self.okDialog, bg="grey", fg="white")
        button1.grid(row=0, column=1)
        button2 = Button(frameBtns, text="cancel", command= self.closeDialog, bg="grey", fg="white")
        button2.grid(row=0, column=2)
        
        # device type input
       
            #    "name" : "sensor02",
            #    "id"   : "sens00000005",
            #    "type" : "mqtt",
        pass

    def removeDeviceInItem(self):        
        selection = self.sensorsListBox.selection()
        self.removeJsonFunc( self.sensorsListBox.index(selection) )
        self.sensorsListBox.delete( selection )
        pass

    def destroy(self):
        self.listbox.destroy()
        pass

    def closeDialog(self):
        self.pop.destroy()
        self.pop.update()

    def okDialog(self):
        json_data = { "name" : self.name_input.get("1.0", 'end-1c'), 
                      "id" : self.id_input.get("1.0", 'end-1c'),
                      "type" : self.type_input.get("1.0", 'end-1c') }
        logger.info(f"saving deviceIn: {json_data}")
        print(json_data)
        self.addJsonFunc( json_data )
        self.replaceDevicesListBox(self.sensors.getJson())
        self.pop.destroy()
        self.pop.update()