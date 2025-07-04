import pytesseract as pyt

import cv2

img = cv2.imread("Text.png")
img2 = cv2.imread("text3.jpg")
img3 = cv2.imread("Text2.jpeg")
img4 = cv2.imread("Text4.jpg")

pyt.pytesseract.tesseract_cmd = "C:\\Users\\user\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

text = pyt.image_to_string(img)
text3 = pyt.image_to_string(img3)
text4 = pyt.image_to_string(img4)
"""text2 = pyt.image_to_string(img2)


#print(text)
print(text2)"""

print(text4)


#print(img3)