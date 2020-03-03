from tkinter import *

F = Frame(borderwidth = 2, relief = "ridge")
F.master.columnconfigure(0, weight = 1)
F.master.rowconfigure(0, weight = 1)
F.grid(sticky="NEWS")

F.columnconfigure(0, weight = 1)
F.columnconfigure(1, weight = 2)

b1 = Button(master=F, text="Button1")
b2 = Button(master=F, text="Button2")

b1.grid(sticky="NEWS")
b2.grid(sticky="NEWS", column = 1, row = 0)

mainloop()
