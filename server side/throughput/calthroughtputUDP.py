# The client performs one transfer of count*BUFSIZE bytes and
# measures the time it takes (roundtrip!).


import sys, time
from socket import *

MY_PORT = 8000
BUFSIZE = 1024


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
    print 'Usage:    (on host_A) throughput -s [port]'
    print 'and then: (on host_B) throughput -c count host_A [port]'
    sys.exit(2)


def server():
    if len(sys.argv) > 2:
        port = eval(sys.argv[2])
    else:
        port = MY_PORT
    s = socket(AF_INET, SOCK_DGRAM) #TCP_SOCK_STREAM_UDP_SOCK_DGRAM
    s.bind(('', port))
    #s.listen(1) tcp
    print 'Server ready...'
    while 1:
        #conn, (host, remoteport) = s.accept() tcp
        while 1:
            #data = conn.recv(BUFSIZE) tcp
	    data = s.recvfrom(BUFSIZE)
            if not data:
                break
            del data
        conn.send('OK\n')
        conn.close()
        print 'Done with', host, 'port', remoteport




main()
