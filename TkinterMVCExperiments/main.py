# MVC Approach adapted from the following articles
# OO aproach recommended in https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
# from https://www.pythontutorial.net/tkinter/tkinter-object-oriented-application/
# thinking in Tkinter https://thinkingtkinter.sourceforge.net/
# A very good MVC tutorial is at: https://www.pythontutorial.net/tkinter/tkinter-mvc/
# A well structured but not compleate example at https://medium.com/swlh/python-oop-mvc-data-science-tkinter-23c3e8dab70f

import zapp_controller

if __name__ == "__main__":
    app = zapp_controller.zAppController()
    app.mainloop()
