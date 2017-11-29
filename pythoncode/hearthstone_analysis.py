import pandas as pd
from pandas import *
import re

exp = [0,6,7,8,9,10]
for i in exp:
    dt = read_csv('hearthstone_expansion_{0}_w.csv'.format(i))
    # 격노
    er = []
    # 과부하
    ol = []
    # 도발
    tt = []
    # 독성
    ps = []
    # 돌진
    crg = []
    # 생명력 흡수
    ls = []
    # 선택
    cs = []
    # 연계
    cb = []
    # 은신
    st = []
    # 적응
    adt = []
    # 주문공격력
    mp = []
    # 질풍
    wf = []
    # 천상의 보호막
    ds = []
    # 침묵
    sl = []
    for j in dt['desc_cut']:
        if '격노' in j:
            er.append(1)
        else:
            er.append(0)
        if '과부하' in j:
            ol.append(1)
        else:
            ol.append(0)
        if '도발' in j:
            tt.append(1)
        else:
            tt.append(0)
        if '독성' in j:
            ps.append(1)
        else:
            ps.append(0)
        if '돌진' in j:
            crg.append(1)
        else:
            crg.append(0)
        if '생명력 흡수' in j:
            ls.append(1)
        else:
            ls.append(0)
        if '선택' in j:
            cs.append(1)
        else:
            cs.append(0)
        if '연계' in j:
            cb.append(1)
        else:
            cb.append(0)
        if '은신' in j:
            st.append(1)
        else:
            st.append(0)
        if '적응' in j:
            adt.append(1)
        else:
            adt.append(0)
        if '주문공격력' in j:
            mp.append(1)
        else:
            mp.append(0)
        if '질풍' in j:
            wf.append(1)
        else:
            wf.append(0)
        if '천상의 보호막' in j:
            ds.append(1)
        else:
            ds.append(0)
        if '침묵' in j:
            sl.append(1)
        else:
            sl.append(0)
    dt['격노'] = er
    dt['과부하'] = ol
    dt['도발'] = tt
    dt['독성'] = ps
    dt['돌진'] = crg
    dt['생명력흡수'] = ls
    dt['선택'] = cs
    dt['연계'] = cb
    dt['은신'] = st
    dt['적응'] = adt
    dt['주문공격력'] = mp
    dt['질풍'] = wf
    dt['천상의보호막'] = ds
    dt['침묵'] =sl
    dt.to_csv('hearthstone_expansion_{0}_w2.csv'.format(i))



