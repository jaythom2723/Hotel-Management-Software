import tkinter as tk
from tkinter import ttk
from tkinter import font as tkf
from tkinter.messagebox import showerror

from globals import setScreenDim
from frontend.components.navbar import Navbar

from frontend.pages.home import Home
from frontend.pages.logbook import TillCount

from frontend.pages.debug import Debug

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        global SCREEN_WIDTH, SCREEN_HEIGHT

        tk.Tk.__init__(self, *args, **kwargs)

        setScreenDim((self.winfo_screenwidth(), self.winfo_screenheight()))
        
        self.styles = {}
        self.styles["title_font"] = tkf.Font(family="Helvetica", size=18, weight="bold", slant="italic")
        self.styles["header_font"] = tkf.Font(family="Helvetica", size=12, weight="bold", slant="italic")
        self.styles["navbar_background_color"] = '#454545'

        self.sConfig = ttk.Style()
        self.sConfig.configure('Navbar.TFrame', background=f'{self.styles["navbar_background_color"]}')

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_columnconfigure(2, weight=1)
        
        navbar = Navbar(self.container, self)
        navbar.grid(row=1, column=1, sticky="nsw", ipadx=8, ipady=8)

        self.frames = {}
        for F in (Home, TillCount, Debug):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=1, column=2, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()