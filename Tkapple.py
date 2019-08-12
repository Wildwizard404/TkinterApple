from tkinter import *
from PIL import Image,ImageTk
import os,sys,time 
import pygame
top = Tk()
top.geometry('1500x842')
top.resizable(0,0)
top.title("Tkapple")
top.iconbitmap("Tkapple.ico")
lshow = Text(top,height=50, width=123)
lshow.place(x=0 ,y=0,anchor=NW)
lettersfile = open("bear/0.txt","r")
letters = lettersfile.read()
lshow.delete(0.0, END)
lshow.insert(END,letters)
im=Image.open("img_bear/0.jpg")
img=ImageTk.PhotoImage(im)
pshow = Label(top,image=img)
pshow.place(x=925 ,y=0,anchor=NW)
fpsshow = Label(top,text = "FPS:00.00000000000000")
fpsshow.place(x=1135 ,y=580,anchor=NW)
def play():
    time_start,now_time = time.time(),time.time()
    now_time += 0.01
    play_index = 1
    pygame.mixer.music.play()
    while play_index <= 6573:
        #show letters
        lettersfile = open("bear/"+str(play_index)+".txt","r")
        letters = lettersfile.read()
        lshow.delete(0.0, END)
        lshow.insert(END,letters)
        
        #show pics
        im=Image.open("img_bear/"+str(play_index)+".jpg")
        img=ImageTk.PhotoImage(im)
        pshow.config(image=img)
        
        top.update()
        old_time = now_time
        now_time = time.time()
        fpsshow.config(text = "FPS:"+str(1/(now_time-old_time)))
        play_index = int(30.014*(time.time()-time_start))
pygame.mixer.init()
track = pygame.mixer.music.load("badapple.mp3")
Button(top,text = "开始",command = play,height = 4,width = 10).place(x=1160 ,y=600,anchor=NW)
mainloop()


