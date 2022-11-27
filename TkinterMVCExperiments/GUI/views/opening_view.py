import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from pandastable import Table, TableModel


class OpeningView(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # field options
        options = {'padx': 5, 'pady': 5}
        # self.grid(**options,sticky=tk.NSEW)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=3)
        # self.grid_rowconfigure(2, weight=1)
        # self.grid_rowconfigure(3, weight=1)
        # self.grid_rowconfigure(4, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)
        # self.grid_columnconfigure(3, weight=1)
        # self.grid_columnconfigure(4, weight=1)


        # data table label
        self.opening_label0 = ttk.Label(self, text='zUltimate Tournament App',font="Helventica 22 bold")
        self.opening_label0.grid(column=0, row=0,**options)

       #  # data table label
       #  self.opening_label1 = ttk.Label(self, text='zUltimate Tournament App',font="Helventica 22 bold")
       #  self.opening_label1.grid(column=1, row=1,**options)
       #
       #  # data table label
       #  self.opening_label2 = ttk.Label(self, text='zUltimate Tournament App', font="Helventica 22 bold")
       #  self.opening_label2.grid(column=2, row=2, **options)
       #
       #  # data table label
       #  self.opening_label3 = ttk.Label(self, text='zUltimate Tournament App', font="Helventica 22 bold")
       #  self.opening_label3.grid(column=3, row=3, **options)
       #
       #  # data table label
       #  self.opening_label4 = ttk.Label(self, text='zUltimate Tournament App', font="Helventica 22 bold")
       #  self.opening_label4.grid(column=4, row=4, **options)
       #
       # # data table label
       #  self.opening_label5 = ttk.Label(self, text='zUltimate Tournament App', font="Helventica 22 bold")
       #  self.opening_label5.grid(column=5, row=5, **options)

    def show_it(self):
        self.grid()

    def hide_it(self):
        self.grid_forget()


