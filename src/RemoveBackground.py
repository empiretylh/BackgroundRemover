import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
# Load the input image
from PaperLayout import GeneratePhoto
class RemoveBackground():

   #images will be array
    def __init__(self,images,aspect_ratio,rgb,output_di):
        self.images = images
        self.aspect_ratio = aspect_ratio
        self.rgb = rgb
        self.output_di = output_di

      
    def remove(self):       
        aspect_ratio = self.aspect_ratio

        for i in self.images:
            print(i)
            imgread = cv2.imread(i[0])

            segmentor = SelfiSegmentation()
            rgb = (255,0,0)
            img = segmentor.removeBG(imgread,rgb,threshold=0.9)

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
            
            cv2.imwrite(self.output_di+i[0],crop_img)
            