import socket
import SendKeys

password = 'aaa'
host = ''
port = 8122

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print 'running'

while 1:
    client, address = s.accept()
    data = client.recv(1024)
    if data.split(' ')[0] == password:
        print data.split(' ')[1:]
