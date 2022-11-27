from tkinter import *
from pandastable import Table, TableModel
import pandas as pd
from tkinter import filedialog
from tkinter import ttk


class TestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('600x400+200+100')
            self.main.title('Table app')
            filename = filedialog.askopenfilename()
            self.df = pd.read_csv(filename)
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            self.table = pt = Table(f, dataframe=self.df,
                                    showtoolbar=False, showstatusbar=False, enable_menus=False)
            self.table.editable = False
            pt.show()
            # # button 2
            # self.button_2 = ttk.Button(self, text='Button Two')
            # self.button_2['command'] = self.donothing()
            # self.button_2.grid(column=0, row=4, columnspan=3)

            return

        def donothing(self):
            x=1

app = TestApp()
#launch the app
app.mainloop()