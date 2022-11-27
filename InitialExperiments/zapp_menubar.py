import tkinter as tk

def donothing():
    x = 0


class zapp_menubar:
    def __init__(self, container):

        menubar = tk.Menu()
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open Full Tournament", command=container.open_tournament_file)
        filemenu.add_command(label="Open Custom Division", command=container.open_division_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=container.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About...", command=container.show_app_info)
        menubar.add_cascade(label="Help", menu=helpmenu)
        container.config(menu=menubar)
