import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation 
import os 
from paper import GeneratePhoto

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()
width = 640
height = 480

img = cv2.imread('img.jpg')

imgOut = segmentor.removeBG(img,(255,0,0),threshold=0.7)

cv2.imwrite('processed_image.jpg', imgOut)

