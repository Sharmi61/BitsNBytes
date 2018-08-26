from tkinter import *
window=Tk()
x1=Button(window,text="image")
photo=PhotoImage(file="rr.png")
x1.config(image=photo,width="40",height="40",activebackground="black",bg="black",bd=0,command=sil)
x1.place(relx=1,x=5,y=-5,anchor=NE)
window.mainloop()