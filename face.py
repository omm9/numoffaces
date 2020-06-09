#!/usr/bin/python3
import io
import picamera
import cv2
import numpy

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.capture(stream, format='jpeg')

        #Convert the picture into a numpy array
        buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

        #Now creates an OpenCV image
        image = cv2.imdecode(buff, 1)
        cv2.imwrite('/home/pi/git/facedetect/orig.jpg',image)

        #Load a cascade file for detecting faces
        face_cascade = cv2.CascadeClassifier('/home/pi/opencv-4.1.0/data/haarcascades/haarcascade_frontalface_alt.xml')

        #Convert to grayscale
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imwrite('/home/pi/git/facedetect/gray.jpg',gray)

        #Look for faces in the image using the loaded cascade file
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        print("Found " +str(len(faces))+ " face(s)")

         #Draw a rectangle around every found face
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

            #Save the result image
            cv2.imwrite('result.jpg',image)
            cv2.imwrite('/home/pi/git/facedetect/result.jpg',image)
