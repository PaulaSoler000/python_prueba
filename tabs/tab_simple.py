import tkinter as tk
from tkinter import ttk

class Table1:
    def __init__(self, parent):
        self.parent = parent
        self.table = ttk.Label(self.parent, text="Table 1")
        self.table.grid(column=0, row=1, padx=30, pady=30)

class Table2:
    def __init__(self, parent):
        self.parent = parent
        self.table = ttk.Label(self.parent, text="Table 2")
        self.table.grid(column=0, row=1, padx=30, pady=30)

root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")

table1 = Table1(tab1)
table2 = Table2(tab2)

root.mainloop()