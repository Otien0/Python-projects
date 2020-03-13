from tkinter import *
import pygame
import os
import time

player=Tk()
player.title("my music player")
player.geometry("400x250")  

pygame.mixer.init()

n=0

def start():
	global n
	n=n+1

	if n==1:
		song_name=songs_listbox.get()
		pygame.mixer.music.load(song_name)
		pygame.mixer.music.play(0)
		print("music started ")
		pygame.mixer.music.set_volume(Volume.get())
		print(pygame.mixer.music.get_volume())
		print(Volume.get())

	elif (n%2)!=0:
		pygame.mixer.music.unpause()
		print("unPaused")
		
def stop():
        pygame.mixer.music.pause()
        print("paused")

def play_next(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index]/length-1)
    pygame.mixer.music.play()



l1=Label(player,text="MUSIC PLAYER",font=("times",20,"bold"),fg="black",bg="#b51253")
l1.grid(row=1,column=1)

b1=Button(player,text='Play',width=20,font=("roman",10,"bold"),fg="purple",bg="pink",command=start)
b1.grid(row=4,column=1)
b2=Button(player,text='Stop',width=20,font=("roman",10,"bold"),fg="purple",bg="red",command=stop)
b2.grid(row=8,column=1)
b3=Button(player,text='Next',width=20,font=("roman",10,"bold"),fg="purple",bg="pink",command=play_next)
b3.grid(row=8,column=2)

Volume=Scale(player,from_=1.0,to_=10.0,orient = HORIZONTAL, resolution=0.1,bg="#15032e")
Volume.grid(row=10,column=1)

songs_list=os.listdir()
songs_listbox=StringVar(player)
songs_listbox.set("select songs")
menu=OptionMenu(player,songs_listbox,*songs_list)
menu.grid(row=4,column=2)

        
player.mainloop()
