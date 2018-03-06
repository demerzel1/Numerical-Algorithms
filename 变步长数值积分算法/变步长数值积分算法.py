# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math

def cal(x):
    return np.sin(x)/x

e=1e-5
b=6.0
a=0.0+e #避免除0产生错误
#以下为变步长积分算法
h=b-a
t1=h*(cal(a)+cal(b))/2
n=1
p=1+e
while p>e:
    s=0
    k=0
    while k<=n-1:
        x=a+(k+0.5)*h
        s=s+cal(x)
        k=k+1
    t=t1/2+h*s/2
    p=abs(t1-t)
    print("步长h="+ str(h))
    #输出中间过程的步长
    t1=t
    n=n*2
    h=h/2
print(str(t1))
#输出答案