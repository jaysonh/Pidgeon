from Scheduler import Scheduler
import tkinter as tk
from tkinter import ttk
import json

class GuiScheduleDisplay:
    deviceID = ""
    
    def __init__(self, root : tk , json_data : json ):

        self.listbox = ttk.Treeview(root, columns=("Column1", "Column2", "Column3", "Column4", "Column5"))
        self.listbox.pack(side="top", fill="both", expand=True)

        #self.listbox.insert("", "end", text=f"Name:", values=(json_data["name"] ))
        #self.listbox.insert("", "end", text=f"ID: ", values=(json_data["id"],  ))
        #self.listbox.insert("", "end", text=f"Type: ", values=(json_data["type"] ))
        #self.listbox.insert("", "end", text=f"Num Channels: ", values=(json_data["numChannels"] ))


        for job in json_data:
            self.listbox.insert("", "end", text=job["id"], values=( job["time"], job["deviceID"], job["address"], "next run:", job["action"] ))
            print(job)
        pass
        #self.schedule = schedule

