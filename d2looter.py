import pyautogui
import keyboard as kb
import tkinter as tk
global auto_loot
auto_loot = False
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
winx = (round(screen_width/3))
winy = (round(screen_height/3))
# Create the overlay window as a translucent Toplevel window
overlay1 = tk.Toplevel(root)
overlay1.overrideredirect(True)
overlay1.attributes('-alpha', .5)  # Set the overlay transparency (0.5 for 50% transparency)
overlay1.geometry(f'{screen_width}x{winy}+0+0')
overlay1.configure(bg='black')

# Create the left rectangle
overlay2 = tk.Toplevel(root)
overlay2.overrideredirect(True)
overlay2.attributes('-alpha', .5)  # Set the overlay transparency (0.5 for 50% transparency)
overlay2.geometry(f'{winx}x{winy}+0+{winy}')
overlay2.configure(bg='black')

# Create the right rectangle
overlay3 = tk.Toplevel(root)
overlay3.overrideredirect(True)
overlay3.attributes('-alpha', .5)  # Set the overlay transparency (0.5 for 50% transparency)
overlay3.geometry(f'{winx}x{winy}+{2*winx}+{winy}')
overlay3.configure(bg='black')

# Create the bottom rectangle
overlay4 = tk.Toplevel(root)
overlay4.overrideredirect(True)
overlay4.attributes('-alpha', .5)  # Set the overlay transparency (0.5 for 50% transparency)
overlay4.geometry(f'{screen_width}x{winy}+0+{2*winy}')
overlay4.configure(bg='black')
root.update()
def show():
    root.update()
    overlay1.deiconify()
    overlay2.deiconify()
    overlay3.deiconify()
    overlay4.deiconify()
    global auto_loot
    if auto_loot == False:
        root.withdraw()
        overlay1.withdraw()
        overlay2.withdraw()
        overlay3.withdraw()
        overlay4.withdraw()
def loot():
    Coord = pyautogui.locateCenterOnScreen('unique.png', region=(winx, winy, winx, winy))
    Coord2 = pyautogui.locateCenterOnScreen('rune.png', region=(winx, winy, winx, winy))
    if Coord is None and Coord2 is None:
        print("No loot")
    elif Coord is not None:
        pyautogui.click(Coord.x, Coord.y)
    elif Coord2 is not None:
        pyautogui.click(Coord2.x, Coord2.y)
    

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
        show()
        loot()
    else:
        root.withdraw()
        overlay1.withdraw()
        overlay2.withdraw()
        overlay3.withdraw()
        overlay4.withdraw()
root.mainloop()