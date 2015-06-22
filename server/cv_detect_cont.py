from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import cv2

def face_detect(image):
	#print image
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
	
	#print image
	#img = cv2.imread(image)
	#img = cv2.imread('1.png')
	if len(image)<1:
		print 'NO Found'
		return False
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 3)

	#print len(faces)
	if len(faces) > 0:
		#for (x,y,w,h) in faces:
			#img2 = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			#~ roi_gray = gray[y:y+h, x:x+w]
			#~ roi_color = img[y:y+h, x:x+w]
			#~ eyes = eye_cascade.detectMultiScale(roi_gray)
			#~ for (ex,ey,ew,eh) in eyes:
			#~ cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		print 'found face'
		cv2.imwrite( "/var/www/tempFace/temp.jpg", image )
		dd = input("enter...")
		return True
	else:
		print 'NO face'
		return False
	#cv2.imshow('img',img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()




if __name__ == "__main__":
	# initialize the camera and grab a reference to the raw camera capture
	camera = PiCamera()
	camera.resolution = (300, 200)
	camera.framerate = 32
	rawCapture = PiRGBArray(camera, size=(300, 200))

	# allow the camera to warmup
	time.sleep(3)

	# capture frames from the camera
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		# grab the raw NumPy array representing the image, then initialize the timestamp
		# and occupied/unoccupied text
		#start = time.time()
		image = frame.array
		
		#print type(image)
		#image2 = cv2.imdecode(data, 1)
		#print image2
		# show the frame
		cv2.imshow("Frame", image)
		key = cv2.waitKey(1) & 0xFF
		face_detect(image)
		# clear the stream in preparation for the next frame
		rawCapture.truncate(0)
		#end = time.time()
		#print end - start
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break
