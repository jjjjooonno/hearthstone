from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
from datetime import datetime
import re
import time

dr = webdriver.Chrome('/Users/joono/Downloads/chromedriver')
dr.implicitly_wait(1000)
name = []
rank = []
hs_class = []
species = []
cost = []
attack = []
life = []
abil = []
#hsDb > div.hsDbCommonTitle > h2
card = []
dr.get('http://hs.inven.co.kr/dataninfo/card/detail.php?code=68')
drt = dr.page_source
soup = BeautifulSoup(drt,'html.parser')
card.extend(soup.find_all('table'))