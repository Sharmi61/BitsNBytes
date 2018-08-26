import tkinter as tk
    

def write_slogan():
    print("welcome official ")
def write_slogan1():
    print("Welcome clerk")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="Clerk", 
                   fg="red",
                   command=write_slogan1)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="official",fg="blue",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
