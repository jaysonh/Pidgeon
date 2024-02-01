from Scheduler import Scheduler
import tkinter as tk
from tkinter import ttk
from tkinter import *
import json
from Logging import *
from Event import *
import threading
import time
from MQTTHandler import *
from Logging import *
from LoggingTextHandler import *

class GuiDisplayLog:
    deviceID = ""
    
    def __init__(self, root : tk ):
        self.start_time = time.time()

        self.parent = root
        
        self.text_widget = tk.Text(root)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        vsb = ttk.Scrollbar(self.text_widget, orient="vertical", command=self.text_widget.yview)
        vsb.pack(side='right', fill='y')
        self.text_widget.configure(yscrollcommand=vsb.set)

        handler = LoggingTextHandler(self.text_widget)
        handler.setLevel(logging.DEBUG)  # Set the desired log level
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger = logging.getLogger()  # Get the root logger
        logger.addHandler(handler)

        self.bottomframe = Frame(root)
        self.bottomframe.pack( side = BOTTOM )

        self.addButton = Button(self.bottomframe, text ="clear", command = self.clearDisplayLog)
        self.addButton.pack(side="right", fill="none", expand=False)



    def clearDisplayLog(self):
        
        self.text_widget.delete('1.0', tk.END) # delete all lines

        
  