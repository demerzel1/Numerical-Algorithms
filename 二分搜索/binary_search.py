# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import math

def cal(x):
    return x-2* np.sin(x)

plt.close()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) #建图
ax.set_xlim(-10,10)
x = np.linspace(-10,10, 1000)
y = x-2* np.sin(x) 
plt.plot(x,y,label="$x-2*sin(x)$",color="red",linewidth=1) #绘制x-2sin(x)的图像

plt.grid(True)
plt.ion() #交互式绘图

try:
    e=1e-5 
    b=5
    a=0
    while b-a>e:
        print("a= "+str(a)+" b= "+str(b))
        ax.scatter(a,cal(a),c='b', marker='o')
        ax.scatter(b,cal(b),c='b', marker='o')
        #绘制左右端点
        mid=(a+b)/2
        if cal(mid)>0 :
            b=mid
        else:
            a=mid
        #二分区间
        ax.scatter(mid, cal(mid), c='b', marker='*') #绘制中点
        plt.pause(0.5)
        ax.set_xlim(a-0.3,b+0.3) #缩小区间显示范围
        #ax.lines.pop(1)
    ax.scatter(a,cal(a),c='b',marker='*')
    print(a)
    
except Exception as err:
    print(err)