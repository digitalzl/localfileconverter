import subprocess
import os
from utils.ffmpeg_path import get_ffmpeg_path

FFMPEG_PATH = get_ffmpeg_path()

def convert_ts_to_mp4(input_file):
    output_file = os.path.splitext(input_file)[0] + ".mp4"

    command = [
        FFMPEG_PATH,
        "-i", input_file,
        "-c", "copy",
        output_file
    ]

    subprocess.run(command, check=True)
    return output_file