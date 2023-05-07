import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation 
import numpy as np
# Load the input image
imgread = cv2.imread('img.jpg')

segmentor = SelfiSegmentation()
img = segmentor.removeBG(imgread,(255,0,0),threshold=0.7)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the face detector
face_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')


# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

if len(faces) > 0:
    # Calculate the center of the bounding box
    x, y, w, h = faces[0]
    center_x = x + w // 2
    center_y = y + h // 2
    
    # Calculate the width and height of the cropped image
    aspect_ratio = 1.1 / 1.3
    if w / h > aspect_ratio:
        crop_width = int(aspect_ratio * h)
        crop_height = h
    else:
        crop_width = w
        crop_height = int(w / aspect_ratio)
        
    # Calculate the coordinates of the top-left corner of the cropped image
    margin_x = crop_width // 2
    margin_y = crop_height // 2
    crop_x = max(0, center_x - crop_width // 2 - margin_x)
    crop_y = max(0, center_y - crop_height // 2 - margin_y)

    # Crop the image
    crop_img = img[crop_y:crop_y+crop_height+margin_y*2, crop_x:crop_x+crop_width+margin_x*2]
   
    # Resize the cropped image to the desired size
    resize_img = cv2.resize(crop_img, (int(210/3), int(297/3)), interpolation = cv2.INTER_AREA)
    
    # Add border to the resized image to create a margin
    margin = 30
    bordered_img = cv2.copyMakeBorder(resize_img, margin, margin, margin, margin, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    
    # Add the six cropped images to an A4 sheet
    a4_sheet = np.zeros((int(297), int(210), 3), np.uint8)
    for i in range(2):
        for j in range(3):
            x_offset = j * (bordered_img.shape[1] + 20) + 20
            y_offset = i * (bordered_img.shape[0] + 20) + 20
            a4_sheet[y_offset:y_offset+bordered_img.shape[0], x_offset:x_offset+bordered_img.shape[1]] = bordered_img
            
    cv2.imwrite('output.jpg',a4_sheet)
    

# Close all windows
cv2.destroyAllWindows()
