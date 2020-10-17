from ctypes import windll
import tkinter as tk
import csv
import os
from win32printing import Printer

font = {
    "height": 16,
}

windll.shcore.SetProcessDpiAwareness(1)

def filename():
    if not 'Box1.csv' in os.listdir():
        return 'Box1.csv'
    else:
        boxlist1 = []
        for x in os.listdir():
            if 'Box' in x:
                boxlist1.append(x)
        boxlist2 = []
        for y in boxlist1:
            boxlist2.append(y[:-4])
        boxlist3 = []
        for z in boxlist2:
            boxlist3.append(int(z[3:]))
        boxnum = max(boxlist3)+1
        return "Box" + str(boxnum) + ".csv"

def contains_print(foo):
    contents = T.get('1.0', 'end').splitlines()
    if "print" in contents:
        T.delete('1.0', tk.END)
        data = uniq(contents)
        print(data)
        with open(filename(), 'x') as f:
            [f.write('{0},{1}\n'.format(key, value)) for key, value in data.items()]
        with Printer(linegap=2, margin=(10,10,10,10)) as printer:
            printer.text(filename(), font_config={"height":24})
            for x,y in data.items():
                printer.text("UPC: {}  Qty: {}".format(x, y), font_config=font)

def uniq(inputlist):
    data = {}
    for x in inputlist:
        if x == "print":
            pass
        else:
            if x in data:
                data[x] += 1
            else:
                data[x] = 1
    return data

root = tk.Tk()
T = tk.Text(root, height=10, width=30)
T.pack()
T.bind("<Return>", contains_print)
tk.mainloop()
