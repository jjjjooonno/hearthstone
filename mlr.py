from pandas import *
import tensorflow as tf
import numpy as np


dt = read_csv('hearthstone_merge.csv')
# 코스트
mana = np.asarray(dt['mana'],dtype=np.float32)
# 공격력
att = np.asarray(dt['attack'],dtype=np.float32)
# 체력
hlt = np.asarray(dt['health'],dtype=np.float32)
# 격노
rage = np.asarray(dt['격노'],dtype=np.float32)
# 과부하)
over = np.asarray(dt['과부하'],dtype=np.float32)
# 도발
taunt = np.asarray(dt['도발'],dtype=np.float32)
# 독성
pois = np.asarray(dt['독성'],dtype=np.float32)
# 돌진
char = np.asarray(dt['돌진'],dtype=np.float32)
# 생명력흡수
lfst = np.asarray(dt['생명력흡수'],dtype=np.float32)
# 선택
cho = np.asarray(dt['선택'],dtype=np.float32)
# 연계
com = np.asarray(dt['연계'],dtype=np.float32)
# 은신
hid=np.asarray(dt['은신'],dtype=np.float32)
# 적응
adpt = np.asarray(dt['적응'],dtype=np.float32)
# 주문공격력
mgpw=np.asarray(dt['주문공격력'],dtype=np.float32)
# 질풍
wndf=np.asarray(dt['질풍'],dtype=np.float32)
# 천상의보호막
dvsh = np.asarray(dt['천상의보호막'],dtype=np.float32)
# 침묵
silen = np.asarray(dt['침묵'],dtype=np.float32)


#



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
W = tf.Variable(tf.random_uniform([1, 16], -1.0, 1.0))

y = tf.matmul(W, np.transpose(x_data))

loss = tf.reduce_mean(tf.square(y - mana))
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(100000):
    sess.run(train)
    if step % 1000 == 0:
        print(step, sess.run(W), sess.run(loss))