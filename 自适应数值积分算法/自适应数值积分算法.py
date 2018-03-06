# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import math

def cal(x):
    return np.sin(x)/x
#所求函数
e = 1e-5
b = 6.0
a = 0.0+e #防止除0
e = e/(b-a)
i = 0
s = 0
u = a
v = b
st = np.zeros(1000000)
#以下为自适应算法 经过一些改动
while 1:
    h = v-u
    t1 = (cal(u)+cal(v))*h/2
    w = (u+v)/2
    t2 = t1/2+h*cal(w)/2
    if abs(t2-t1) < e*h :
        s = s+t2
        if i != 0:
            u = v
            v = st[i]
            i=i-1
        else :
            print(s)
            break
    else :
        i=i+1
        st[i] = v
        v = w