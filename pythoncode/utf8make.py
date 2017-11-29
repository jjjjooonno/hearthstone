from pandas import *
from sklearn import linear_model


dt = read_csv('hearthstone_merge.csv')
x = dt['mana']
att = dt['attack']
hlt = dt['health']


# 격노
rage = dt['격노']
# 과부하
over = dt['과부하']
# 도발
taunt = dt['도발']
# 독성
pois = dt['독성']
# 돌진
char = dt['돌진']
# 생명력흡수
lfst = ['생명력흡수']
# 선택
cho = ['선택']
# 연계
com = ['연계']
# 은신
hid=['은신']
# 적응
adpt = ['적응']
# 주문공격력
mgpw=['주문공격력']
# 질풍
wndf=['질풍']
# 천상의보호막
dvsh = ['천상의보호막']
# 침묵
silen = ['침묵']