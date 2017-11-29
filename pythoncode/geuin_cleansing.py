from pandas import *
from selenium import webdriver
import re
from bs4 import BeautifulSoup
# //*[@id="hsDb"]/div[4]/table[1]/tbody/tr[1]/td[2]/a[1]
# //*[@id="hsDb"]/div[4]/table[1]/tbody/tr[2]/td[2]/a[1]
dr = webdriver.Chrome('/Users/joono/Downloads/chromedriver')

dr.get('http://hs.inven.co.kr/dataninfo/card/')
for i in range(0,20):
    for j in range(0,30):
        dr.find_element_by_xpath('//*[@id="hsDb"]/div[4]/table[1]/tbody/tr[{0}]/td[2]/a[1]'.format(j)).click()
        drt = dr.page_source

        tables =