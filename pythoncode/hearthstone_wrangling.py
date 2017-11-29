import pandas as pd
from pandas import *
import re
exp = [0,6,7,8,9,10]
for i in exp:
    dt = pd.read_csv('hearthstone_expansion_{0}.csv'.format(i))
    desc = []
    for j in dt['desc']:
        i1 = j[7:].split('<')
        i2 = ''.join(i1)
        i3 = i2.split('>')
        i4 = ''.join(i3)
        i5 = i4.split('/')
        i6 = ''.join(i5)
        i7 = i6.split('br')
        i8 = ''.join(i7)
        i9 = i8.split('b')
        i10 = ''.join(i9)
        desc.append(i10)
    dt['desc_cut'] = desc
    dt = dt.drop('desc',1)
    dt.to_csv('hearthstone_expansion_{0}_w.csv'.format(i))
