import cv2

# Load the image
img = cv2.imread('processed_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create face and shoulder detector objects
face_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
shoulder_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_upperbody.xml')

# Detect faces and shoulders in the grayscale image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
shoulders = shoulder_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around the detected faces and shoulders
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
for (x, y, w, h) in shoulders:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

print(len(shoulders))
# Crop the image using the coordinates of the detected face and shoulders
if len(faces) > 0 and len(shoulders) > 0:
    x, y, w, h = faces[0]
    x1, y1, w1, h1 = shoulders[0]
    crop_img = img[y:y+h1, x:x+w]
    cv2.imwrite('cropimage.jpg',crop_img)
else:
    print('Not Generated')
# Display the image with the detected objects
cv2.imwrite('detectimage.jpg', img)
