import os
import sys

def get_ffmpeg_path():
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, "ffmpeg", "bin", "ffmpeg.exe")
    
    # go up one folder from /code → project root
    base_dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_dir, "ffmpeg", "bin", "ffmpeg.exe")