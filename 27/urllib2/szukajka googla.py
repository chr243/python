import urllib2

headers = {'User-agent' : 'Mozilla/5.0'}
req = urllib2.Request('https://www.google.pl/search?q=chomikuj+otchlan+pdf&ie=&oe=', None, headers)
html = urllib2.urlopen(req).read()
with open('pliknowy.txt', 'a') as plik:
    for line in html:
        plik.write(line)
'''
%3Dcache <- po tym jest link do chomika
'''
