import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import tkinter.scrolledtext as scrolledtext

import temperature_converter

class ConverterFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # field options
        options = {'padx': 5, 'pady': 5}

        # temperature label
        self.temperature_label = ttk.Label(self, text='Fahrenheit')
        self.temperature_label.grid(column=0, row=0, sticky=tk.W, **options)

        # temperature entry
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, **options)
        self.temperature_entry.focus()


        self.convert_button = ttk.Button(self, text='Convert')
        self.convert_button['command'] = self.convert
        self.convert_button.grid(column=2, row=0, sticky=tk.W, **options)

        # dataframe textbox
        self.dftext = tk.scrolledtext.ScrolledText(self,width=200)
        self.dftext.grid(column=0, row=2, columnspan=3, **options)
#        self.dftext.insert(tk.END, df.to_string(index=False,max_cols=df.shape[1]))
#        self.dftext.configure(state=tk.DISABLED)

        # result label
        self.result_label = ttk.Label(self)
        self.result_label.grid(row=3, columnspan=3, **options)

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
            self.dftext.configure(state=tk.NORMAL)
            self.dftext.insert(tk.END,f'fahrenheit {f}, celcius {c}\n')
            self.dftext.configure(state=tk.DISABLED)
        except ValueError as error:
            showerror(title='Error', message=error)
