from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import cv2
import io
from PIL import Image


def face_rec(stream):
	if len(stream)<1:
		print 'NO Found'
		return False
	#gray = cv2.cvtColor(stream, cv2.COLOR_BGR2GRAY)
	image_to_predict = stream
	predict_image_pil = cv2.cvtColor(image_to_predict, cv2.COLOR_BGR2GRAY)
	#predict_image_pil = cv2.imread(image_to_predict, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	#predict_image_pil = Image.open(image_to_predict).convert('L')
	predict_image = np.array(predict_image_pil, 'uint8')
	#faces = face_cascade.detectMultiScale(predict_image)
	faces = face_cascade.detectMultiScale(predict_image)
	if len(faces) > 0:
		print 'found face'
		for (x, y, w, h) in faces:
			nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
			if (nbr_predicted == 0):
				nbr_predicted = "omer"
			else:
				if (nbr_predicted == 2):
					nbr_predicted = "tzahit"
			print "{} is Correctly Recognized with confidence {}".format(nbr_predicted, conf)
			

if __name__ == "__main__":
	# initialize the camera and grab a reference to the raw camera capture
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	recognizer = cv2.createLBPHFaceRecognizer()
	recognizer.load('/home/pi/tempRecognizer/train.xml')
	


	camera = PiCamera()
	camera.resolution = (300, 200)
	camera.preview_fullscreen=False 
	camera.preview_window=(620, 320, 640, 480) 
	camera.framerate = 32
	rawCapture = PiRGBArray(camera, size=(300, 200))

	# allow the camera to warmup
	time.sleep(3)

	camera.start_preview()
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
		#cv2.imshow("Frame", image)
		
		#camera.preview()
		key = cv2.waitKey(1) & 0xFF
		#face_detect(image)
		face_rec(image)
		# clear the stream in preparation for the next frame
		rawCapture.truncate(0)
		#end = time.time()
		#print end - start
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break
