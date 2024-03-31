from tkinter import *
from PIL import Image, ImageTk
# Assuming HomePage is correctly defined in homepage.py and uses pack for layout
from homepage import HomePage
from arraypage import ArrayPage

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_ui()

        # Toggle state for Array operation
        self.array_operation_running = False  # Initially not running

    def init_ui(self):
        self.master.geometry('1366x768')
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

        self.array_b = Button(self.frame, image=self.array_icon, bg='orange', relief='flat', command=self.toggle_array_operation)
        self.array_b.pack(pady=10)

        self.frame.bind('<Enter>', self.expand)
        self.frame.bind('<Leave>', self.contract)
        self.frame.pack_propagate(False)

        self.frames = {}
        self.create_frames()

    def create_frames(self):
        self.container = Frame(self.master)
        self.container.pack(side="right", fill="both", expand=True)

        for F in (HomePage, ArrayPage):
            frame = F(self.container)
            self.frames[F] = frame
            frame.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.show_frame(HomePage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

    def toggle_array_operation(self):
        # Toggle the state
        self.array_operation_running = not self.array_operation_running

        if self.array_operation_running:
            # Start or continue the operation
            print("Array operation started")  # Placeholder for actual operation
            self.array_b.config(relief='sunken')  # Optional: visually indicate the button is active
        else:
            # Stop the operation
            print("Array operation stopped")  # Placeholder for stopping the operation
            self.array_b.config(relief='raised')  # Optional: reset the button's visual state

    # Existing expand and contract methods...

# Run the app
root = Tk()
app = App(master=root)
app.mainloop()
