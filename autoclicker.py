import pyautogui as pyg
import time
import keyboard


time.sleep(3)

while True:
    pyg.leftClick()
    if keyboard.is_pressed("esc"):
        break
