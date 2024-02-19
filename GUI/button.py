
# TKinter for GUI (Buttons)
from tkinter import *
# CREATE THE WINDOW
root = Tk()
def myClick():
    myLabel = Label(root, text="I clicked the Button!")
    myLabel.pack()
    
    
#Creating a label widget
myButton = Button(root, text="Click Me!", command=myClick, fg="blue",bg="red")#no parantesis for the functions#Control Button Size,padx=50, pady=50)#, state=DISABLED) IT WILL BE GHRADED OUT AND OYU WILL NOT BE ABLE TO CLICK IT
myButton.pack()
#creat an evernt loop looping ex check when your mouse moving
root.mainloop()
