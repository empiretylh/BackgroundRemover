import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation 
import os 


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


import cv2

# Load the input image
img = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the face detector
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Crop the image for each detected face
for (x, y, w, h) in faces:
    # Crop the image using array slicing
    face_crop = img[y:y+h, x:x+w]
    # Display the cropped face image
    cv2.imshow("Face Crop", face_crop)
    cv2.waitKey(0)
    
# Close all windows
cv2.destroyAllWindows()
