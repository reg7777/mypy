## #! usr/bin/python
from Tkinter import *


window = Tk(className="My first GUI")

foo = Label(window,text="Hello World") # add a label to root window
foo.pack()

window.mainloop()
