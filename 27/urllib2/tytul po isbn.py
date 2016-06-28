import urllib2
import androidhelper

droid = androidhelper.Android()


kodkreskowy = droid.scanBarcode()
isbn = int(kodkreskowy['result']['SCAN_RESULT'])
kod = urllib2.urlopen('http://katalogi.bn.org.pl/iii/encore/search/C__S' + isbn + '__Orightresult__U?lang=pol&suite=cobalt')

for line in kod:
    if 'onerror' in line:
        y = line.split('="')
        z = y[2].split('"')
        c = z[0].split(';')
        x = c[0].split('/')
        tytul = x[0] + x[1]
        print tytul

url = 'https://www.google.pl/search?q=chomikuj+' + tytul + '+pdf&ie=&oe='
droid.startAtivity('android.intent.action.VIEW', url)
