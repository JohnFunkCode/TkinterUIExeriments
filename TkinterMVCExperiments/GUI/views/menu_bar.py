import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

def donothing():
    x = 0


class MenuBar:
    def __init__(self, app_container):
        self.app_container = app_container
        menubar = tk.Menu()
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open Full Tournament", command=self.open_tournament_file)
        filemenu.add_command(label="Open Custom Division", command=self.open_division_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=app_container.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About...", command=self.show_app_info)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # placeholder for testing
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Test One", command=self.test_one)
        helpmenu.add_command(label="Test Two", command=self.test_two)

        menubar.add_cascade(label="Test", menu=helpmenu)


        app_container.config(menu=menubar)

    def open_tournament_file(self):
        filename = filedialog.askopenfilename(title="Select the file with the tournament data",filetypes=[("csv","*.csv")])
        self.app_container.database = pd.read_csv(filename)
        self.app_container.data_load_view.update_table()
        self.app_container.data_load_view.table.show()
        self.app_container.data_load_view.show_it()
        self.app_container.opening_view.hide_it()

    def open_division_file(self):
        filename = filedialog.askopenfilename(title="Select the file with the division data",filetypes=[("csv","*.csv"),("excel","*.xls")])
        self.app_container.database = pd.read_csv(filename)
        self.app_container.data_load_view.update_table()
        self.data_load_view.table.show()
        self.data_load_view.show_it()
        self.opening_view.hide_it()

    def show_app_info(self):
        messagebox.showinfo("About", "Version beta 1\nLast updated 11/5/2022", parent=self.z_window)

    def test_one(self):
        self.app_container.data_load_view.highlight_age_error(11)
        self.app_container.data_load_view.highlight_age_error(22)
        self.app_container.data_load_view.highlight_age_error(33)

    def test_two(self):
        self.app_container.data_load_view.goto_row_column(11,'Age')