

#required imports(panda, open cv, and motion)
import pandas, time
import cv2 
from datetime import datetime
# required imports for csv file and db
import csv
import sqlite3
from SQLConnection import SQLConn



back = None 

vid = cv2.VideoCapture("detectionApp/vtest.avi")

# vid = cv2.VideoCapture(0)
if not (vid.isOpened()):
	print("Could not open camera")


recordLogs = [ -1, -1 ] # initialize the recording logs to a null value
time = [] #initialize time var to a null value
dframe = pandas.DataFrame(columns = ["Start", "End"]) #End and start time columns assigned to data frame 

# cur = SQLConn.connectToSQL()
contents = csv.reader("mvmtlog.csv")


while True: # loop takes in multiple images as a video
	
	check, frame = vid.read()
	motion = 0 # initialize motion w a value of 0 to indicate no motion


	# image set to grayscale and gaussian blur to ensure that it is not difficult to find
	grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	grayScale = cv2.GaussianBlur(grayScale, (21, 21), 0)

	
	if back is None: # condition where back defined as gray if it is a null value
		back = grayScale
		continue

	
	difference = cv2.absdiff(back, grayScale)

	# shows white whenever there is a significant change in background
	thold = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)[1] 
	thold = cv2.dilate(thold, None, iterations = 2)


	(cont,_) = cv2.findContours(thold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for contour in cont:
		if cv2.contourArea(contour) < 10000:
			continue
		motion = 1
		(x, y, w, h) = cv2.boundingRect(contour)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3) #moving object marked with a green rectangle

	#append used to mark motion status, start, and end
	recordLogs.append(motion)
	if (recordLogs[-1]*recordLogs[-2])==-1:
		time.append(datetime.now())



	# cv2.imshow("GrayScale", grayScale)#Displaying image in gray_scale
	# cv2.imshow("Difference Frame", dframe) # shows difference bw current frame to the first frame
	# cv2.imshow("Threshold Frame", thold) #if image intensity greater than 60 then show image

	cv2.imshow("Color Frame: ", frame)
	
	key = cv2.waitKey(1)
	
	if key == ord('q'): 
		if motion == 1:
			time.append(datetime.now())
		break

# Appending time of motion in DataFrame
for i in range(0, len(time), 2):
	dframe = dframe.append({"Start":time[i], "End":time[i + 1]})

print(dframe)

dframe.to_csv("mvmtlog.csv") #csv file to log times of movement


SQLConn.closeConnection(cur)
cv2.destroyAllWindows()
