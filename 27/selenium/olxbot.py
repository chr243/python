from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


fantom = 'path/to/phantomjs.exe'

def kradnij(strona):
    driver = webdriver.PhantomJS(fantom, service_args=['--load-images=no'])
    driver.set_window_size(1024, 768)
    driver.get("https://olx.pl/praca/?page=" + str(strona))
    ogloszenie = 2
    while 1:
        try:
            driver.find_element_by_xpath('//tbody/tr[' + str(ogloszenie) + ']/td/article/div[1]/h3/a/strong').click()
        except:
            print 'Pomijam ogloszenie.'
        try:
            driver.find_element_by_xpath('//*[@id="contact_methods"]/li').click()
            time.sleep(5)
            numer = driver.find_element_by_xpath('//*[@id="contact_methods"]/li').text
            kategoria = driver.find_element_by_xpath('//tbody/tr/td[2]/ul/li[3]/a').text
            nazwaogloszenia = driver.find_element_by_xpath('//div[1]/div[1]/div[1]/div[1]/h1').text
            lokalizacja = driver.find_element_by_xpath('//div[1]/div[1]/div[1]/div[1]/p/span/span[2]/strong').text
            imie = driver.find_element_by_xpath('//div[1]/div[2]/p/span[1]').text
            numer = driver.find_element_by_xpath('//*[@id="contact_methods"]/li').text
            wpis = imie + ' ### ' + numer + ' ### ' + lokalizacja + ' ### ' + kategoria + ' ### ' + nazwaogloszenia
            print str(wpis)
            try:
                db = open('bazaolx', 'w')
                db.write(wpis)
                db.close()
                print 'ok'
            except:
                print 'problem z zapisywaniem'
        except:
            print 'Brak numeru, lece dalej\n'
            #driver.save_screenshot('screen.png')
        if ogloszenie >= 43:
            ogloszenie = 2
            strona += 1
            print 'Zmiana strony.'
            driver.get('http://olx.pl/praca/?page=' + str(strona))
        else:
            ogloszenie += 1
            driver.back()


kradnij(4)
