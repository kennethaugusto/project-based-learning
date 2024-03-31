from tkinter import *
from PIL import Image, ImageTk
from algorithm import Player
import pandas as pd

# Assuming HomePage is correctly defined in homepage.py and uses pack for layout
from homepage import HomePage
from arraypage import ArrayPage

def load_players():
    filepath = "C:/Users/kenne/Documents/GitHub/project-based-learning/stats.csv"
    df = pd.read_csv(filepath)
    players = {}
    for index, row in df.iterrows():
        name = row['NAME']
        team = row['TEAM']
        pos = row['POS']
        age = row['AGE']
        gp = row['GP']
        mpg = row['MPG']
        usg = row['USG%']
        to = row['TO%']
        fta = row['FTA']
        ft = row['FT%']
        twopa = row['2PA']
        twop = row['2P%']
        threepa = row['3PA']
        threep = row['3P%']
        efgp = row['eFG%']
        tsp = row['TS%']
        ppg = row['PPG']
        rpg = row['RPG']
        apg = row['APG']
        spg = row['SPG']
        bpg = row['BPG']
        tpg = row['TPG']
        pplusr = row['P+R']
        pplusa = row['P+A']
        pplusrplusa = row['P+R+A']
        vi = row['VI']
        ortg = row['ORtg']
        drtg = row['DRtg']

    if name not in players:
        players[name] = Player(name, team, pos, age, gp, mpg, usg, to, fta, ft, twopa, twop, threepa, threep, efgp, tsp, ppg, rpg, apg, spg, bpg, tpg, pplusr, pplusa, pplusrplusa, vi, ortg, drtg)


class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.players = load_players()
        self.init_ui()

    def init_ui(self):
        self.master.geometry('500x500')
        self.min_w = 75  # Minimum width for the sidebar
        self.max_w = 350  # Maximum width for the sidebar
        self.cur_width = self.min_w  # Current width of the sidebar
        self.expanded = False  # Sidebar is not expanded initially


        # Define and resize icons
        self.array_icon = ImageTk.PhotoImage(Image.open('array.png').resize((40, 40), Image.LANCZOS))
        self.home_icon = ImageTk.PhotoImage(Image.open('home.png').resize((40, 40), Image.LANCZOS))

        # Sidebar frame
        self.frame = Frame(self.master, bg='orange', width=self.min_w, height=self.master.winfo_height())
        self.frame.pack(side='left', fill='y')

        # Buttons in the sidebar
        self.home_b = Button(self.frame, image=self.home_icon, bg='orange', relief='flat', command=lambda: self.show_frame(HomePage))
        self.home_b.pack(pady=10)

        # Inside the init_ui method, where you create the sidebar buttons
        self.array_b = Button(self.frame, image=self.array_icon, bg='orange', relief='flat', command=lambda: self.show_frame(ArrayPage))
        self.array_b.pack(pady=10)


        

        # Sidebar expand/contract on mouse hover
        self.frame.bind('<Enter>', self.expand)
        self.frame.bind('<Leave>', self.contract)
        self.frame.pack_propagate(False)

        self.frames = {}
        self.create_frames()

    def create_frames(self):
        # This is the container frame where other frames will be placed
        self.container = Frame(self.master)
        self.container.pack(side="right", fill="both", expand=True)
    
        for F in (HomePage, ArrayPage):
            if F == ArrayPage:
                frame = F(master=self.container, players=self.players)  # Pass players to ArrayPage
            else:
                frame = F(master=self.container)
            self.frames[F] = frame
            frame.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

        self.show_frame(HomePage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

    def expand(self, e=None):
        if not self.expanded:
            self.cur_width += 10
            rep = self.master.after(5, self.expand)
            self.frame.config(width=self.cur_width)
            if self.cur_width >= self.max_w:
                self.expanded = True
                self.master.after_cancel(rep)
                self.fill()

    def contract(self, e=None):
        if self.expanded:
            self.cur_width -= 10
            rep = self.master.after(5, self.contract)
            self.frame.config(width=self.cur_width)
            if self.cur_width <= self.min_w:
                self.expanded = False
                self.master.after_cancel(rep)
                self.fill()

    def fill(self):
        if self.expanded:
            self.home_b.config(text='Home', image='', font=(0, 12))
            self.array_b.config(text='Array', image='', font=(0, 12))
        else:
            self.home_b.config(image=self.home_icon,font=(0, 12))
            self.array_b.config(image=self.array_icon, font=(0, 12))

root = Tk()
app = App(master=root)
app.mainloop()