import numpy as np
import cv2
import os
cap=cv2.VideoCapture(0)

while True:
	#ret,frame =cap.read()
	#frame_gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	ret,old_frame =cap.read()
	old_gray=cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
	ret,bw=cv2.threshold(old_gray,128,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	connect=10
	nb_components,output,stats,cent=cv2.connectedComponentsWithStats(bw,connect,cv2.CV_32S)
	cv2.imshow('result',output)
	sizes=stats[1:, -1]
	nb_components=nb_components-1
	min_size=250
	img2=np.zeros((old_frame.shape),np.uint8)
	for i in range(0,nb_components+1):
		color= np.random.randint(255,size=3)
		cv2.rectangle(img2,(stats[i][0],stats[i][1],stats[i][2],stats[i][3]),(0,255,0),2)
		img2[output == i+1] =color
		
