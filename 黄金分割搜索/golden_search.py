# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import math

def cal(x):
    return np.cos(x)

plt.close()
fig = plt.figure() #建图
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(-5,5) #设置范围
x = np.linspace(-np.pi,np.pi, 1000)
y = np.cos(x)
plt.plot(x,y,label="$cos(x)$",color="red",linewidth=1) #显示cos（x）图像

plt.grid(True)
plt.ion() #交互式绘图，动态显示区间

try:
    e=1e-7
    b=np.pi/2
    a=-np.pi/2
    x1=a+(b-a)*0.382
    x2=a+(b-a)*0.618
    f1=cal(x1)
    f2=cal(x2)
    #黄金分割点计算
    while b-a>e:
        ax.scatter(a,cal(a),c='b', marker='o')
        ax.scatter(b,cal(b),c='b', marker='o')
        ax.scatter(x1,f1,c='b', marker='*')
        ax.scatter(x2,f2,c='b', marker='*')
        #用圆点显示左右端点，用星显示黄金分割点
        if f2>f1:
            a=x1
            x1=x2
            f1=f2
            x2=a+0.618*(b-a)
            f2=cal(x2)
        else:
            b=x2
            x2=x1
            f2=f1
            x1=a+0.382*(b-a)
            f1=cal(x1)
        plt.pause(1)
        print("a= "+str(a)+" b= "+str(b))
        ax.set_xlim(a-0.3,b+0.3) #逐步缩小显示范围，显示的更清楚
        #ax.lines.pop(1)
    ax.scatter(a+b/2,cal(a+b/2),c='b',marker='*')
    print(a+b/2)
except Exception as err:
    print(err)