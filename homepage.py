# homepage.py
from tkinter import Frame, Label

class HomePage(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='white')
        self.master = master
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.home_label = Label(self, text="WSmd!", bg='white')
        self.home_label.pack(pady=20)
