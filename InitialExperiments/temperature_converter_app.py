import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Temperature Converter')
        self.geometry('2000x600')
        self.resizable(False, False)

