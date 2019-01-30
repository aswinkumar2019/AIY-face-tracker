import picamera
from time import sleep
import re
from PIL import Image
import pytesseract
import cv2
import os
import tess_lib as ip
def processing(im):
     image = cv2.imread(im)
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     cv2.imshow("Image", gray)
     filename = "{}.png".format(os.getpid())
     cv2.imwrite(filename, gray)
     tb = cv2.imread(filename)
     clean = ip.cleanUpTextArea(tb)
     txt = ip.ocrImage(clean, extractBadChars=True, spellCheck=False)
     if txt == '':
         print('Sorry, I am unable to read the page.Please try again.')
     else:
         print(txt)
         print("Your wordlist")
     wordList = re.sub("[^\w]", " ",  txt).split()
     for x in wordList:
        print(x)
        print("Next Word")
     return wordList
def main():
     finalmark=0
     print("Enter the mark for this question")
     mark=int(input())
     print("Place the vision kit before the answer key")
     camera = picamera.PiCamera()
     camera.start_preview()
     sleep(5)
     camera.capture('image1.jpeg')
     print("Image captured")
     camera.stop_preview()
     key=processing("image1.jpeg")
     divide=len(key)
     each_mark=mark/divide
     print("Place the vision kit before the answer key")
     camera.start_preview()
     sleep(5)
     camera.capture('image2.jpeg')
     camera.stop_preview()
     print("Image Captured")
     answer=processing("image2.jpeg")
     for y in key:
         for z in answer:
             if y==z:
                   finalmark+=each_mark
     print("Your mark is")
     print(finalmark)
main()
