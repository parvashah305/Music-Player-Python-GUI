from tkinter import *
import pygame
import os
from tkinter import filedialog

pygame.mixer.init()

player=Tk()
player.geometry("500x300")
player.title("Music Player")
player.resizable(0,0)
player.configure(background="blue")

song_box=Listbox(player,bg="black",fg="green",width=60,selectbackground="Aqua",selectforeground="black")
song_box.pack(pady=20)

def add_song():
    song=filedialog.askopenfilename(initialdir="audio",title="Choose a song")
    song_box.insert(END,song[song.rfind("/")+1:-4])

def add_many_song():

    songs=filedialog.askopenfilenames(initialdir="audio",title="Choose a songs")

    for song in songs:
        song_box.insert(END,song[song.rfind("/")+1:-4])

def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

def delete_all_song():
    song_box.delete(0,END)
    pygame.mixer.music.stop()


def play():
    selected_song = song_box.get(ACTIVE)
    path = os.getcwd().replace("\\", "/")
    song1=f"{path}/audio/{selected_song}.mp3"


    pygame.mixer.music.load(song1)
    pygame.mixer.music.play(loops=0)


def forward():
    next_song=song_box.curselection()
    next_song=next_song[0]+1

    song=song_box.get(next_song)

    path = os.getcwd().replace("\\", "/")
    song1=f"{path}/audio/{song}.mp3"

    
    pygame.mixer.music.load(song1)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0,END)

    song_box.activate(next_song)

    song_box.selection_set(next_song,last=None)

def backward():
    previous_song=song_box.curselection()
    previous_song=previous_song[0]-1

    song=song_box.get(previous_song)

    path = os.getcwd().replace("\\", "/")
    song1=f"{path}/audio/{song}.mp3"

    
    pygame.mixer.music.load(song1)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0,END)

    song_box.activate(previous_song)

    song_box.selection_set(previous_song,last=None)


    
def stop():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)

paused=False

def pause(is_paused):

    global paused

    if paused:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True

#start_button_img=PhotoImage(file="play.png")
#back_button_img=PhotoImage(file="back.png")
#forward_button_img=PhotoImage(file="forward.png")
#pause_button_img=PhotoImage(file="pause.png")
#stop_button_img=PhotoImage(file="stop.png")

song_frame=Frame(player,bg="blue")
song_frame.pack()

play_button=Button(song_frame,text="Play",command=lambda: play())
back_button=Button(song_frame,text="Back",command=backward)
forward_button=Button(song_frame,text="Forward",command=forward)
pause_button=Button(song_frame,text="Pause",command=lambda: pause(paused))
stop_button=Button(song_frame,text="Stop",command=stop)

play_button.grid(row=0,column=2,padx=10)
back_button.grid(row=0,column=0,padx=10)
forward_button.grid(row=0,column=1,padx=10)
pause_button.grid(row=0,column=3,padx=10)
stop_button.grid(row=0,column=4,padx=10)

my_menu=Menu(player)
player.config(menu=my_menu)

add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
add_song_menu.add_command(label="Add one song to playlist",command=add_song)
add_song_menu.add_command(label="Add many song to playlist",command=add_many_song)


delete_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Remove Songs",menu=delete_song_menu)
delete_song_menu.add_command(label="Delete one song from playlist",command=delete_song)
delete_song_menu.add_command(label="Delete all songs from playlist",command=delete_all_song)



player.mainloop()