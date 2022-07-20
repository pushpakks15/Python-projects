from tkinter import *
window=Tk()
window.minsize(600,600)
window.title("Mile to Km converter")
window.config(padx=200,pady=200)

entry=Entry(width=20)
entry.grid(column=2,row=0)

label=Label(text="Miles")
label.grid(column=3,row=0)

label1=Label(text="is equal to")
label1.grid(column=1,row=2)

label2=Label(text="0")
label2.grid(column=2,row=2)

label=Label(text="Km")
label.grid(column=3,row=2)


def on_click():
    mile=float(entry.get())
    Km=round(mile*1.6)
    label2.config(text=Km)


button=Button(text="Calculate",command=on_click)
button.grid(column=2,row=3)












window.mainloop()
