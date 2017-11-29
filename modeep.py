from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
from pandas import *
import tensorflow as tf
import numpy as np


dt = read_csv('hearthstone_merge.csv')
# 코스트
mana = (dt['mana'])
# 공격력
att = dt['attack']
# 체력
hlt = dt['health']
# 격노
rage = dt['격노']
# 과부하)
over = dt['과부하']
# 도발
taunt = dt['도발']
# 독성
pois = dt['독성']
# 돌진
char = dt['돌진']
# 생명력흡수
lfst = dt['생명력흡수']
# 선택
cho = dt['선택']
# 연계
com = dt['연계']
# 은신
hid=dt['은신']
# 적응
adpt = dt['적응']
# 주문공격력
mgpw=dt['주문공격력']
# 질풍
wndf=dt['질풍']
# 천상의보호막
dvsh = dt['천상의보호막']
# 침묵
silen = dt['침묵']
# 코스트
# mana = np.asarray(dt['mana'],dtype=np.float32)
# # 공격력
# att = np.asarray(dt['attack'],dtype=np.float32)
# # 체력
# hlt = np.asarray(dt['health'],dtype=np.float32)
# # 격노
# rage = np.asarray(dt['격노'],dtype=np.float32)
# # 과부하)
# over = np.asarray(dt['과부하'],dtype=np.float32)
# # 도발
# taunt = np.asarray(dt['도발'],dtype=np.float32)
# # 독성
# pois = np.asarray(dt['독성'],dtype=np.float32)
# # 돌진
# char = np.asarray(dt['돌진'],dtype=np.float32)
# # 생명력흡수
# lfst = np.asarray(dt['생명력흡수'],dtype=np.float32)
# # 선택
# cho = np.asarray(dt['선택'],dtype=np.float32)
# # 연계
# com = np.asarray(dt['연계'],dtype=np.float32)
# # 은신
# hid=np.asarray(dt['은신'],dtype=np.float32)
# # 적응
# adpt = np.asarray(dt['적응'],dtype=np.float32)
# # 주문공격력
# mgpw=np.asarray(dt['주문공격력'],dtype=np.float32)
# # 질풍
# wndf=np.asarray(dt['질풍'],dtype=np.float32)
# # 천상의보호막
# dvsh = np.asarray(dt['천상의보호막'],dtype=np.float32)
# # 침묵
# silen = np.asarray(dt['침묵'],dtype=np.float32)
x_data = []
for i in range(0,630):
    x_data.append([])
    x_data[i].append(rage[i])
    x_data[i].append(over[i])
    x_data[i].append(taunt[i])
    x_data[i].append(pois[i])
    x_data[i].append(char[i])
    x_data[i].append(lfst[i])
    x_data[i].append(cho[i])
    x_data[i].append(com[i])
    x_data[i].append(hid[i])
    x_data[i].append(adpt[i])
    x_data[i].append(mgpw[i])
    x_data[i].append(wndf[i])
    x_data[i].append(dvsh[i])
    x_data[i].append(silen[i])
    x_data[i].append(att[i])
    x_data[i].append(hlt[i])

mana_y = []
for i in mana:
    mana_y.append([i])
model = Sequential()
model.add(Dense(input_dim=16, units=1))
model.add(Activation('linear'))

rmsprop = RMSprop(lr=1e-10)
model.compile(loss='mse', optimizer=rmsprop)
model.fit(x_data, mana, epochs=1000)

y_predict = model.predict(np.array([[0,0,1,0,0,1,0,0,0,0,0,0,0,0,4,8]]))
print(y_predict)