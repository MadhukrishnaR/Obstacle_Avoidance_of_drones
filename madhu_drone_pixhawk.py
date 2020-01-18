from dronekit import connect,VehicleMode
import time
import pymavlink
import os
file1=open(os.path.join(os.path.expanduser('~'),'Desktop','madhu_s','m.xls'),"a+")
vehicle = connect('/dev/ttyUSB0', wait_ready=True, baud=57600)
while True:
	print("-----Connecting with pixhawk")
	#vehicle=connect(connection_string,wait_ready=True)
	#vehicle = connect('127.0.0.1:14550', wait_ready=True)
	
	#vehicle.wait_ready('autopilot version')
	#print('Autopilot version:%s'%vehicle.version)
	print('Velocity:%s'%vehicle.velocity)
	a=vehicle.velocity
	file1.write(str(a)+str('\n'))
	
