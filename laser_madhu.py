import serial
import math
import rospy
from std_msgs.msg import Float32
#import String
import Num
ser = serial.Serial('/dev/ttyUSB0', baudrate=115200)
l=[]
#def talker():
#	pub=rospy.Publisher('chatter',float32,queue_size=10)
#	rospy.init_node(talker',anonymous=True)
#	rate=rospy.Rate(10)
#	while not rospy.is_shutdown():
#		op=u
#		rospy.loginfo(op)
#		pub.publish(op)
#		rate.sleep()
if __name__=='__main__':		
	try:
		try:
			i=3	
			#for i in range(128):
			a=ser.readline()
			#k=a[0].decode('utf')
			#	f=str(k)
			#	g=l.append(f);
			
			#l=float(k)	
		
			p=a.split("  ",2)
			k=p[1]
			g=k.split(" ")
			l=g[1]
			u=float(l)
		       
			pub=rospy.Publisher('Num',Num,queue_size=10)
			rospy.init_node('talker',anonymous=True)
			rate=rospy.Rate(10)
			msg=Num()
			msg.num=u
			while not rospy.is_shutdown():
				#op=u
				rospy.loginfo(msg)
				pub.publish(msg)
				rate.sleep()
			
			print("%.2f"%u)
			print("\n")
		except(KeyboardInterrupt, SystemExit):
			ser.close()
			raise
	except rospy.ROSInterruptExcepton:
		pass 
			
			
		