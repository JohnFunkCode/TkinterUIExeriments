# from https://www.pythontutorial.net/tkinter/tkinter-object-oriented-application/

import pandas as pd

import zapp

if __name__ == "__main__":
    columns = ['index', 'First Name', 'Last Name', 'Gender', 'Dojo', 'Age', 'Rank', 'Feet', 'Inches', 'Height',
               'Weight', 'BMI', 'Events', 'Weapons']
    data = [(255, 'Lucas', 'May', 'Male', 'CO- Parker', 10, 'Yellow', 4, 3, '4 ft. 3 in.', 52, 154,
             '2 Events - Forms & Sparring ($75)', 'None'),
            (194, 'jake', 'coleson', 'Male', 'CO- Cheyenne Mountain', 10, 'Yellow', 4, 0, '4', 60, 156,
             '2 Events - Forms & Sparring ($75)', 'Weapons ($35)'),
            (195, 'katie', 'coleson', 'Female', 'CO- Cheyenne Mountain', 12, 'Yellow', 4, 0, '4', 65.161,
             '2 Events - Forms & Sparring ($75)', 'Weapons ($35)')]
    # df = pd.DataFrame(data, columns=columns)
    # print(df.to_string(index=False,max_cols=df.shape[1]))

    app = zapp.zApp()
    app.database = pd.DataFrame(data, columns=columns)
    app.mainloop()


# use the OO aproach recommended in https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
# also thinking in Tkinter https://thinkingtkinter.sourceforge.net/
# a good MVC tutorial is at: https://www.pythontutorial.net/tkinter/tkinter-mvc/
# and one at https://medium.com/swlh/python-oop-mvc-data-science-tkinter-23c3e8dab70f