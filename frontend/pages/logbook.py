import tkinter as tk
from tkinter import ttk
from tkinter import font as tkf
from tkinter.messagebox import showerror
import datetime
import time

from backend.sqlapi import sendLogbookEntry, getLogbookEntriesByDate
from ctypes import LogbookEntryMessage
from frontend.components.phentry import PlaceholderEntry
from frontend.components.lbentry import LogbookEntry

placeholders = ["Pennies", "Nickels", "Dimes", "Quarters", "Dollars", "Fives", "Tens", "Twenties", "Fifties", "Hundreds", "Receipts"]
values = {}
values["pennies"]       = 0.01
values["nickels"]       = 0.05
values["dimes"]         = 0.10
values["quarters"]      = 0.25
values["dollars"]       = 1
values["fives"]         = 5
values["tens"]          = 10
values["twenties"]      = 20
values["fifties"]       = 50
values["hundreds"]      = 100
values["receipts"]      = 1

class TillCount(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        title = ttk.Label(self, text="Logbook", font=self.controller.styles["title_font"])
        title.pack()

        self.container = ttk.Frame(self)

        headerOne = ttk.Label(self.container, text="Money", anchor="w", font=self.controller.styles["header_font"])
        headerOne.grid(row=1, column=1)

        dateLabel = ttk.Label(self.container)
        dateLabel.configure(text=f"{datetime.datetime.now().strftime("%m/%d/%Y")}")
        dateLabel.grid(row=1, column=2)

        self.totalLabel = ttk.Label(self.container)
        self.totalLabel.configure(text="Total: $0.0")

        self.stringVars = {}
        self.stringVars["pennies"] = tk.StringVar()
        self.stringVars["nickels"] = tk.StringVar()
        self.stringVars["dimes"] = tk.StringVar()
        self.stringVars["quarters"] = tk.StringVar()
        self.stringVars["dollars"] = tk.StringVar()
        self.stringVars["fives"] = tk.StringVar()
        self.stringVars["tens"] = tk.StringVar()
        self.stringVars["twenties"] = tk.StringVar()
        self.stringVars["fifties"] = tk.StringVar()
        self.stringVars["hundreds"] = tk.StringVar()
        self.stringVars["receipts"] = tk.StringVar()

        self.confirmationCode = tk.StringVar()

        for key in self.stringVars:
            self.stringVars[key].trace("w", lambda name, index, mode, sv=self.stringVars[key]: self.getTotalValue())
        
        entries = {}
        entries["pennies_entry"]       = PlaceholderEntry(self.container, placeholders[0], textvariable=self.stringVars["pennies"])
        entries["nickels_entry"]       = PlaceholderEntry(self.container, placeholders[1], textvariable=self.stringVars["nickels"])
        entries["dimes_entry"]         = PlaceholderEntry(self.container, placeholders[2], textvariable=self.stringVars["dimes"])
        entries["quarters_entry"]      = PlaceholderEntry(self.container, placeholders[3], textvariable=self.stringVars["quarters"])
        entries["dollars_entry"]       = PlaceholderEntry(self.container, placeholders[4], textvariable=self.stringVars["dollars"])
        entries["fives_entry"]         = PlaceholderEntry(self.container, placeholders[5], textvariable=self.stringVars["fives"])
        entries["tens_entry"]          = PlaceholderEntry(self.container, placeholders[6], textvariable=self.stringVars["tens"])
        entries["twenties_entry"]      = PlaceholderEntry(self.container, placeholders[7], textvariable=self.stringVars["twenties"])
        entries["fifties_entry"]       = PlaceholderEntry(self.container, placeholders[8], textvariable=self.stringVars["fifties"])
        entries["hundreds_entry"]      = PlaceholderEntry(self.container, placeholders[9], textvariable=self.stringVars["hundreds"])
        entries["receipts_entry"]      = PlaceholderEntry(self.container, placeholders[10], textvariable=self.stringVars["receipts"])

        entries["pennies_entry"].grid(row=2, column=1, padx=8)
        entries["nickels_entry"].grid(row=2, column=2, padx=8)
        entries["dimes_entry"].grid(row=2, column=3, padx=8)
        entries["quarters_entry"].grid(row=2, column=4, padx=8)

        entries["dollars_entry"].grid(row=3, column=1, pady=8)
        entries["fives_entry"].grid(row=3, column=2, pady=8)
        entries["tens_entry"].grid(row=3, column=3, pady=8)
        entries["twenties_entry"].grid(row=3, column=4, pady=8)

        entries["fifties_entry"].grid(row=4, column=1)
        entries["hundreds_entry"].grid(row=4, column=2)
        entries["receipts_entry"].grid(row=4, column=3)

        confirmCodeEntry = PlaceholderEntry(self.container, "Confirmation Code", textvariable=self.confirmationCode)

        saveButton = ttk.Button(self.container, text="Save", command=lambda: self.saveTillCount(confirmCodeEntry.get()))

        saveButton.grid(row=5, column=2, pady=8)
        confirmCodeEntry.grid(row=5, column=1, pady=8)

        self.totalLabel.grid(row=6, column=4)

        # TODO: Implement a way to see today's logbook entries

        self.scroll_container = ttk.Frame(self)
        self.scroll_bar = ttk.Scrollbar(self.scroll_container, orient='vertical')

        self.updateRecentEntries()

        self.container.pack(side="top", pady=8, ipadx=8)
        self.scroll_container.pack(pady=8, ipadx=8)

    def updateRecentEntries(self):
        date = datetime.datetime.now().strftime("%m/%d/%Y")
        entryMessages = getLogbookEntriesByDate(date)

        for message in entryMessages:
            entry = LogbookEntry(
                self.scroll_container, 
                self.controller,
                message.date,
                message.code,
                message.total
                )
            entry.pack()

    def getTotalValue(self):
        try:
            ret: float = 0.0
            
            for key in self.stringVars:
                if self.stringVars[key].get() in placeholders or self.stringVars[key].get() == "":
                    continue

                for moneyValue in values:
                    if key == moneyValue:
                        ret += values[moneyValue] * float(self.stringVars[key].get())

            self.totalLabel.configure(text=f"Total: ${ret:.2f}")

            return ret
        except ValueError:
            showerror("UH OH!", "You've input an invalid number!")
        

    def saveTillCount(self, confirmcode: str):
        cur_date = datetime.datetime.now().strftime("%m/%d/%Y")

        entry: LogbookEntryMessage = LogbookEntryMessage(cur_date, confirmcode.replace(' ','_'), self.getTotalValue())
        sendLogbookEntry(entry)
        time.sleep(0.25)