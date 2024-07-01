from tkinter import ttk

class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.placeholder = placeholder
        self.insert("0", placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._place_placeholder)
    
    def _place_placeholder(self, e):
        if self.get() != "":
            return

        self.insert("0", self.placeholder)

    def _clear_placeholder(self, e):
        self.delete("0", "end")