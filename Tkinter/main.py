from tkinter import *
window=Tk()

window.title("My first GUI")
window.minsize(600,600)
my_label=Label(text="Hii I am Pushpak")
my_label.grid(column=0,row=0)

def click():
    my_label.config(text=input.get())


button=Button(text="Click me",command=click)
button.grid(column=2,row=2)

input=Entry()
input.grid(row=4,column=4)

new_button=Button(text="Ye hai naya button")
new_button.grid(column=3,row=0)















window.mainloop()
