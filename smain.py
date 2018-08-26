from tkinter import *
window=Tk()
window.title("Government App")
window.geometry('350x200')
lbl=Label(window, text="Welcome to e-office")
lbl.grid(column=0,row=0)
btn=Button(window,text="Go")
btn.grid(column=1,row=0)
window.mainloop()
