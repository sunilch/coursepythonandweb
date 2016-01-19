
import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

url=raw_input('Enter connecting url- ')
#url='www.google.com'
print 'connecting to ',url
mysock.connect((url,80))

mypage=raw_input('Enter the page to send- ')
mysend='GET http://'+url.rstrip('/')+'/'+mypage.lstrip('/')+' HTTP/2.0\n\n'
print 'requesting - ',mysend
mysock.send(mysend)

while True:
    gotdata=mysock.recv(512)
    if len(gotdata) < 1:
        break
    print gotdata

mysock.close()
