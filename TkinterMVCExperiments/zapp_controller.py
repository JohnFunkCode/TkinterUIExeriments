import tkinter as tk
import TkinterMVCExperiments.GUI.datavalidation.data_validation_controller as data_validation_controller

import TkinterMVCExperiments.GUI.menubar.menu_bar
from TkinterMVCExperiments.GUI.splashscreen.splash_screen import SpashScreen
import pandas as pd


class zAppController(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('zUltimate App')
        # self.geometry('1920x1080')
        self.geometry('1721x972')
        self.resizable(True, True)
        self.iconbitmap("zultimate-logo_103x130-1.ico")
        self.config(bg="Grey")  # self.config(bg="Light Grey")

        self.database = pd.DataFrame()
        self.menu_bar = TkinterMVCExperiments.GUI.menubar.menu_bar.MenuBar(self)
        self.data_validation_controller=data_validation_controller.DataValidationController(self)
        self.splash_screen = SpashScreen(self)
        self.splash_screen.grid(sticky=tk.NSEW)

        self.data_validation_controller.hide_view()
        self.splash_screen.show_view()



