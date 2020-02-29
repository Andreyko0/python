from tkinter import *

window = Tk()
window.title("Title")
window.geometry('1200x600')
lbl = Label(window, text = "Label")
lbl.grid(column = 10, row = 0)
lbl1 = Label(window, text = "Hi!")
lbl1.grid(column = 1, row = 1)
txt = Entry(window, width = 10)
txt.grid(column = 5, row = 1)
def clicked():
    lbl1.configure(text = "Button was clicked!")


btn = Button(window, text = "Click", command = clicked )
btn.grid(column = 1, row = 4)

lbl3 = Label(window, text = "Don't press this button")
lbl3.grid(column = 1, row = 6)

txt1 = Entry(window, width = 10)
txt1.grid(column = 5, row = 6)
        
def clicked():
    lbl3.configure(text = "Error!")

btn = Button(window, text="Click", command=clicked)
btn.grid(column=1, row=7)




window.mainloop()