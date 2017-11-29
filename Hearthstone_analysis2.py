import pandas as pd
from pandas import *
exp = [0,6,7,8,9,10]
cards = []
for i in exp:
    dt = read_csv('hearthstone_expansion_{0}_w2.csv'.format(i))
    ex = []
    for j in range(0,len(dt['attack'])):
        ex.append(i)
    dt['exp'] = ex
    cards.append(dt)
dt_whole = DataFrame(concat(cards,ignore_index=True))
dt_whole = DataFrame(dt_whole.drop('Unnamed: 0',axis=1))
dt_whole = DataFrame(dt_whole.drop('Unnamed: 0.1',axis=1))
print(dt_whole)
dt_whole.to_csv('hearthstone_merge.csv',index=False)