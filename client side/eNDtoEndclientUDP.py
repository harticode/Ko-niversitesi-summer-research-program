#Imports library
from socket import *
import time
from datetime import datetime
f= open("EndtoENDUDP_Local.txt","w+")
for i in range(0,11):
	#Creates instance of 'Socket'
	s = socket(AF_INET, SOCK_DGRAM)
	hostname = '192.168.203.141'#'35.202.79.35'# Server IP/Hostname
	port = 8000 #Server Port
	s.connect((hostname,port)) #Connects to server
	#t1 = time.time()
	dt1 = datetime.now()
	print(dt1)		
	size = "T"*pow(2,i)
	s.send(size)
	t2, adrr = s.recvfrom(1024)
	print type(t2)
	dt = datetime.strptime(t2, '%Y-%m-%d %H:%M:%S.%f')
	print(t2)
	print 'time = '+ str(dt-dt1)
	f.write('data = ' + str(pow(2,i)) + ' time = '+ str(dt-dt1) + '\n')
	s.close()
f.close()


