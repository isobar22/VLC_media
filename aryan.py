import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer

root = Tk()

# Create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create a submenu

subMenu = Menu(menubar, tearoff=0)


def browse_file():
    global filename
    filename = filedialog.askopenfile()
    print(filename)


menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo('About Melody', 'This is a music player build using Python Tkinter by aryan.')


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)
subMenu.add_command(label="Exit")

mixer.init()  # intializing the mixer

root.geometry('300x300')
root.title("Melody")
root.iconbitmap(r'favicon.ico')

text = Label(root, text='Lets make some noise!')
text.pack()


def play_music():
    try:
        mixer.music.load(filename)
        mixer.music.play()
        statusbar['text'] = "Playing music" + ' ' + filename
    except:
        tkinter.messagebox.showerror('File not found', 'Melody could not find the file. Please check again.')


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)
    # set volume of mixer takes value only from  0 to 1. Example - 0.1,0.55,0.54,0.99,1


playPhoto = PhotoImage(file='play-button (1).png')
playBtn = Button(root, image=playPhoto, command=play_music)
playBtn.pack()

stopPhoto = PhotoImage(file='stop button.png')
stopBtn = Button(root, image=stopPhoto, command=stop_music)
stopBtn.pack()

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack()

statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
