import time
import csv
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup

# all my imports are above
driver = webdriver.Chrome('/Users/Claudia/Documents/AAAUF_SPRING_19/Adv.Web_Apps/python/scraping_proj/chromedriver')
driver.get('http://oldweb.circuit8.org/inmatelist.php');

time.sleep(3)
#the line below
html = driver.page_source

booknum = []

soup = BeautifulSoup(html, "html.parser")
html = soup.find('table')
#print(html) #this is just to test
with open("bookings.csv", 'a') as f:
    w = csv.writer(f)
    w.writerows(zip(["inmate_name"],["pod"], ["booking_date"],['mni'],["inmate_details"],["inmate_mug"],["bookno"]))

    url = "http://oldweb.circuit8.org"

    for tr in soup.findAll('tr')[1:]:
        name = tr.findAll('td')[0]
        #print(name) #this is a check

        for link in name:
            href1 = link.get("href")
            bookno = href1.split('=')[1]
            booknum.append(bookno)
            print(href1) #this is a check
            name_text = link.get_text()
            print(name_text) #this is a check

        pod = tr.findAll('td')[1]
        for num in pod:
            print(num.string) #this is a check

        booking = tr.findAll('td')[2]
        for year in booking:
            print(year.string)

        mni = tr.findAll('td')[3]
        for num_two in mni:
            print(num_two.string)

        image = tr.findAll('td')[4]
        for pic in image:
            href2 = pic.get("href")
            print(href2)



    #with open("bookings.csv", 'a') as f:
        #w = csv.writer(f)
        w.writerows(zip([name_text],[num.string], [year.string],[num_two.string],[url + href1],[url + href2],[bookno]))

        print(booknum)

#keep the line below

driver.quit();
driver = webdriver.Chrome('/Users/Claudia/Documents/AAAUF_SPRING_19/Adv.Web_Apps/python/scraping_proj/chromedriver')
with open("charges.csv", 'a') as f:
    w = csv.writer(f)
    w.writerows(zip(["book_no"],["charge_no"],["statute"], ["description"],['level'],["degree"]))

    for url_two in booknum:
        driver.get("http://oldweb.circuit8.org/cgi-bin/jaildetail.cgi?bookno=" + url_two)
        html_two = driver.page_source
        #time.sleep(1)

        soup_two = BeautifulSoup(html_two, "html.parser")
        try:
            html_two = soup_two.findAll('table')[1]

            for tr in html_two.findAll('tr')[2:]:
                charges = tr.findAll('td')[0]
                for charge_txt in charges:
                    print(charge_txt.string)

                statute = tr.findAll('td')[1]
                for statno_txt in statute:
                    print(statno_txt.string)

                descrip = tr.findAll('td')[2]
                for descrip_txt in descrip:
                    print(descrip_txt.string)

                level = tr.findAll('td')[3]
                for level_txt in level:
                    print(level_txt.string)

                degree = tr.findAll('td')[4]
                for deg_txt in degree:
                    print(deg_txt.string)

                w.writerows(zip([url_two],[charge_txt.string],[statno_txt.string], [descrip_txt.string],[level_txt.string],[deg_txt.string]))

        except IndexError:
            print('does not have table two')
#keep the line below

driver.quit();
