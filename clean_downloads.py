import sys, time
from os import scandir, rename
from os.path import exists, join, splitext
from time import sleep

    
from shutil import move
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#the following are set source file where I detect any changes and destinations of different file types organized by folder
# Feel free to modify the source file you want to monitor
src_dir = "/Users/jaeyeonlee/Downloads/"
dest_dir_audio = ""
dest_dir_image = ""
dest_dir_pdf = ""
dest_dir_video = ""
dest_dir_word = ""
dest_dir_excel = ""

#folder names for each type of media/downloads

pdf_folder = "/Users/jaeyeonlee/Downloads/PDFs"
audio_folder = "/Users/jaeyeonlee/Downloads/Audios"
image_folder = "/Users/jaeyeonlee/Downloads/Images"
video_folder = "/Users/jaeyeonlee/Downloads/Videos"
excel_folder = "/Users/jaeyeonlee/Downloads/Excels"
word_folder = "/Users/jaeyeonlee/Downloads/Words"

#following are the lists of formats for each file type I often download and store for furture usage

image_formats = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
audio_formats = [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".aiff", ".alac", ".pcm"]
video_formats = [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm", ".m4v", ".3gp", ".mpg"]
excel_formats = [".xlsx", ".xlsm", ".xlsb", ".xltx", ".xltm", ".xlt", ".xls", ".xml", ".xla", ".xlw", ".xlr"]
word_formats = [".docx", ".doc"]

def move_file(dest, entry, name):
    #check if file already exists in the folder
    if f"{dest}/name" in 

def unique_name():
    pass



class myEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(src_dir) as entries:
            for entry in entries:
                if entry.is_file(): #we are only going to orgainze files
                    name = entry.name
                    self.check_audio(entry, name)
                    self.check_video(entry, name)
                    self.check_image(entry, name)
                    self.check_word(entry, name)
                    self.check_excel(entry, name)
                    self.check_pdf(entry, name)
    def check_audio(self, entry, name):
        if audio_folder not in os.listdir(src_dir):
            os.makedirs(audio_folder, exist_ok=True)
        if name.endswith(audio_formats) or name.endswith(audio_formats.upper()):
            move_file(dest, entry, name)
            
    def check_video(self, entry, name):
        if video_folder not in os.listdir(src_dir):
            os.makedirs(video_folder, exist_ok=True)
        if name.endswith(video_formats) or name.endswith(video_formats.upper()):
            move_file(dest, entry, name)
            
    def check_image(self, entry, name):
        if image_folder not in os.listdir(src_dir):
            os.makedirs(image_folder, exist_ok=True)
        if name.endswith(image_formats) or name.endswith(image_formats.upper()):
            move_file(dest, entry, name)
            
    def check_word(self, entry, name):
        if word_folder not in os.listdir(src_dir):
            os.makedir(word_folder, exist_ok=True)
        if name.endswith(word_formats) or name.endswith(word_formats.upper()):
            move_file(dest, entry, name)
            
    def check_excel(self, entry, name):
        if excel_folder not in os.listdir(src_dir):
            os.makedirs(excel_folder, exist_ok=True)
        if name.endswith(excel_formats) or name.endswith(excel_formats.upper()):
            move_file(dest, entry, name)
            
    def check_pdf(self, entry, name):
        if pdf_folder not in os.listdir(src_dir):
            os.makedirs(pdf_folder, exist_ok=True)
        if name.endswith('.pdf'):
            move_file(dest, entry, name)

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
