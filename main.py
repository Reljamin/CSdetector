import pyautogui
import time
import cv2
import numpy as np
import pytesseract
from matplotlib import pyplot as plt
from playsound import playsound
import os
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

    w, h = hpbar_img.shape[:-1]

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

while counter < 3 and curCS < 300:
    time.sleep(2)


    #print("old CS Count: " + str(oldCS))
    #print("old Minions: " + str(oldMinions))

    curCS = int(get_cs())
    print("Current CS Count: " + str(curCS))
    curMinions = get_livingMinions()
    print("current Minions: " + str(curMinions))
    missedCS = getMissedCS(oldMinions, curMinions, oldCS, curCS)
    missedCSCounter += missedCS

    print("Missed CS Count: " + str(missedCS))

    oldCS = curCS
    oldMinions = curMinions

    if missedCS > 0:
        playsound(r".\audio_assets\pipe.mp3")


    print("Total missed CS Count: " + str(missedCSCounter))
    counter += 1
    

    






#print(get_cs())
#print(get_livingMinions())


