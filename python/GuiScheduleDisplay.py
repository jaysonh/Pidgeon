from Scheduler import Scheduler
import tkinter as tk
from tkinter import ttk
from tkinter import *
import json

class GuiScheduleDisplay:
    deviceID = ""
    
    def __init__(self, root : tk , json_data : json ):

        self.parent = root
        self.listbox = ttk.Treeview(root, columns=("Column1", "Column2", "Column3", "Column4", "Column5"))
        self.listbox.pack(side="top", fill="both", expand=True)

        #self.listbox.insert("", "end", text=f"Name:", values=(json_data["name"] ))
        #self.listbox.insert("", "end", text=f"ID: ", values=(json_data["id"],  ))
        #self.listbox.insert("", "end", text=f"Type: ", values=(json_data["type"] ))
        #self.listbox.insert("", "end", text=f"Num Channels: ", values=(json_data["numChannels"] ))

        for job in json_data:
            self.listbox.insert("", "end", text=job["id"], values=( job["time"], job["deviceID"], job["address"], "next run:", job["action"] ))
            print(job)

                
        self.bottomframe = Frame(root)
        self.bottomframe.pack( side = BOTTOM )

        self.addButton = Button(self.bottomframe, text ="add", command = self.openAddScheduleDialog)
        self.addButton.pack(side="right", fill="none", expand=False)

        
        self.removeButton = Button(self.bottomframe, text ="remove", command = self.removeScheduleItem)
        self.removeButton.pack(side="left", fill="none", expand=False)

        pass
        #self.schedule = schedule


    def closeDialog(self):
        self.pop.destroy()
        self.pop.update()

    def okDialog(self):

        #print("close dialog: " + self.cron_day_week_var.get())
        cron_str = self.cron_day_week_var .get() + " " + self.cron_month_var.get() + " " + self.cron_day_var.get() + " " + self.cron_hour_var.get() + " " + self.cron_minute_var.get() + " " + self.cron_second_var.get()
        self.add_schedule( cron_str )
        self.pop.destroy()
        self.pop.update()

    def add_schedule( self, cron_str ):

        print("adding schedule: " + cron_str)
        pass

    def openAddScheduleDialog(self):
        #global pop
        self.pop = Toplevel(self.parent)
        self.pop.title("Add Schedule Item")
        self.pop.geometry("450x250")
        self.pop.config(bg="white")
        
        # schedule id input
        frame_id_input = Frame(self.pop, bg="gray71")
        frame_id_input.pack(pady=2)
        id_label = tk.Label( frame_id_input, text="id")
        id_label.grid(row=0, column=1)
        id_input = tk.Text(frame_id_input, 
                   height = 1, 
                   width = 20) 
        id_input.grid(row=0, column=2)
        
        # cron schedule input
        frame_cron_input = Frame(self.pop, bg="gray71")
        frame_cron_input.pack(pady=2)
        cron_label = tk.Label( frame_cron_input, text="schedule time")
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


        # device id input
        frame_device_id_input = Frame(self.pop, bg="gray71")
        frame_device_id_input.pack(pady=2)
        device_id_label = tk.Label( frame_device_id_input, text="device id")
        device_id_label.grid(row=0, column=1)
        device_id_input = tk.Text(frame_device_id_input, 
                   height = 1, 
                   width = 20) 
        device_id_input.grid(row=0, column=2)

        # address input
        frame_address_input = Frame(self.pop, bg="gray71")
        frame_address_input.pack(pady=2)
        address_label = tk.Label( frame_address_input, text="address")
        address_label.grid(row=0, column=1)
        address_input = tk.Text(frame_address_input, 
                   height = 1, 
                   width = 20) 
        address_input.grid(row=0, column=2)

        # action input
        frame_action_input = Frame(self.pop, bg="gray71")
        frame_action_input.pack(pady=2)
        action_label = tk.Label( frame_action_input, text="action")
        action_label.grid(row=0, column=1)
        action_input = tk.Text(frame_action_input, 
                   height = 5, 
                   width = 20) 
        action_input.grid(row=0, column=2)

        # Add a Frame
        frameBtns = Frame(self.pop, bg="gray71")
        frameBtns.pack(pady=10)
        # Add Button for making selection
        button1 = Button(frameBtns, text="add", command=self.okDialog, bg="blue", fg="white")
        button1.grid(row=0, column=1)
        button2 = Button(frameBtns, text="cancel", command= self.closeDialog, bg="blue", fg="white")
        button2.grid(row=0, column=2)
        pass

    def removeScheduleItem(self):
        selected = self.listbox.selection()
        current_idx = self.listbox.index(selected)
        print("remove: " + str(current_idx))

        self.listbox.delete(selected)

        pass

