#Imports library
import socket

#Creates instance of 'Socket'
su = socket.socket()

hostname ='192.168.203.134' #'35.202.79.35' #Server IP/Hostname
port = 8000 #Server Port

su.connect((hostname,port)) #Connects to server

while True:
    x = raw_input("Enter message: ") #Gets the message to be sent
    su.send(x.encode()) #Encodes and sends message (x)
