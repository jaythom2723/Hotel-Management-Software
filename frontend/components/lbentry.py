import tkinter as tk
from tkinter import ttk
from tkinter import font as tkf
from tkinter.messagebox import showerror

class LogbookEntry(ttk.Frame):
    def __init__(self, parent, controller, date: str, code: str, total: float):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.dateLabel = ttk.Label(self, text=f"Date: {date}")
        self.totalLabel = ttk.Label(self, text=f"Total: ${total:.2f}")
        self.confirmationLabel = ttk.Label(self, text=f"Code: {code}")

        self.dateLabel.pack()
        self.confirmationLabel.pack()
        self.totalLabel.pack()