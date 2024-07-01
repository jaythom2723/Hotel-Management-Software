import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter import font as tkf

class Home(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        title = ttk.Label(self, text="Home", font=self.controller.styles["title_font"])
        title.pack()