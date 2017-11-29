from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import DataFrame
import re
import time

dr = webdriver.Chrome('/Users/joono/Downloads/chromedriver')
dr.implicitly_wait(1000)


expansion = [0,6,7,8,9,10]
page = [8,4,2,4,4,4]
for i in expansion:
    cn = []
    rarity = []
    desc = []
    att_num = []
    hlth_num = []
    cost_num = []
    name = re.compile('-[0-9]\"\>[a-zA-Z가-힣0-9\s\:]+')

    cost = re.compile('cost\"\>[0-9]+')

    att = re.compile('attack\"\>[0-9]+')

    hlth = re.compile('health\"\>[0-9]+')

    desc_re = re.compile(r'right\"\>[\(\)\'가-힣\s<br/>\.0-9\:\+,]+')

    for j in (range(1,page[expansion.index(i)]+1)):
        dr.get('http://hs.inven.co.kr/dataninfo/card/#cardtype=4,expansion={0},page={1}'.format(i,j))
        time.sleep(1)
        drt = dr.page_source
        soup = BeautifulSoup(drt,'html.parser')
        card = soup.find_all('tbody')
        cards = str(card[1]).split('<tr>')[1:]
        for k in cards:
            cn.append(name.findall(k)[0][4:])
            print(name.findall(k))
            rarity.append(name.findall(k)[0][1])
            att_num.append(att.findall(k)[0][8:])
            hlth_num.append(hlth.findall(k)[0][8:])
            desc.append(desc_re.findall(k)[0])
            cost_num.append(cost.findall(k)[0][6:])
    dt = DataFrame({'name' : cn, 'rarity' : rarity, 'desc' : desc, 'mana' : cost_num, 'attack' : att_num, 'health' : hlth_num})
    print(dt)
    dt.to_csv('hearthstone_expansion_{0}.csv'.format(i), encoding = 'utf-8',index = None)

# 카드이름 / 하수인 / 등급 / 설명
#
# dr.get('http://hs.inven.co.kr/dataninfo/card/#cardtype=4,expansion=6,page=1')
# drt = dr.page_source
# soup = BeautifulSoup(drt,'html.parser')
# card = soup.find_all('tbody')
# cards=str(card[1]).split('<tr>')[1:]

# name1 = soup.find('h2',attrs = {'class' : 'title710BR1'})
# name2 = str(name1).split('(')
# name3 = name2[0].split('-')
# name.append(name3[1].strip())
# cardeffect = str(card[0])
# cardtext = str(card[2]).split('\n')
#
#
#
# con = re.compile('[가-힣0-9]+')
# text = []
# for i in cardtext:
#     text.append(con.findall(i))
# text.append(con.findall(cardeffect))
#
#
# rank.append(text[8][1])
# hs_class.append(text[11][1])
# species.append(text[12][-1])
# cost.append(text[16][1])
# attack.append(text[19][1])
# life.append(text[20][1])
# dr.back()
# time.sleep(1)
#
#
# dt = DataFrame({'Name': name, 'rank': rank, 'Hs_class': hs_class,
#                 'Species': species, 'Cost': cost, 'Attack': attack, 'Life': life})
# print(dt)
dr.close()