

#required imports(panda, open cv, and motion)
import pandas
import cv2 
import time 
import datetime
# required imports for csv file and db
import csv
import sqlite3

back = None 
recordLogs = [ None, None ] # initialize the recording logs to a null value
time = [None] #initialize time var to a null value
dframe = pandas.DataFrame(columns = ["Start", "End"]) #End and start time columns assigned to data frame 
vid = cv2.VideoCapture(0)

connection = sqlite3.connect('MotionDetection.db')
contents = csv.reader("mvmtlog.csv")


while True: # loop takes in multiple images as a video
	
	check = video.read()
	frame = video.read() # initialze frame from video
	motion = 0 # initialize motion w a value of 0 to indicate no motion


	# image set to grayscale and gaussian blur to ensure that it is not difficult to find
	grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	grayScale = cv2.GaussianBlur(gray, (21, 21), 0)

	
	if back is None: # condition where back defined as gray if it is a null value
		back = gray
		continue

	
	difference = cv2.absdiff(back, gray)

	# shows white whenever there is a significant change in background
	thold = cv2.dilate(thold, None, iterations = 3)
	thold = cv2.threshold(diff_frame, 60, 255, cv2.THRESH_BINARY)[1] 
	cont = cv2.findContours(thold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for contour in cont:
		if cv2.contourArea(contour) < 800:
			continue
		motion = 1
		(x, y, w, h) = cv2.boundingRect(contour)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3) #moving object marked with a green rectangle

	#append used to mark motion status, start, and end
	recordLogs.append(motion)
	recordLogs = recordLogs[-2:]
	if recordLogs[-1] == 1 and recordLogs[-2] == 0:
		time.append(datetime.now())
	if recordLogs[-1] == 0 and recordLogs[-2] == 1:
		time.append(datetime.now())

	
	cv2.imshow("GrayScale", grayScale)#Displaying image in gray_scale
	cv2.imshow("Difference Frame", dframe) # shows difference bw current frame to the first frame
	cv2.imshow("Threshold Frame", thold) #if image intensity greater than 60 then show image

	
	key = cv2.waitKey(1)
	
	if key == ord('k'): 
		if motion == 1:
			time.append(datetime.now())
		break

# Appending time of motion in DataFrame
for i in range(0, len(time), 2):
	dframe = dframe.append({"Start":time[i], "End":time[i + 1]})

dframe.to_csv("mvmtlog.csv") #csv file to log times of movement
connection.close()
cv2.destroyAllWindows()
