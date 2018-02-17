import socket
import os

def Main():
    host = '10.42.0.246'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = "ocr.pdf"
    filesize = str(os.path.getsize(filename))
    s.send(filename)
    resp = s.recv(1024)
    s.send(filesize)

    resp = s.recv(1024)

    if resp == "OKAY":
        with open(filename, 'rb') as f:
            bytesToSend = f.read(1024)
            s.send(bytesToSend)
            while bytesToSend != "":
                bytesToSend = f.read(1024)
                s.send(bytesToSend)


    # filename = raw_input("Filename? -> ")
    # if filename != 'q':
    #     s.send(filename)
    #     data = s.recv(1024)
    #     if data[:6] == 'EXISTS':
    #         filesize = long(data[6:])
    #         message = raw_input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
    #         if message == 'Y':
    #             s.send("OK")
    #             f = open('new_'+filename, 'wb')
    #             data = s.recv(1024)
    #             totalRecv = len(data)
    #             f.write(data)
    #             while totalRecv < filesize:
    #                 data = s.recv(1024)
    #                 totalRecv += len(data)
    #                 f.write(data)
    #                 print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
    #             print "Download Complete!"
    #             f.close()
    #     else:
    #         print "File Does Not Exist!"

    s.close()
    

if __name__ == '__main__':
    Main()




