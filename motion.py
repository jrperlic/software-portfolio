from imutils.video import VideoStream
import datetime
import imutils
import time
import cv2 as cv

capture = cv.VideoCapture("1.mp4") # filename
firstFrame = None

while True:
	frame = capture.read()
	frame = frame[1]
	if frame is None:
		break
	frame = imutils.resize(frame,width=500)
	gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
	gray = cv.GaussianBlur(gray,(21,21),0)
	if firstFrame is None:
		firstFrame = gray
		continue
	frameDelta = cv.absdiff(firstFrame,gray)
	thresh = cv.threshold(frameDelta,25,255,cv.THRESH_BINARY)[1]
	thresh = cv.dilate(thresh,None,iterations=2)
	cnts = cv.findContours(thresh.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	for c in cnts:
		if cv.contourArea(c) < 1500:
			continue
		(x,y,w,h) = cv.boundingRect(c)
		cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
	cv.imshow("Feed",frame)
	key = cv.waitKey(1)
	if key == ord("q"):
		break

capture.release()
cv.destroyAllWindows()