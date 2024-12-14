import pyautogui
import time
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


pyautogui.position()
time.sleep(3)

im1 = pyautogui.screenshot(region=(1776, 2, 45,20))

image = np.array(im1)

image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresholded = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

cv2.imwrite("CSImgDebug.png", thresholded)

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(thresholded, config=custom_config)

print(f"Extracted Text: {text}")


if "112" in text:
    print("Found 112!")
else:
    print("loser")
