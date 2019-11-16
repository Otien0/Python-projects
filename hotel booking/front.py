from tkinter import *

window = Tk()
window.title("Hotel Booking")

Label1 = Label(window, text="Casino Royale Hotel").grid(row=0,column=0)
Label2 = Label(window, text="Name").grid(row=1,column=0)
Label3 = Label(window, text="Adress").grid(row=2,column=0)
Label4 = Label(window, text="Phone number").grid(row=3,column=0)
Label5 = Label(window, text="number of days you want to stay in: ").grid(row=4,column=0)
Label6 = Label(window, text="Room type(Normal, king or delux) :").grid(row=5,column=0)
Label7 = Label(window, text="total amount").grid(row=6,column=0)

name_text=StringVar()
entry1=Entry(window,textvariable=name_text).grid(row=1,column=1)

address_text=StringVar()
entry2=Entry(window,textvariable=address_text).grid(row=2,column=1)

phone_number_text=StringVar()
entry3=Entry(window,textvariable=phone_number_text).grid(row=3,column=1)

noof_text=StringVar()
entry4=Entry(window,textvariable=noof_text).grid(row=4,column=1)

roomtype_text=StringVar()
entry5=Entry(window,textvariable=roomtype_text).grid(row=5,column=1)

amount_text=StringVar()
entry6=Entry(window,textvariable=amount_text).grid(row=6,column=1)



window.mainloop()
