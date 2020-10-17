#Main FIle of MP3Player
# Author: Ashwani Rathee
# Learned a lot

#Importing Libraries
from tkinter import *
from tkinter import filedialog
import pygame


root=Tk()
root.title('Tkloid')             # Name of the player
root.geometry("960x540")       # Size of the player
root.resizable(0, 0)

photo = PhotoImage(file = "assets/icons/icon.png")
root.iconphoto(False, photo)
#Initialize pygame.Mixer
root.configure(background='#efefef')

pygame.mixer.init()

#add song function
def add_song():
	song = filedialog.askopenfilename(initialdir="assets/audio/",title="Choose A song",filetypes=(("mp3 Files","*.mp3"),("wav files","*.wav"),("m4a files","*.m4a"),("ogg files","*.ogg"),))
	song = song.replace("/home/ashwani/hamr-project-final/assets/audio/","")
	song_box.insert(END,song)

def play():
	song =song_box.get(ACTIVE)
	song = f'/home/ashwani/hamr-project-final/assets/audio/{song}'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.load(song)
    song_box.selection_clear(ACTIVE)

#create PLayist Box
song_box =Listbox(root,bg="white",fg="black",width=100,height=200,selectbackground="gray")
song_box.pack(pady=20,padx=20)

#create player control buttons
back_btn_img = PhotoImage(file='assets/icons/backward.png')
forward_btn_img = PhotoImage(file='assets/icons/fast-forward.png')
play_btn_img = PhotoImage(file='assets/icons/music.png')
pause_btn_img = PhotoImage(file='assets/icons/pause.png')
stop_btn_img = PhotoImage(file='assets/icons/stop.png')

#create player control frame
controls_frame=Frame(root)
controls_frame.pack()

#create player control buttons
back_button = Button(controls_frame,image=back_btn_img,borderwidth=0)
forward_button = Button(controls_frame,image=forward_btn_img,borderwidth=0)
play_button = Button(controls_frame,image=play_btn_img,borderwidth=0,command=play)
pause_button = Button(controls_frame,image=pause_btn_img,borderwidth=0)
stop_button = Button(controls_frame,image=stop_btn_img,borderwidth=0,command=stop)

back_button.grid(row=0,column=0,padx=10)

play_button.grid(row=0,column=2,padx=10)
pause_button.grid(row=0,column=1,padx=10)
stop_button.grid(row=0,column=3,padx=10)

forward_button.grid(row=0,column=4,padx=10)

#create menu
my_menu=Menu(root)
root.config(menu=my_menu)

#Add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="File",menu=add_song_menu)
add_song_menu.add_command(label="Add to List",command=add_song)

#Audio Analysismenu

root.mainloop()