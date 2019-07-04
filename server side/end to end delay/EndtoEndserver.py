from socket import *
import time
from datetime import datetime

#s = socket.socket() #Creates an instance of socket
port = 8000 #Port to host server on
maxConnections = 999
IP = gethostname() #IP address of local machine
s = socket() #TCP_SOCK_STREAM_UDP_SOCK_DGRAM
s.bind(('', port))
s.listen(1)
print("Server started at " + IP + " on port " + str(port))
for i in range(0,11):
	#Accepts the incomming connection
	conn, (host, remoteport) = s.accept()
	print("New connection made!", host)
	running = True
	while running:
	    data = conn.recv(1024) #Gets the incomming message
	    word = "T"*pow(2,i)
	    if data == word:
	    	#t2 = time.time()
		dt2 = datetime.now()
		print(i)
		print(dt2)
		conn.send(str(dt2))
		conn.close()
		break
	    #print(data)
        
