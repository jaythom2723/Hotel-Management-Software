import tkinter as tk
from tkinter import ttk
from tkinter import font as tkf

class Navbar(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent, style="Navbar.TFrame")
        self.controller = controller

        homeButton = ttk.Button(self, text="Home", command=lambda: self.changeWindow("Home"))
        bookingsButton = ttk.Button(self, text="Bookings", command=lambda: self.changeWindow("Bookings"))
        roomsButton = ttk.Button(self, text="Rooms", command=lambda: self.changeWindow("Rooms"))
        tabsButton = ttk.Button(self, text="Tabs", command=lambda: self.changeWindow("Tabs"))
        invoiceButton = ttk.Button(self, text="Invoice", command=lambda: self.changeWindow("Invoice"))
        creditCardBatch = ttk.Button(self, text="CC Batch", command=lambda: self.changeWindow("CCBatch"))
        tillCount = ttk.Button(self, text="Logbook", command=lambda: self.changeWindow("TillCount"))

        homeButton.pack()
        bookingsButton.pack()
        roomsButton.pack()
        tabsButton.pack()
        invoiceButton.pack()
        creditCardBatch.pack()
        tillCount.pack()

    def changeWindow(self, name):
        self.controller.show_frame(name)