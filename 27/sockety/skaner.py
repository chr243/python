import socket
maska_sieci = '192.168.0.'


def skan(i):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.01)
        s.connect((maska_sieci + str(i), 135))
        ip = maska_sieci + str(i)
        print ip + ' - online:'
        skan_portow(ip)
    except:
        pass

def skan_portow(ip):
    for n in range(1,1024):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.01)
            s.connect((ip, n))
            print n
        except:
            pass


print 'Skanuje:'
for i in range(0,255):
    skan(i)
print 'Koniec skanowania.'
