import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("Simpli Music Player")
root.geometry("485x300+290+10")
root.configure(background='#333333')
root.resizable(False, False)
mixer.init()

# Create a function to open a file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
              if song.endswith(".mp3"):
                     Playlist.insert(END, song)


def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


# icon
lower_frame = Frame(root , bg = "#FFFFFF", width = 485 , height = 120 )
lower_frame.place ( x = 0 , y = 180)

image_icon = PhotoImage(file="music icon.png")
root.iconphoto(False, image_icon)

# Button
ButtonPlay = PhotoImage(file="play-button.png")
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=PlayMusic).place(x=180, y=220)

ButtonStop = PhotoImage(file="stop1.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.stop).place(x=80, y=220)

ButtonUnpause = PhotoImage(file="unpause.png")
Button(root, image=ButtonUnpause, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.unpause).place(x=380, y=220)

ButtonPause = PhotoImage(file="pause.png")
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.pause).place(x=280, y=220)

# Label       

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=34, width=485, height=150)

Button(root, text="Browse Music", width=59, height=1, font=("calibri",
      12, "bold"), fg="Black", bg="#FFFFFF", command=AddMusic).place(x=0, y=0)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# Execute Tkinter

root.mainloop()