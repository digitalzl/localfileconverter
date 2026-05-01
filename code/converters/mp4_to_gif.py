import subprocess
import os
from utils.ffmpeg_path import get_ffmpeg_path

FFMPEG_PATH = get_ffmpeg_path()

def convert_mp4_to_gif(input_file):
    output_file = os.path.splitext(input_file)[0] + ".gif"
    palette = os.path.splitext(input_file)[0] + "_palette.png"

    subprocess.run([
        FFMPEG_PATH,
        "-i", input_file,
        "-vf", "fps=10,scale=480:-1:flags=lanczos,palettegen",
        palette
    ], check=True)

    subprocess.run([
        FFMPEG_PATH,
        "-i", input_file,
        "-i", palette,
        "-lavfi", "fps=10,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse",
        output_file
    ], check=True)

    os.remove(palette)
    return output_file