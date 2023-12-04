
from tkinter import *
from tkinter import ttk
import tkinter as tk
import json

class GUIDisplaySensor:

    def __init__(self, root : Tk, json_data : json ):

        #f = ttk.Frame(root)
        #f['padding'] = (5,5,100,5)

        labelName = Label( root, text=str("Name: " + json_data["name"]), relief=RAISED )
        labelID   = Label( root, text=str("ID:   " + json_data["id"]),   relief=RAISED )
        labelType = Label( root, text=str("Type: " + json_data["id"]),   relief=RAISED )
        labelName.pack()
        labelID.pack()
        labelType.pack()

        pass