import pyautogui, mouseinfo, time, os
pyautogui.moveTo(1004,1049, duration=1)
pyautogui.click()
pyautogui.moveTo(569,608, duration=1)
pyautogui.click()
pyautogui.moveTo(731,441, duration=1)
pyautogui.doubleClick()
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MeuMonitor(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"Pasta criada: {event.src_path}")

# Caminho da pasta a ser monitorada
caminho = 'C:/Users/prog2/Documents/João Victor Turma 2'

observer = Observer()
observer.schedule(MeuMonitor(), path=caminho, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
