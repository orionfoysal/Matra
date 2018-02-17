import socket
import threading
import os

def RetrFile(name, sock):

    filename = sock.recv(1024)
    sock.send("OK")
    filesize = sock.recv(1024)

    filesize = int(float(filesize))

    # print filename
    print filesize

    sock.send("OKAY")

    f = open("new.pdf", "wb")
    data = sock.recv(1024)
    totalRecv = len(data)
    f.write(data)
    while totalRecv < filesize:
        data = sock.recv(1024)
        totalRecv += len(data)
        f.write(data)
        print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
    print "Download Complete!"
    f.close()
    
    # sock.send("OKA")


    # if os.path.isfile(filename):
    #     sock.send("EXISTS " + str(os.path.getsize(filename)))
    #     userResponse = sock.recv(1024)
    #     if userResponse[:2] == 'OK':
    #         with open(filename, 'rb') as f:
    #             bytesToSend = f.read(1024)
    #             sock.send(bytesToSend)
    #             while bytesToSend != "":
    #                 bytesToSend = f.read(1024)
    #                 sock.send(bytesToSend)
    # else:
    #     sock.send("ERR ")

    sock.close()

def Main():
    host = '10.42.0.246'
    port = 5000


    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print "Server Started."
    while True:
        c, addr = s.accept()
        print "client connedted ip:<" + str(addr) + ">"
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()
         
    s.close()

if __name__ == '__main__':
    Main()
