import tkinter as tk
import TkinterMVCExperiments.GUI.views.data_load_view
import TkinterMVCExperiments.GUI.views.menu_bar
from TkinterMVCExperiments.GUI.views.opening_view import OpeningView
import pandas as pd
from pandastable import TableModel


class zAppController(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('zUltimate App')
        # self.geometry('1920x1080')
        self.geometry('1721x972')
        self.resizable(True, True)
        # self.attributes("-alpha",0.5)   #make the window 50% transperant

        self.iconbitmap("zultimate-logo_103x130-1.ico")
        self.config(bg="Grey")
        # self.config(bg="Light Grey")

        self.database = pd.DataFrame()
        self.menu_bar = TkinterMVCExperiments.GUI.views.menu_bar.MenuBar(self)
        self.data_load_view = TkinterMVCExperiments.GUI.views.data_load_view.DataLoadView(self)
        self.data_load_view.grid(sticky=tk.NSEW)
        self.opening_view = OpeningView(self)
        self.opening_view.grid(sticky=tk.NSEW)

        self.data_load_view.hide_it()
        self.opening_view.show_it()



