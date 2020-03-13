import random
from tkinter import *
import string

def generate_password():
    password = []
    for entry in range(5):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)

#converting password into a string
    y = "".join(str(x) for x in password)
    label.config(text=y)


passwd = Tk()
passwd.title("Random Password Generator")
passwd.geometry("300x250")
button=Button(passwd, text="Generate Password", fg="blue", bg='red', command=generate_password)
button.grid(row=2,column=2)
label=Label(passwd, font=("times", 18, "bold"), fg="yellow")
label.grid(row=4,column=2)
passwd.mainloop()