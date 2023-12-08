
from tkinter import *
from tkinter import ttk
import tkinter as tk
import json


class GUIDisplayDeviceOut:

    def __init__(self, root : Tk, json_data : json ):

        self.listbox = ttk.Treeview(root, columns=("Column1"))
        self.listbox.pack(side="top", fill="both", expand=True)

        self.listbox.insert("", "end", text=f"Name:", values=(json_data["name"] ))
        self.listbox.insert("", "end", text=f"ID: ", values=(json_data["id"],  ))
        self.listbox.insert("", "end", text=f"Type: ", values=(json_data["type"] ))
        self.listbox.insert("", "end", text=f"Num Channels: ", values=(json_data["numChannels"] ))

        pass

    def destroy(self):
        self.listbox.destroy()
        pass
        