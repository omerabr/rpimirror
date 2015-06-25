#!/usr/bin/python

# Import the required modules
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2, os
import numpy as np
from PIL import Image

# For face detection we will use the Haar Cascade provided by OpenCV.
#cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For face recognition we will the the LBPH Face Recognizer 
recognizer = cv2.createLBPHFaceRecognizer()

def get_images_and_labels(path):
    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
    #image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.sad')]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    faceName = raw_input('What is your name?')
    labels = []
    count = 0
    
    while (count < 10):
		camera = PiCamera()
		camera.resolution = (300, 200)
		camera.framerate = 32
							
		camera.start_preview()
		
		time.sleep(1)
		camera.capture(path+faceName+"_"+str(count)+".jpg")
		camera.close()
		count = count + 1
		

    image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.sad')]
    print image_paths
    
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image
        nbr = int(image_path.split("/")[6][0])
        # Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)
    # return the images list and labels list
    return images, labels

# Path to the Yale Dataset
path = '/home/pi/tempRecognizer/face_recognizer/faces/'
# Call the get_images_and_labels function and get the face images and the 
# corresponding labels
images, labels = get_images_and_labels(path)
print labels
cv2.destroyAllWindows()

# Perform the tranining
recognizer.train(images, np.array(labels))
recognizer.save('/home/pi/tempRecognizer/train.xml')
