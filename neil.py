import pyautogui
import time
import cv2
import numpy as np
import pytesseract





def check_cs():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    pyautogui.position()

    cs = pyautogui.screenshot(region=(1776, 2, 45,20))

    image = np.array(cs)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresholded = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

    cv2.imwrite("CSImgDebug.png", thresholded)

    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(thresholded, config=custom_config)

    
    return text

def minion_counter():

    minionCounter = 0

    im1 = pyautogui.screenshot('Game.png')
    im2 = cv2.imread('Game.png')
    im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)
    im3 = cv2.imread('health_bar.png')
    im3 = cv2.cvtColor(im3, cv2.COLOR_BGR2RGB)
    im4 = cv2.imread('lowhpbar.png')
    im4 = cv2.cvtColor(im4, cv2.COLOR_BGR2RGB)

    result = cv2.matchTemplate(im2, im3, cv2.TM_CCOEFF_NORMED)
    result2 = cv2.matchTemplate(im2, im4, cv2.TM_CCOEFF_NORMED)

    threshold = 0.98
    threshold2 = 0.98

    locations = np.where(result >= threshold)
    locations2 = np.where(result2 >= threshold2)

    for pt in zip(*locations[::-1]):
        
        minionCounter += 1
    for pt in zip(*locations2[::-1]):
        
        minionCounter += 1

    return minionCounter

print(check_cs())
print(minion_counter())
