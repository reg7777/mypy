from Tkinter import *
import tkFont
def killme():
    root.quit()
    root.destroy()
root=Tk(className="My first GUI")
root.geometry('10x10+0+0')
root.config(bg='black')
dFont=tkFont.Font(family="Arial", size=30)
lb=Text(root, width=16, height=5, font=dFont)
yscrollbar=Scrollbar(root, orient=VERTICAL, command=lb.yview)
yscrollbar.pack(side=RIGHT, fill=Y)
lb["yscrollcommand"]=yscrollbar.set
lb.pack(side=LEFT, fill=BOTH, expand = YES)
root.geometry('800x600+0+0')
root.mainloop()
