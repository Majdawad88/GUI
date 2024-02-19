
# TKinter for GUI (Grid)
from tkinter import *
# CREATE THE WINDOW
root = Tk()
#Creating a label widget
myLabel1 = Label(root, text="Hello Word!")
myLabel2 = Label(root, text="My name is Majd Awad",padx = 50,pady = 50,fg = "red",bg = "blue")
myLabel3 = Label(root, text="    ").grid(row=1, column=1)
#shoving it onto the screen PACK IT IN AS BIG AS THE STUFF is
#myLabel.pack()
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
#creat an evernt loop looping ex check when your mouse moving
root.mainloop()
