import subprocess
import os
from utils.ffmpeg_path import get_ffmpeg_path

FFMPEG_PATH = get_ffmpeg_path()

def convert_mp4_to_mp3(input_file):
    output_file = os.path.splitext(input_file)[0] + ".mp3"

    command = [
        FFMPEG_PATH,
        "-y",
        "-i", input_file,
        "-vn",              # no video
        "-acodec", "libmp3lame",
        "-ab", "320k",      # bitrate
        output_file
    ]

    subprocess.run(command, check=True)
    return output_file