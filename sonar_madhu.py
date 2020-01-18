import serial
import math
import rospy
import std_msgs.msg 
#import String
ser = serial.Serial('/dev/ttyACM0', baudrate=9600)
while True:
	try:
	    a=ser.readline()
	    p=a.split(" = ",2)
	    k=p[1]
	    g=k.split(" ",1)
	    l=g[0]
	    u=float(l)
	    
	    print("%.2f"%u)
	    print("\n")
	except(KeyboardInterrupt, SystemExit):
		ser.close()
		raise