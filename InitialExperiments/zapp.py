import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import zapp_window
import zapp_menubar
import pandas as pd
from pandastable import TableModel

class zApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('zUltimate App')
        self.geometry('2000x1950')
        self.resizable(False, False)
        # self.attributes("-alpha",0.5)   #make the window 50% transperant
        self.iconbitmap("zultimate-logo_103x130-1.ico")

        self.database = pd.DataFrame()
        self.z_menu = zapp_menubar.zapp_menubar(self)
        self.z_window = zapp_window.zAppWindow(self)

    def open_tournament_file(self):
        print("open tournament file")
        filename = filedialog.askopenfilename()
        self.z_window.activity_log.configure(state=tk.NORMAL)
        self.z_window.activity_log.insert(tk.END,f'tournament filename = {filename}\n')
        self.database = pd.read_csv(filename)
        self.z_window.activity_log.insert(tk.END, self.database.to_string(index=False, max_cols=9))
        self.z_window.activity_log.configure(state=tk.DISABLED)
        self.z_window.table.updateModel(TableModel(self.database))
        self.z_window.table.show()

        # root.update()  # Prevent the askfilename() window doesn't stay open

    def open_division_file(self):
        print("open division file")
        filename = filedialog.askopenfilename()
        self.z_window.activity_log.configure(state=tk.NORMAL)
        self.z_window.activity_log.insert(tk.END,f'division filename = {filename}\n')
        self.z_window.activity_log.configure(state=tk.DISABLED)
        self.z_window.table.show()

    def show_app_info(self):
        messagebox.showinfo("About","Version beta 1\nLast updated 11/5/2022",parent=self.z_window)