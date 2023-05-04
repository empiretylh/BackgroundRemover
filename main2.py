import cv2

# Load the input image
img = cv2.imread('img.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the face detector
face_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')


# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Crop the image for each detected face
for (x, y, w, h) in faces:
    # Crop the image using array slicing
    print('x : ',x,y,w,h)
    face_crop = img[y:y+h+1000, x:x+w+1000]
    # Display the cropped face image
    cv2.imshow("Face Crop", face_crop)
    cv2.waitKey(0)
    
# Close all windows
cv2.destroyAllWindows()
