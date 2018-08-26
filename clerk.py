from tkinter import *

master = Tk()
Label(master, text="User Phone number").grid(row=50)
Label(master, text="Application Details").grid(row=60)
Label(master, text="To whom forwarded").grid(row=70)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e1.grid(row=50, column=50)
e2.grid(row=60, column=50)
e3.grid(row=70, column=50)
btn=Button(master,text="Go")
btn.grid(column=50,row=80)

mainloop( )