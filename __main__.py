import pyautogui
import keyboard as kb
import time
from tkinter import *
global auto_loot
auto_loot = False
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
winx = (round(screen_width/3))
winy = (round(screen_height/3))
#root.title("autoloot")
#root.configure(width=500, height=300)
#root.geometry("{}x{}+{}+{}".format(winx, winy, winx, winy))
#root.mainloop()
def loot():
    Coord = pyautogui.locateCenterOnScreen('unique.png', region=(winx, winy, winx, winy))
    Coord2 = pyautogui.locateCenterOnScreen('rune.png', region=(winx, winy, winx, winy))
    if Coord is None and Coord2 is None:
        print("No loot")
    elif Coord is not None:
        pyautogui.click(Coord.x, Coord.y)
        time.sleep(1)
    elif Coord2 is not None:
        pyautogui.click(Coord2.x, Coord2.y)
        time.sleep(1)

def start():
    global auto_loot
    auto_loot = not auto_loot
    if auto_loot == True:
        print("start")
    else:
        print("stop")
kb.add_hotkey('insert', start)
while True:
    if auto_loot:
        loot()
    else:
        pass
