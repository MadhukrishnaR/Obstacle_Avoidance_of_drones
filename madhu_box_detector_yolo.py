#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os
import sys
import rospy as rospy
import roslib
#roslib.load_manifest('stereo_cam')
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
#from scipy.ndImage import filters
#import cv2
#import sys
from cv_bridge import CvBridge,CvBridgeError
import cv_bridge
import numpy as np
global po 
po=0
# In[2]:
class img_conv:
	def __init__(self):
		#self.image_pub=rospy.Publisher('img_topic2',Image,queue_size=1)
		self.bridge=CvBridge()
		self.image_sub=rospy.Subscriber("/left/image_raw",Image,self.callback1)
		#self.subscriber=rospy.Subscriber('/right/image_raw',Image,self.callback(),queue_size=1)
	def  callback1(self,data):
		#rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
		print ("lll")
		global po
		try: 
			cv_image=self.bridge.imgmsg_to_cv2(data,"bgr8")
		except CvBridgeError as e:
			print(e)
		(rows,cols,channels)=cv_image.shape
		if cols>60 and rows >60:
			cv2.circle(cv_image,(50,50),10,255)

#im0 = os.path.join(os.path.expanduser('~'),'test2','frame0119.jpg')
#image=cv2.imread(os.path.join(os.path.expanduser('~'),'Downloads','IMG20200107182036.jpg'))
#image=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
		bbox,label,conf=cv.detect_common_objects(cv_image)
		print(bbox,label,conf)
		out=draw_bbox(image,bbox,label,conf)
		cv2.imwrite(os.path.join(os.path.expanduser('~'),'Desktop','test5','t%d.bmp'%po),out)
		cv2.imshow("object",out)
		po=po+1
#cv2.waitKey()

#cv2.destroyAllWindows()
def main(args):
	img=img_conv()
	rospy.init_node('img',anonymous=True)
	#left_raw_image=rospy.Subscriber('/left/image_raw',Image,self.callback_left())
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print ("shut down")
	cv2.destroyAllWindows()
		
if __name__=='__main__':
	main(sys.argv)
	




