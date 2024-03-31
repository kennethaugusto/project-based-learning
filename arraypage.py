from algorithm import Player
import pandas as pd

from tkinter import Frame, Label, Scrollbar, Listbox, VERTICAL, END
# If ArrayPage is in a separate file, you might need to import the Player class or the data structure holding the players

class ArrayPage(Frame):
    def __init__(self, master=None, players=None):
        super().__init__(master)
        self.players = players
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Player information display (assuming `players` is a dictionary of Player instances)
        self.player_listbox = Listbox(self)
        self.player_listbox.pack(fill="both", expand=True)

        scrollbar = Scrollbar(self.player_listbox, orient=VERTICAL)
        scrollbar.pack(side='right', fill='y')

        self.player_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.player_listbox.yview)

        # Populate the listbox with player data
        if self.players:  # Check if players data is not None or empty
            for player_name, player_instance in self.players.items():
                self.player_listbox.insert(END, f"{player_name}: {str(player_instance)}")
                # Assuming your Player class has a __str__ method that formats its attributes nicely

