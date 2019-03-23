import time
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup


# my path is '/Users/mcadams/Documents/python/scraping'
# yours will be different


driver = webdriver.Chrome('/Users/Claudia/Documents/AAAUF_SPRING_19/Adv.Web_Apps/python/scraping_proj/chromedriver')
driver.get('https://www.rottentomatoes.com/browse/dvd-streaming-all');

# page_source is a variable created by Selenium - it holds all the HTML
html = driver.page_source

bsObj = BeautifulSoup(html, "html.parser")
title_list = bsObj.findAll("h3", {"class":"movieTitle"})
for title in title_list:
    print(title.get_text())

print("There are " + str(len(title_list)) + " movies in the list.")
driver.quit()
