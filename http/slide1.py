
import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com',80))

mysock.send('GET http://py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    gotdata=mysock.recv(512)
    if len(gotdata) < 1:
        break
    print gotdata

mysock.close()
