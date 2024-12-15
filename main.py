import pyautogui
import time
import cv2
import numpy as np
import pytesseract
from matplotlib import pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



def get_cs():
    pyautogui.position()
    time.sleep(3)
    print(pyautogui.position())
    print(pyautogui.position())

    im1 = pyautogui.screenshot('CSnum.png', region=(1779, 2, 33, 20))

    imgRead = cv2.imread('CSnum.png')

    gray = cv2.cvtColor(imgRead, cv2.COLOR_BGR2GRAY)
    colored = cv2.cvtColor(imgRead, cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(gray, config='--psm 7 -c tessedit_char_whitelist=0123456789')

    return text






def get_livingMinions():

    minionCounter = 0

    game_ss = pyautogui.screenshot('Game.png')
    game_img = cv2.imread('Game.png')
    game_img = cv2.cvtColor(game_img, cv2.COLOR_BGR2RGB)
    hpbar_img = cv2.imread('minionhpbar.png')
    hpbar_img = cv2.cvtColor(hpbar_img, cv2.COLOR_BGR2RGB)
    hpbar2_img = cv2.imread('lowhpbar.png')
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

    result = cv2.imwrite('result.png', game_img)
    result1 = cv2.imread('result.png')

    #plt.subplot(1, 1, 1)
    #plt.imshow(result1)
    #plt.show()

    return minionCounter

print(get_cs())
print(get_livingMinions())


"""
game_ss = pyautogui.screenshot('Game.png')
game_img = cv2.imread('Game.png')
game_img = cv2.cvtColor(game_img, cv2.COLOR_BGR2RGB)
hpbar_img = cv2.imread('minionhpbar.png')
hpbar_img = cv2.cvtColor(hpbar_img, cv2.COLOR_BGR2RGB)
hpbar2_img = cv2.imread('lowhpbar.png')
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

result = cv2.imwrite('result.png', game_img)
result1 = cv2.imread('result.png')

plt.subplot(1, 1, 1)
plt.imshow(result1)
plt.show()

print(minionCounter)

"""