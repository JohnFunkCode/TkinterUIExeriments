import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import tkinter.scrolledtext as scrolledtext
from pandastable import Table, TableModel

import temperature_converter

class zAppWindow(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # field options
        options = {'padx': 5, 'pady': 5}

        # temperature entry
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, **options)
        self.temperature_entry.focus()

        # convert button
        self.convert_button = ttk.Button(self, text='Convert')
        self.convert_button['command'] = self.convert
        self.convert_button.grid(column=2, row=0, sticky=tk.W, **options)

        # result label
        self.result_label = ttk.Label(self)
        self.result_label.grid(column=0, row=1, columnspan=3, **options)


        # activity label
        self.activity_log_label = ttk.Label(self, text='Activity Log')
        self.activity_log_label.grid(column=0, row=1, sticky=tk.W, **options)

        # activity log textbox
        self.activity_log = tk.scrolledtext.ScrolledText(self,width=200)
        self.activity_log.grid(column=0, row=2, columnspan=3, **options)

        # error log label
        self.error_log_label = ttk.Label(self, text='Error Log')
        self.error_log_label.grid(column=0, row=3, sticky=tk.W, **options)

        # error log textbox
        self.error_log = tk.scrolledtext.ScrolledText(self,width=200)
        self.error_log.grid(column=0, row=4, columnspan=3, **options)

        # button 1
        self.button_1 = ttk.Button(self, text='Button One')
        self.button_1['command'] = self.convert
        self.button_1.grid(column=3, row=2, sticky=tk.W, **options)

        # button 2
        self.button_2 = ttk.Button(self, text='Button Two')
        self.button_2['command'] = self.convert
        self.button_2.grid(column=3, row=4, sticky=tk.W, **options)

        self.pandas_table_frame = ttk.Frame(self,borderwidth=2,relief='sunken')
        self.table = Table(parent=self.pandas_table_frame, model=TableModel(container.database),
                                showtoolbar=False, showstatusbar=False, enable_menus=False,width=1550,height=200)
        self.pandas_table_frame.grid(column=0,row=5,columnspan=3,**options)
        self.table.redraw()

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def convert(self):
        """  Handle button click event
        """
        try:
            f = float(self.temperature.get())
            c = temperature_converter.TemperatureConverter.fahrenheit_to_celsius(f)
            result = f'{f} Fahrenheit = {c:.2f} Celsius'
            self.result_label.config(text=result)
            self.activity_log.configure(state=tk.NORMAL)
            self.activity_log.insert(tk.END,f'fahrenheit {f}, celcius {c}\n')
            self.activity_log.configure(state=tk.DISABLED)
        except ValueError as error:
            showerror(title='Error', message=error)
