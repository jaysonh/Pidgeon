from Scheduler import Scheduler
import tkinter as tk
from tkinter import ttk
from tkinter import *
import json
from JsonParams import *
from Logging import *

class GuiDisplayLogic:
    def __init__(self, root : tk , json_data : json,json_data_parent : JsonParams,  addJsonFunc = None, saveJsonFunc = None, removeJsonFunc = None) -> None:
        
        logger.info("creating GuiDisplayLogic")
        self.parent = root
        self.addJsonFunc = addJsonFunc
        self.removeJsonFunc = removeJsonFunc
        self.logic = json_data_parent

        self.tree = ttk.Treeview(root)
        self.tree["columns"]=("paramName","paramValue")
        self.tree.column("paramName", width=100 )
        self.tree.column("paramValue", width=100)
        self.tree.heading("paramName", text="Name")
        self.tree.heading("paramValue", text="Value")
        self.tree.insert("" , "end", text="Line 1", values=("Name",json_data["name"]))
        self.tree.insert("" , "end", text="Line 1", values=("ID",json_data["id"]))
        self.tree.insert("" , "end", text="Line 1", values=("inputDevice",json_data["inputDevice"]))
        self.tree.insert("" , "end", text="Line 1", values=("outputDevice",json_data["outputDevice"]))
        self.tree.insert("" , "end", text="Line 1", values=("updateTime",json_data["updateTime"]))
        self.tree.insert("" , "end", text="Line 1", values=("logic",json_data["logic"]))
        self.tree.insert("" , "end", text="Line 1", values=("action",json_data["action"]))
        self.tree.pack(side="top", fill="both", expand=True)
           
        self.bottomframe = Frame(root)
        self.bottomframe.pack( side = BOTTOM )

        self.addButton = Button(self.bottomframe, text ="add", command = self.openAddLogicDialog)
        self.addButton.pack(side="right", fill="none", expand=False)
        
        self.removeButton = Button(self.bottomframe, text ="remove", command = self.removeLogicItem)
        self.removeButton.pack(side="left", fill="none", expand=False)

        self.saveButton = Button(self.bottomframe, text ="save", command = saveJsonFunc)
        self.saveButton.pack(side="left", fill="none", expand=False)

        self.logicListBox = self.createDevicesListBox(root, json_data_parent.getJson(), root, self.onListboxSelectDevices ) 

    def replaceDevicesListBox(self, items : json):
        
        # clear treeview
        self.logicListBox.delete(*self.logicListBox.get_children())

        # add data to the treeview
        for i in items:
            self.logicListBox.insert('', tk.END, values=i["id"])             
        pass

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
        selection = self.logicListBox.selection()
        current_idx = self.logicListBox.index(selection)
        self.fromJson(self.logic.getJson()[current_idx] )

    def openAddLogicDialog(self):
        #global pop
        self.pop = Toplevel(self.parent)
        self.pop.title("Add Logic Item")
        self.pop.geometry("450x450")
        self.pop.config(bg="white")
        
        
        # cron schedule input
        frame_cron_input = Frame(self.pop, bg="gray71")
        frame_cron_input.pack(pady=2)
        cron_label = tk.Label( frame_cron_input, text="update time")
        cron_label.grid(row=0, column=1)

        cron_second_label = tk.Label( frame_cron_input, text="sec")
        cron_second_label.grid(row=0, column=2)
        self.cron_second_var = tk.StringVar() 
        cron_second = ttk.Combobox(frame_cron_input, width = 2, textvariable = self.cron_second_var)
        cron_second['values'] = ('*', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59' ) 
        cron_second.current(0)
        cron_second.grid(row = 0, column = 3) 
        
        cron_minute_label = tk.Label( frame_cron_input, text="min")
        cron_minute_label.grid(row=0, column=4)
        self.cron_minute_var = tk.StringVar() 
        cron_minute = ttk.Combobox(frame_cron_input, width = 2, textvariable = self.cron_minute_var)
        cron_minute['values'] = ('*', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59') 
        cron_minute.current(0)
        cron_minute.grid(row = 0, column = 5) 
     
        cron_hour_label = tk.Label( frame_cron_input, text="hour")
        cron_hour_label.grid(row=0, column=5)
        self.cron_hour_var = tk.StringVar() 
        cron_hour = ttk.Combobox(frame_cron_input, width = 2, textvariable = self.cron_hour_var)
        cron_hour['values'] = ( '*', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24' ) 
        cron_hour.current(0)
        cron_hour.grid(row = 0, column = 6) 
        
        cron_day_label = tk.Label( frame_cron_input, text="day")
        cron_day_label.grid(row=0, column=7)
        self.cron_day_var = tk.StringVar() 
        cron_day = ttk.Combobox(frame_cron_input, width = 2, textvariable = self.cron_day_var)
        cron_day['values'] = ('*', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31') 
        cron_day.current(0)
        cron_day.grid(row = 0, column = 8) 

        cron_month_label = tk.Label( frame_cron_input, text="month")
        cron_month_label.grid(row=0, column=9)
        self.cron_month_var = tk.StringVar() 
        cron_month = ttk.Combobox(frame_cron_input, width = 2, textvariable = self.cron_month_var)
        cron_month['values'] = ('*', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12') 
        cron_month.current(0)
        cron_month.grid(row = 0, column = 10) 
        
        cron_day_week_label = tk.Label( frame_cron_input, text="day_week")
        cron_day_week_label.grid(row=0, column=11)
        self.cron_day_week_var = tk.StringVar() 
        cron_day_week = ttk.Combobox(frame_cron_input, width = 2, textvariable = self.cron_day_week_var)
        cron_day_week['values'] = ('*', '1', '2', '3', '4', '5', '6', '7') 
        cron_day_week.current(0)
        cron_day_week.grid(row = 0, column = 12) 

        #frame_address_input = Frame(self.pop, bg="gray71")
        #frame_address_input.pack(pady=2)
        #address_label = tk.Label( frame_address_input, text="address")
        #address_label.grid(row=0, column=1)
        #address_input = tk.Text(frame_address_input, 
        #           height = 1, 
        #           width = 20) 
        #address_input.grid(row=0, column=2)

        # device id input
        frame_name_input = Frame(self.pop, bg="gray71")
        frame_name_input.pack(pady=2)
        name_label = tk.Label( frame_name_input, text="name")
        name_label.grid(row=0, column=1)
        self.name_input = tk.Text(frame_name_input, 
                   height = 1, 
                   width = 20) 
        self.name_input.grid(row=0, column=2)

        # address input
        frame_id_input = Frame(self.pop, bg="gray71")
        frame_id_input.pack(pady=2)
        id_label = tk.Label( frame_id_input, text="id")
        id_label.grid(row=0, column=1)
        self.id_input = tk.Text(frame_id_input, 
                   height = 1, 
                   width = 20) 
        self.id_input.grid(row=0, column=2)

        # input device input
        frame_input_device = Frame(self.pop, bg="gray71")
        frame_input_device.pack(pady=2)
        input_device_label = tk.Label( frame_input_device, text="input device")
        input_device_label.grid(row=0, column=1)
        self.in_device_input = tk.Text(frame_input_device, 
                   height = 5, 
                   width = 20) 
        self.in_device_input.grid(row=0, column=2)
        
        # output device input
        frame_output_device = Frame(self.pop, bg="gray71")
        frame_output_device.pack(pady=2)
        output_device_label = tk.Label( frame_output_device, text="output device")
        output_device_label.grid(row=0, column=1)
        self.out_device_input = tk.Text(frame_output_device, 
                   height = 5, 
                   width = 20) 
        self.out_device_input.grid(row=0, column=2)
        
        # output device input
        frame_logic = Frame(self.pop, bg="gray71")
        frame_logic.pack(pady=2)
        logic_label = tk.Label( frame_logic, text="logic")
        logic_label.grid(row=0, column=1)
        self.logic_input = tk.Text(frame_logic, 
                   height = 5, 
                   width = 20) 
        self.logic_input.grid(row=0, column=2)
        
        # output device input
        frame_action = Frame(self.pop, bg="gray71")
        frame_action.pack(pady=2)
        action_label = tk.Label( frame_action, text="action")
        action_label.grid(row=0, column=1)
        self.action_input = tk.Text(frame_action, 
                   height = 5, 
                   width = 20) 
        self.action_input.grid(row=0, column=2)


        # Add a Frame
        frameBtns = Frame(self.pop, bg="gray71")
        frameBtns.pack(pady=10)
        # Add Button for making selection
        button1 = Button(frameBtns, text="add", command=self.okDialog, bg="grey", fg="white")
        button1.grid(row=0, column=1)
        button2 = Button(frameBtns, text="cancel", command= self.closeDialog, bg="grey", fg="white")
        button2.grid(row=0, column=2)
        pass

    def fromJson(self, json_data : json):
        pass        
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.tree.insert("" , "end",    text="Line 1", values=("Name",json_data["name"]))
        self.tree.insert("" , "end",    text="Line 1", values=("ID",json_data["id"]))
        self.tree.insert("" , "end",    text="Line 1", values=("inputDevice",json_data["inputDevice"]))
        self.tree.insert("" , "end",    text="Line 1", values=("outputDevice",json_data["outputDevice"]))
        self.tree.insert("" , "end",    text="Line 1", values=("updateTime",json_data["updateTime"]))
        self.tree.insert("" , "end",    text="Line 1", values=("logic",json_data["logic"]))
        self.tree.insert("" , "end",    text="Line 1", values=("action",json_data["action"]))
        
    def closeDialog(self):
        self.pop.destroy()
        self.pop.update()

    def okDialog(self):

        json_data = { "name" : self.name_input.get("1.0", 'end-1c'), 
                      "id" : self.id_input.get("1.0", 'end-1c'),
                      "inputDevice" : self.in_device_input.get("1.0", 'end-1c'),
                      "outputDevice" : self.out_device_input.get("1.0", 'end-1c'),
                      "updateTime" : "",
                      "logic" : self.logic_input.get("1.0", 'end-1c'),
                      "action" : self.action_input.get("1.0", 'end-1c')
                        }
        print("saving deviceOut json:")
        print(json_data)
        self.addJsonFunc( json_data )

        self.replaceDevicesListBox(self.logic.getJson())

        self.pop.destroy()
        self.pop.update()


    def removeLogicItem(self):      
        selection = self.logicListBox.selection()
        self.removeJsonFunc( self.logicListBox.index(selection) )
        self.logicListBox.delete( selection )
 
    def destroy(self):
        self.listbox.destroy()
        pass