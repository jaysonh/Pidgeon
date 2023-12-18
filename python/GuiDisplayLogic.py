from Scheduler import Scheduler
import tkinter as tk
from tkinter import ttk
from tkinter import *
import json

class GuiDisplayLogic:
    def __init__(self, root : tk , json_data : json) -> None:
        self.listbox = ttk.Treeview(root, columns=("Column1"))
        #eframe = ttk.Frame(root)
        #eframe.pack(side="bottom", fill="x")
        self.listbox.pack(side="top", fill="both", expand=True)

        print("displaying logic json: " + json.dumps(json_data))
        self.listbox.insert("", "end", text=f"name",  values=(json_data["name"] ))
        self.listbox.insert("", "end", text=f"id"  ,  values=(json_data["id"] ))
        self.listbox.insert("", "end", text=f"inputDevice" ,  values=(json_data["inputDevice"] ))
        self.listbox.insert("", "end", text=f"outputDevice" ,  values=(json_data["outputDevice"] ))
        self.listbox.insert("", "end", text=f"updateTime" ,  values=(json_data["updateTime"] ))
        self.listbox.insert("", "end", text=f"logic",  values=(json_data["logic"] ))
        self.listbox.insert("", "end", text=f"action" ,  values=(json_data["action"] ))
           
        # convert json to string
           
        pass

    def destroy(self):
        self.listbox.destroy()
        pass