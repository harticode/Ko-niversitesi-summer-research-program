# The client performs one transfer of count*BUFSIZE bytes and
# measures the time it takes (roundtrip!).


import sys, time
from socket import *

MY_PORT = 8000
BUFSIZE = 1024 #bytes
period_of_time = [1,2,5,10,20,30,40,60,120,300] #in seconds



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
    print 'and then: (on host_B) PDR -c count host_A [port]' # give the count 0
    sys.exit(2)



def client():
    if len(sys.argv) < 4:
        usage()
    count = int(eval(sys.argv[2]))
    host = sys.argv[3]
    if len(sys.argv) > 4:
        port = eval(sys.argv[4])
    else:
        port = MY_PORT
    name = host + " TCP_PDR.txt"
    f= open(name,"w+")
    for PERIOD_OF_TIME in period_of_time:
        testdata = 'x' * (BUFSIZE-22) + '\n'
        print "test data is = "
        print sys.getsizeof(testdata) #to be sure we send 1024bytes 
        print " lock up \n"
        t1 = time.time()
        s = socket(AF_INET, SOCK_STREAM) #TCP SOCK_STREAM UDP SOCK_DGRAM
        t2 = time.time()
        s.connect((host, port))
        s.send("O")
        #time.sleep(5)
        t3 = time.time()
        i = 0
        while 1:
            if time.time() >= t3 + PERIOD_OF_TIME : break
            #s.sendto(testdata, (host, port))
            s.send(testdata)
            i = i+1
        t4 = time.time()
        data = conn.recv(BUFSIZE)
        t5 = time.time()
        f.write('PERIOD_OF_TIME = ' + str(PERIOD_OF_TIME)+ '\n')
        f.write('Total:' + str(t3-t1) + " is equal to PERIOD_OF_TIME= " + str(PERIOD_OF_TIME) + '\n')
        f.write('sent:= ' + str(i) + 'recieved:= ' + '\n' + '\n')
        print data
        print 'Raw timers:', t1, t2, t3, t4, t5
        print 'Intervals:', t2-t1, t3-t2, t4-t3, t5-t4
        print 'Total:', t4-t1, "is equal to PERIOD_OF_TIME= ", PERIOD_OF_TIME
        print 'sent:= ', str(i) , '   recieved:= '

    f.close()


main()
