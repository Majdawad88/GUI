
# TKinter for GUI (Input Fields)
from tkinter import *
# CREATE THE WINDOW
root = Tk()
e = Entry(root, width =50,bg="blue",fg="white", borderwidth = 5)
e.pack()
e.insert(0, "Enter Your Name: ")
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
    
    
#Creating a label widget
myButton = Button(root, text="Enter your name: ", command=myClick, fg="blue",bg="red")#no parantesis for the functions#Control Button Size,padx=50, pady=50)#, state=DISABLED) IT WILL BE GHRADED OUT AND OYU WILL NOT BE ABLE TO CLICK IT
myButton.pack()
#creat an evernt loop looping ex check when your mouse moving
root.mainloop()
