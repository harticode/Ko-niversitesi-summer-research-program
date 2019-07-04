from socket import *
import time
from datetime import datetime

#s = socket.socket() #Creates an instance of socket
port = 8000 #Port to host server on
maxConnections = 999
IP = gethostname() #IP address of local machine

s = socket(AF_INET, SOCK_DGRAM) #TCP_SOCK_STREAM_UDP_SOCK_DGRAM
s.bind(('', port))
#s.listen(1)

print("Server started at " + IP + " on port " + str(port))

#Accepts the incomming connection
#conn, (host, remoteport) = s.accept()
print("New connection made!")

running = True
for i in range(0,11):
	#Accepts the incomming connection
	running = True
	while running:
	    data, address = s.recvfrom(1024) #Gets the incomming message
	    word = "T"*pow(2,i)
	    if data == word:
	    	#t2 = time.time()
		dt2 = datetime.now()
		print(i)
		print(dt2)
		s.sendto(str(dt2) , address)
		break
	    #print(data)


        
