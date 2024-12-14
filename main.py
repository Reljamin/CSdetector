import pyautogui
import time
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


pyautogui.position()
time.sleep(3)
print(pyautogui.position())
print(pyautogui.position())

im1 = pyautogui.screenshot('CSnum.png', region=(1779, 2, 33, 20))

imgRead = cv2.imread(r'C:\Users\Ariel\Documents\Code\Personal Projects\CSDetector\CSdetector\CSnum.png')

gray = cv2.cvtColor(imgRead, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray, config='--psm 7 -c tessedit_char_whitelist=0123456789')

print(text)