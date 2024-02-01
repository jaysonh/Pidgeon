import tkinter as tk
import logging

class LoggingTextHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
        self.max_lines = 200

    def emit(self, record):
        try:
            log_entry = self.format(record)
            self.text_widget.insert(tk.END, log_entry + '\n')
            self.text_widget.see(tk.END)

            num_lines = float(self.text_widget.index('end-1c').split('.')[0])
            while num_lines > self.max_lines:
                self.text_widget.delete('1.0', '2.0') # delete first line
                num_lines = float(self.text_widget.index('end-1c').split('.')[0])
        except:
            #otherwise logger already ended
            pass
