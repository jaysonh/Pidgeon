
from tkinter import *
from tkinter import ttk
import tkinter as tk
import json

class GUIDisplayDeviceIn:

    def __init__( self, root : Tk, json_data : json ):

        self.parent = root
        self.listbox = ttk.Treeview(root, columns=("Column1"))
        #eframe = ttk.Frame(root)
        #eframe.pack(side="bottom", fill="x")
        self.listbox.pack(side="top", fill="both", expand=True)

        self.listbox.insert("", "end", text=f"Name:", values=(json_data["name"] ))
        self.listbox.insert("", "end", text=f"ID: ", values=(json_data["id"],  ))
        self.listbox.insert("", "end", text=f"Type: ", values=(json_data["type"] ))
    
        self.bottomframe = Frame(root)
        self.bottomframe.pack( side = BOTTOM )

        self.addButton = Button(self.bottomframe, text ="add", command = self.openAddDeviceInDialog)
        self.addButton.pack(side="right", fill="none", expand=False)
        
        self.removeButton = Button(self.bottomframe, text ="remove", command = self.removeDeviceInItem)
        self.removeButton.pack(side="left", fill="none", expand=False)

        pass

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
        name_input = tk.Text(frame_name_input, 
                   height = 1, 
                   width = 20)
        name_input.grid(row=0, column=2)
        
        # device id input
        frame_id_input = Frame(self.pop, bg="gray71")
        frame_id_input.pack(pady=2)
        id_label = tk.Label( frame_id_input, text="id")
        id_label.grid(row=0, column=1)
        id_input = tk.Text(frame_id_input, 
                   height = 1, 
                   width = 20)
        id_input.grid(row=0, column=2)

        
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
        pass

    def destroy(self):
        self.listbox.destroy()
        pass

    def closeDialog(self):
        self.pop.destroy()
        self.pop.update()

    def okDialog(self):
        #print("close dialog: " + self.cron_day_week_var.get())
        #cron_str = self.cron_day_week_var .get() + " " + self.cron_month_var.get() + " " + self.cron_day_var.get() + " " + self.cron_hour_var.get() + " " + self.cron_minute_var.get() + " " + self.cron_second_var.get()
        self.pop.destroy()
        self.pop.update()