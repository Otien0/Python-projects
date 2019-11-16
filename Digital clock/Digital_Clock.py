import sys
from tkinter import *
import time

def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)


watch=Tk()
watch.title("My Watch")
watch.geometry("500x200")
clock=Label(watch,font=("times",50,"bold"),fg="yellow",bg="blue")
clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi=Label(watch,text="Digital Clock",font=("times 24 bold"),fg="green")
digi.grid(row=0,column=2)

nota=Label(watch,text="hours   minutes   seconds   ",font=("times 15 bold"))
nota.grid(row=3,column=2)

watch.mainloop()
