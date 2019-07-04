# The client performs one transfer of count*BUFSIZE bytes and
# measures the time it takes (roundtrip!).


import sys, time
from socket import *

MY_PORT = 8000
BUFSIZE = 1024
period_of_time = [1,2,5,10,20,30,40,60,120,300]



def main():
    if len(sys.argv) < 2:
        usage()
    if sys.argv[1] == '-s':
        server()
    elif sys.argv[1] == '-c':
        client()
    else:
        usage()


def usage():
    sys.stdout = sys.stderr
    print 'Usage:    (on host_A) PDR -s [port]'
    print 'and then: (on host_B) PDR -c count host_A [port]'
    sys.exit(2)


def server():
    if len(sys.argv) > 2:
        port = eval(sys.argv[2])
    else:
        port = MY_PORT
    s = socket(AF_INET, SOCK_STREAM) #TCP_SOCK_STREAM_UDP_SOCK_DGRAM
    s.bind(('', port))
    host = "192.168.203.142"
    s.listen(1) #tcp
    print 'Server ready...'
    j=0
    name = host + " Local_TCP_PDR.txt"
    f= open(name,"w+")
    flag = 1
    while 1:
        conn, (host, remoteport) = s.accept() #tcp
	i=0
	while flag == 1:
		data = conn.recv(BUFSIZE)
		print data[0]
		if data[0] == "O": flag=0
	t1 = time.time()
        while 1:
            data = conn.recv(BUFSIZE) #tcp
	    #data = s.recvfrom(BUFSIZE)
	    if time.time() > t1 + period_of_time[j]: 
		break
            if not data:
                break
            del data
	    i = i+1
	t4 = time.time()
	msg = str(i) + ' time = '+str(t4-t1)
        conn.send(msg)
        conn.close()
        print 'Done with', host, 'port', remoteport
	f.write('PERIOD_OF_TIME = ' + str(period_of_time[j])+ '\n')
	j=j+1
	f.write('recieved:= ' + str(i) + '\n' + '\n')


def client():
    if len(sys.argv) < 4:
        usage()
    count = int(eval(sys.argv[2]))
    host = sys.argv[3]
    if len(sys.argv) > 4:
        port = eval(sys.argv[4])
    else:
        port = MY_PORT
    testdata = 'x' * (BUFSIZE-1) + '\n'
    t1 = time.time()
    s = socket(AF_INET, SOCK_STREAM)
    t2 = time.time()
    s.connect((host, port))
    t3 = time.time()
    i = 0
    while i < count:
        i = i+1
        s.send(testdata)
    s.shutdown(1) # Send EOF
    t4 = time.time()
    data = s.recv(BUFSIZE)
    t5 = time.time()
    print data
    print 'Raw timers:', t1, t2, t3, t4, t5
    print 'Intervals:', t2-t1, t3-t2, t4-t3, t5-t4
    print 'Total:', t5-t1
    print 'Throughput:', round((BUFSIZE*count*0.001) / (t5-t1), 3),
    print 'K/sec.'


main()
