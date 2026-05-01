import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter

from converters.ts_to_mp4 import convert_ts_to_mp4
from converters.mp4_to_gif import convert_mp4_to_gif
from converters.mp4_to_mp3 import convert_mp4_to_mp3

import sys
import os

sys.path.append(os.path.dirname(__file__))


def select_ts():
    file_path = filedialog.askopenfilename(
        title="Select TS file",
        filetypes=[("TS files", "*.ts")]
    )

    if file_path:
        try:
            output = convert_ts_to_mp4(file_path)
            messagebox.showinfo("Success", f"Converted:\n{output}")
        except:
            messagebox.showerror("Error", "Conversion failed")


def select_mp4():
    file_path = filedialog.askopenfilename(
        title="Select MP4 file",
        filetypes=[("MP4 files", "*.mp4")]
    )

    if file_path:
        try:
            output = convert_mp4_to_gif(file_path)
            messagebox.showinfo("Success", f"GIF created:\n{output}")
        except:
            messagebox.showerror("Error", "Conversion failed")

def select_mp4_audio():
    file_path = filedialog.askopenfilename(
        title="Select MP4 file",
        filetypes=[("MP4 files", "*.mp4")]
    )

    if file_path:
        try:
            output = convert_mp4_to_mp3(file_path)
            messagebox.showinfo("Success", f"MP3 created:\n{output}")
        except:
            messagebox.showerror("Error", "Conversion failed")


# GUI 
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.geometry(f"{300}x{200}")

button = customtkinter.CTkButton(master=app, hover_color="#000266", text=".ts to .mp4", command=select_ts)
button.pack(pady=10, padx=10)

button = customtkinter.CTkButton(master=app, hover_color="#000266", text=".mp4 to .gif", command=select_mp4)
button.pack(pady=10, padx=10)

button = customtkinter.CTkButton(master=app, hover_color="#000266", text=".mp4 to .mp3", command=select_mp4_audio)
button.pack(pady=10, padx=10)

app.mainloop()