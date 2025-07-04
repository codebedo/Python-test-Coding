import pytesseract as pyt

import cv2

img = cv2.imread("Text.png")

pyt.pytesseract.tesseract_cmd = "C:\\Users\\user\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

text = pyt.image_to_string(img)

print(text)