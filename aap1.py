import pygame
import tkinter as tk
from tkinter import filedialog

pygame.init()

# Define the window size
win_width = 500
win_height = 300

# Create the window
win = tk.Tk()
win.geometry('{}x{}'.format(win_width, win_height))
win.title("Music Player")

# Create the buttons
play_button = tk.Button(win, text="Play", width=10)
pause_button = tk.Button(win, text="Pause", width=10)
stop_button = tk.Button(win, text="Stop", width=10)

# Define the button actions
def play_music():
    pygame.mixer.music.load(file_path.get())
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

# Place the buttons in the window
play_button.pack()
pause_button.pack()
stop_button.pack()

# Add a file dialog to select the music file
file_path = tk.StringVar()

def browse_file():
    file_path.set(filedialog.askopenfilename())

browse_button = tk.Button(win, text="Browse", command=browse_file)
browse_button.pack()

file_path_label = tk.Label(win, textvariable=file_path)
file_path_label.pack()

# Loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the button states based on the music status
    if pygame.mixer.music.get_busy():
        play_button.config(state="disabled")
        pause_button.config(state="normal")
        stop_button.config(state="normal")
    else:
        play_button.config(state="normal")
        pause_button.config(state="disabled")
        stop_button.config(state="disabled")

    # Update the window
    win.update()
