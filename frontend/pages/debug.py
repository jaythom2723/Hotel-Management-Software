import tkinter as tk
from tkinter import ttk
from tkinter import font as tkf

class Debug(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller