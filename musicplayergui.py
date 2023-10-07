import os
import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize pygame
pygame.mixer.init()

# Create a function to add music to the playlist
def add_to_playlist():
    file_path = filedialog.askopenfilename(title="Select Music", filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        playlist.insert(tk.END, file_path)

# Create a function to play selected music
def play_music():
    selected_song = playlist.get(tk.ACTIVE)
    if selected_song:
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play(loops=0)

# Create a function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Create the main window
root = tk.Tk()
root.title("Music Player")

# Create and configure the playlist
playlist = tk.Listbox(root, selectmode=tk.SINGLE, bg="lightgray")
playlist.pack(fill=tk.BOTH, expand=True)

# Create buttons
add_button = tk.Button(root, text="Add Music", command=add_to_playlist)
play_button = tk.Button(root, text="Play", command=play_music)
stop_button = tk.Button(root, text="Stop", command=stop_music)

add_button.pack()
play_button.pack()
stop_button.pack()

root.mainloop()
