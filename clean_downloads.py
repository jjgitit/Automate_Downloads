from os import scandir
from time import sleep
from shutil import move

from wachdog.observers import Observer
from wachdog.events import FileSystemEventHandler


