import os, sys, time
from os import scandir, rename
from time import sleep
from shutil import move
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#the following are set source file where I detect any changes and destinations of different file types organized by folder
# Feel free to modify the source file you want to monitor
src_dir = "../../Downloads/"
dest_dir_audio = ""
dest_dir_image = ""
dest_dir_pdf = ""
dest_dir_video = ""
dest_dir_word = ""
dest_dir_excel = ""

#folder names for each type of media/downloads

pdf_folder = "PDF"
audio_folder = "Audios"
image_folder = "Images"
video_folder = "Videos"
excel_folder = "Excels"
word_folder = "Words"

#following are the lists of formats for each file type I often download and store for furture usage

image_formats = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
audio_formats = [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".aiff", ".alac", ".pcm"]
video_formats = [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm", ".m4v", ".3gp", ".mpg"]
excel_formats = [".xlsx", ".xlsm", ".xlsb", ".xltx", ".xltm", ".xlt", ".xls", ".xml", ".xla", ".xlw", ".xlr"]


class myEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(src_dir) as entries:
            for entry in entries:
                if entry.is_file(): #we are only going to orgainze files
                    name = entry.name
                    check_audio(entry, name)
                    check_video(entry, name)
                    check_image(entry, name)
                    check_word(entry, name)
                    check_excel(entry, name)
                    check_pdf(entry, name)
    def check_audio(self, name):
        pass
    def check_video(self, name):
        pass
    def check_image(self, name):
        pass
    def check_word(self, name):
        if entry.endswith('.docx') or entry.endswith('.doc'):
        #move to word folder
    def check_excel(self, name):
        if entry.endswith(excel_formats):
            pass
    def check_pdf(self, name):
        if entry.endswith('.pdf'):
            pass

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = src_dir
    event_handler = myEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1) #we are detecting the change in source folder every second
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
