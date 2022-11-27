# from https://www.pythontutorial.net/tkinter/tkinter-object-oriented-application/

import pandas as pd

import zapp_controller

if __name__ == "__main__":
    app = zapp_controller.zAppController()
    app.mainloop()


# use the OO aproach recommended in https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
# also thinking in Tkinter https://thinkingtkinter.sourceforge.net/
# a good MVC tutorial is at: https://www.pythontutorial.net/tkinter/tkinter-mvc/
# and one at https://medium.com/swlh/python-oop-mvc-data-science-tkinter-23c3e8dab70f