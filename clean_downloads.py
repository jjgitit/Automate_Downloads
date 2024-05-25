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

#following are the lists of formats for each file type I often download and store for furture usage

image_formats = []
audio_formats = []
video_formats = []

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
    def check_audio(self, cur_file):
        pass
    def check_video(self, cur_file):
        pass
    def check_image(self, cur_file):
        pass
    def check_word(self, cur_file):
        pass
    def check_excel(self, cur_file):
        pass
    def check_pdf(self, cur_file):
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
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
