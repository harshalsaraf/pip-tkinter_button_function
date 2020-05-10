from tkinter import *

window = Tk()
window.title("bu command")


def click():
    l1 = Label(window, text="clicked")
    l1.pack()


button = Button(window, text="button", command=click)
button.pack()



window.mainloop()
