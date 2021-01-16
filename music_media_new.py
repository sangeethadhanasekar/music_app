from pathlib import *
from tkinter import *
import pygame
pygame.init()
pygame.mixer.init()
#global song


   
root=Tk()
root.title("MINI PLAYER")
root.geometry('500x600')
name_var=StringVar()
lists_var=StringVar()

def play_pressed():
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def pause_pressed():
    pygame.mixer.music.pause()
def unpause_pressed():
    pygame.mixer.music.unpause()
def stop_pressed():
    pygame.mixer.music.stop()
    
def music_names_load():
    entries=Path('sounds/')
    for entry in entries.iterdir():
            a.insert(1,entry)

def music_name(value):
    music_name=value
    play_pressed(music_name)
    
    
            
def music_name_out(event):
              
             name_entry.delete(1,END)
             w=event.widget
             idx=int(w.curselection()[0])
             value=w.get(idx)
             name_entry.insert(1,value)
             global song
             song=value
             
             
#def play_presseds():
           
#music list and music playlist display
label1=Label(root,text="music track :",font=("arieal",13)).grid(row=1,column=0,padx=0)
name_entry=Entry(root,width=50,textvariable=name_var,cursor='hand2')
name_entry.grid(row=1,column=1,padx=0,pady=0)
label2=Label(root,text="select the music from the below list:",font=("Helvetica",12)).grid(row=2,column=1,padx=5,pady=4)
a=Listbox(root,height=10,width=30,font=("Helvetica",16),cursor='dot',selectmode='SINGLE')
a.grid(row=3,column=1)
a.bind('<<ListboxSelect>>',music_name_out)


#buttons display 
pause_button=Button(root,text="PAUSE",height=2,width=20,command=pause_pressed).grid(row=4,column=0,padx=5,pady=10)
unpause_button=Button(root,text="UNPAUSE",height=2,width=20,command=unpause_pressed).grid(row=5,column=0,padx=5,pady=10)
play_button=Button(root,text="PLAY",height=2,width=20,command=play_pressed)
play_button.grid(row=4,column=2,padx=2,pady=10)
stop_button=Button(root,text="STOP",height=2,width=20,command=stop_pressed).grid(row=5,column=2,padx=2,pady=10)
play_button.bind('<<ButtonSelect>>',play_pressed)





#window resize when window enlarged or minimized 
root.columnconfigure(0,weight=1,minsize=75)
root.columnconfigure(1,weight=1,minsize=75)
root.columnconfigure(2,weight=1,minsize=75)
root.rowconfigure(0,weight=1,minsize=50)
root.rowconfigure(1,weight=1,minsize=50)
root.rowconfigure(2,weight=1,minsize=50)
root.rowconfigure(3,weight=1,minsize=50)
root.rowconfigure(4,weight=1,minsize=5)



music_names_load()


root.mainloop()
