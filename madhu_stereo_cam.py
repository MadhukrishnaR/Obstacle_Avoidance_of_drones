#!/usr/bin/env python
import rospy
#roslib.load_manifest('stereo_cam')
import roslib
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
#from scipy.ndImage import filters
import cv2
from cv_bridge import CvBridge,CvBridgeError
k=False
class img_conv:
	def __init__(self):
		self.image_pub=rospy.Publisher('img_topic2',Image)
		self.bridge=CvBridge()
		self.subscriber=rospy.Subscriber('/left/image_raw',Image,self.callback(),queue_size=1)
		#if k:
		#	print "subscribed to /left/image_raw"
	def callback(self,rawdata):
		#rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
		print ("lll")
		try: 
			cv_image=self.bridge.imgmsg_to_cv2(rawdata,"bgr8")
		except CvBridgeError as e:
			print(e)
		(rows,cols,channels)=cv_image.shape
		if cols>60 and rows >60:
			cv2.circle(cv_image,(50,50),10,255)
		cv2.imshow("Image window",cv_image)
		cv2.waitKey(3)
		try:
			self.image_pub.publish(self.bridge.imgmsg_to_cv2_to_imgmsg(cv_image,"bgr8"))
		except CvBridgeError as e:
			print(e)
		#if k:
		#	print 'received image type : %s'%ros_data.format
		#np_arr =np.fromstring(ros_data.data,np.uint8)
		#image_np=cv2.imdecode(np_arr,cv2.CV_LOAD_IMAGE_COLOR)
		#method='GridFAST'
	#	feat_det=cv2.FeatureDetector_create(method)
	#	time1=time.time
	#	featpoints=feat.feat_det.detect(cv2.cvtColor(image_np,cv2.COLOR_BGR2GRAY))
	#	time2=time.time()
	#	if k:
	#		print' %s detector found:%s points  in: %s sec'%(method,len(featpoints),time2-time1)
	#	for featpoint in featpoints:
	#		x,y=featpoint.pt
	#		cv2.circle(image_np,(int(x),int(y)),3,(0.0.255),-1)
	#	cv2.imshow('cv_img',image_np)
	#	cv2.waitKey(2)
	#	msg=Image()
	#	msg.header.stamp=rospy.Time.now()
	#	msg.format='jpeg'
	#	msg.data=np.array(cv2.imencode('.jpg',image_np)[1]).tostring()
		
def main(args):
	ic=img_conv()
	rospy.init_node('img_conv',anonymous=True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print ("shut down")
	cv2.destroyAllWindows()
		
if __name=='__main__':
	main(sys.argv)
	

