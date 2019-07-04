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
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    print 'Server ready...'
    while 1:
        conn, (host, remoteport) = s.accept()
        while 1:
            data = conn.recv(BUFSIZE)
            if not data:
                break
            del data
        conn.send('OK\n')
        conn.close()
        print 'Done with', host, 'port', remoteport


def client():
    if len(sys.argv) < 4:
        usage()
    count = int(eval(sys.argv[2]))
    host = sys.argv[3]
    if len(sys.argv) > 4:
        port = eval(sys.argv[4])
    else:
        port = MY_PORT
    name = host + " UDP_PDR.txt"
    f= open(name,"w+")
    for PERIOD_OF_TIME in period_of_time:
	    testdata = 'x' * (BUFSIZE-22) + '\n'
	    t1 = time.time()
	    s = socket(AF_INET, SOCK_DGRAM) #TCP SOCK_STREAM UDP SOCK_DGRAM
	    t2 = time.time()
	    s.connect((host, port))
	    s.sendto("O", (host, port))
	    #time.sleep(0.001)
	    t3 = time.time()
	    i = 0
	    while 1:
            if time.time() >= t3 + PERIOD_OF_TIME : break
            s.sendto(testdata, (host, port))
            #s.sendto(testdata)
            i = i+1
	    s.shutdown(1) # Send EOF
	    t4 = time.time()
	    #data = s.recvfrom(BUFSIZE)
	    t5 = time.time()
        f.write('PERIOD_OF_TIME = ' + str(PERIOD_OF_TIME)+ '\n')
	    f.write('Total:' + str(t4-t3) + " is equal to PERIOD_OF_TIME= " + str(PERIOD_OF_TIME) + '\n')
	    f.write('sent:= ' + str(i) + '\n' + '\n')
	    #print data
	    print 'Raw timers:', t1, t2, t3, t4, t5
	    print 'Intervals:', t2-t1, t3-t2, t4-t3, t5-t4
	    print 'Total:', t4-t1, "is equal to PERIOD_OF_TIME= ", PERIOD_OF_TIME
	    print 'sent:= ',str(i),'\n' + '\n'
	    
    f.close()


main()
