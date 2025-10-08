import customtkinter as ctk
import tkinter.filedialog as fd
import pygame   

#Initialize pygame mixer
pygame.mixer.init()

#Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#window
app = ctk.CTk()
app.title("Music Player")
app.geometry("500x400")


def load_file():
    file = fd.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file:
        pygame.mixer.music.load(file)
        song_label.configure(text=f"Loaded: {file.split('/')[-1]}")

def play_song():
    pygame.mixer.music.play()

def pause_song():
    pygame.mixer.music.pause()

def resume_song():
    pygame.mixer.music.unpause()

def stop_song():
    pygame.mixer.music.stop()

def set_volume(value):
    pygame.mixer.music.set_volume(float(value))

#UI Components
song_label = ctk.CTkLabel(app, text="No song loaded", font=("Arial", 16))
song_label.pack(pady=20)

load_button = ctk.CTkButton(app, text="Load Song", command=load_file)
load_button.pack(pady=5)

play_button = ctk.CTkButton(app, text="Play", command=play_song)
play_button.pack(pady=5)

pause_button = ctk.CTkButton(app, text="Pause", command=pause_song)
pause_button.pack(pady=5)

resume_button = ctk.CTkButton(app, text="Resume", command=resume_song)
resume_button.pack(pady=5)

stop_button = ctk.CTkButton(app, text="Stop", command=stop_song)
stop_button.pack(pady=5)

volume_slider = ctk.CTkSlider(app, from_=0, to=1, command=set_volume)
volume_slider.set(0.5)  
volume_slider.pack(pady=10)


app.mainloop()
