import sys
from tkinter import *
import time


def tick():
    time_string=time.strftime("%H:%M:%S\n%D")
    clock.config(text=time_string)
    clock.after(30,tick)

root=Tk()
clock=Label(root,font=("times",25,"bold"),bg="blue")
clock.grid(row=50,column=50)
tick()
root.mainloop()
