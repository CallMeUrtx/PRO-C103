import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
pasta = 'C:\Users\kevin\Documents\merda'
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'ola, {event.src_path}foi criado')
    def on_deleted(self,event):
        print(f'alguem excluiu{event.src_path}')
    def on_modified(self,event):
        print(f'ola, foi modificado{event.src_path}')
    def on_moved(self,event):
        print(f'alguem moveu{event.src_path}para{event.dest_path}')

evento = FileEventHandler()
observer = Observer()
observer.schedule(evento, pasta, recursive = True)
observer.start()
try:
    while True:
        time.sleep(2)
        print('executando')
except KeyboardInterrupt:
    print('interompido')
    observer.stop()
        
            
                   