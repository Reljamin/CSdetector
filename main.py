import pyautogui
import time
import cv2
import numpy as np
import pytesseract
from matplotlib import pyplot as plt
from playsound import playsound
from pynput import keyboard
import os
import threading
#from pynput.keyboard import Key, Controller

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print()

def get_cs():
    #pyautogui.position()
    #time.sleep(3)
    #print(pyautogui.position())
    #print(pyautogui.position())

    im1 = pyautogui.screenshot(r".\image_assets\CSnum.png", region=(1775, 2, 40, 20))

    

    imgRead = cv2.imread(r".\image_assets\CSnum.png")

    gray = cv2.cvtColor(imgRead, cv2.COLOR_BGR2GRAY)
    colored = cv2.cvtColor(imgRead, cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(gray, config='--psm 7 -c tessedit_char_whitelist=0123456789')

    if len(text) == 0:
        return 0
    else:
        return text
    






def get_livingMinions():

    minionCounter = 0

    #if os.path.exists("./image_assets/Game.png"):
        #os.remove("./image_assets/Game.png")
    game_ss = pyautogui.screenshot(r".\image_assets\Game.png")
    game_img = cv2.imread(r".\image_assets\Game.png")
    game_img = cv2.cvtColor(game_img, cv2.COLOR_BGR2RGB)
    hpbar_img = cv2.imread(r".\image_assets\minionhpbar.png")
    hpbar_img = cv2.cvtColor(hpbar_img, cv2.COLOR_BGR2RGB)
    hpbar2_img = cv2.imread(r".\image_assets\lowhpbar.png")
    hpbar2_img = cv2.cvtColor(hpbar2_img, cv2.COLOR_BGR2RGB)

    h, w = hpbar_img.shape[:2]

    res = cv2.matchTemplate(game_img, hpbar_img, cv2.TM_CCOEFF_NORMED)
    res2 = cv2.matchTemplate(game_img, hpbar2_img, cv2.TM_CCOEFF_NORMED)
    threshold1 = .98
    threshold2 = .98

    loc = np.where(res >= threshold1)
    loc2 = np.where(res2 >= threshold2)


    for pt in zip(*loc[::-1]):  # Switch columns and rows
        cv2.rectangle(game_img, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
        minionCounter += 1

    for pt in zip(*loc2[::-1]):  # Switch columns and rows
        cv2.rectangle(game_img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        minionCounter += 1

    result = cv2.imwrite(r".\image_assets\result.png", game_img)
    result1 = cv2.imread(r".\image_assets\result.png")

    #plt.subplot(1, 1, 1)
    #plt.imshow(result1)
    #plt.show()

    return minionCounter

def getMissedCS(oldMinions, curMinions, oldCS, curCS):
    deadMinions = oldMinions - curMinions

    if deadMinions < 0:
        deadMinions = 0

    csDiff = curCS - oldCS

    if csDiff >= deadMinions:
        return 0
    
    return deadMinions - csDiff




game_start = True

oldCS = int(get_cs())
oldMinions = 0
counter = 0
curCS = oldCS
missedCSCounter = 0



running = False
stop_flag = False

def run_script():
    global running, stop_flag

    oldCS = int(get_cs())
    oldMinions = 0
    counter = 0
    missedCSCounter = 0
    curCS = oldCS

    print("[Script started]")

    while running and not stop_flag and curCS < 300:
        time.sleep(2)

        curCS = int(get_cs())
        print("Current CS Count:", curCS)

        curMinions = get_livingMinions()
        print("Current Minions:", curMinions)

        missedCS = getMissedCS(oldMinions, curMinions, oldCS, curCS)
        missedCSCounter += missedCS

        if missedCS > 0:
            playsound(r".\audio_assets\pipe.mp3")

        print("Missed CS this cycle:", missedCS)
        print("Total missed CS:", missedCSCounter)

        oldCS = curCS
        oldMinions = curMinions
        counter += 1

    running = False
    print("[Script stopped]")

def start_script():
    global running
    if not running:
        running = True
        threading.Thread(target=run_script, daemon=True).start()

def stop_script():
    global running, stop_flag
    stop_flag = True
    running = False
    print("[Stop requested]")

def on_press(key):
    if key == keyboard.Key.f8:
        start_script()
    elif key == keyboard.Key.f9:
        stop_script()

def main():
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()

#print(get_cs())
#print(get_livingMinions())


