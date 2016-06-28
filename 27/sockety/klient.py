import socket
import SendKeys


host = '127.0.0.1'
port = 8118

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
s.send('aaa bbb ccc')
print 'Wyslano'
