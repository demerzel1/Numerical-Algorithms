import matplotlib.pyplot as plt
import numpy as np

fig= plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_ylim(-50,50)
#建立图像
x0 = np.array([0,10,20,30,40,50,60,70,80,90,100,110,120],np.float32)
y0 = np.array([3.2,5,7,7.2,4.5,4.9,8,16.3,7,-8,-2,3.4,15],np.float32)
#初始插值点
ax.plot(x0,y0,'--*')
#以下为三次自然样条算法
h = np.zeros(len(x0)+10)
a = np.zeros(len(x0)+10)
b = np.zeros(len(x0)+10)
c = np.zeros(len(x0)+10)
d = np.zeros(len(x0)+10)
sss = np.zeros(len(x0)+10)
for k in range(len(x0)-1):
    h[k] = x0[k+1]-x0[k]
a[1] = 2*(h[0]+h[1])
k=2
while k < len(x0)-1:
    a[k] = 2*(h[k-1]+h[k])-h[k-1]*h[k-1]/a[k-1]
    k = k+1
for k in range(len(x0)):
    if k == 0:
        continue
    c[k] = (y0[k]-y0[k-1])/h[k-1]
for k in range(len(x0)-1):
    if k == 0:
        continue
    d[k] = 6*(c[k+1]-c[k])
b[1] = d[1]
k=2
while k < len(x0)-1:
    b[k] = d[k]-b[k-1]*h[k-1]/a[k]
    k = k+1
sss[len(x0)-2] = b[len(x0)-2]/a[len(x0)-2]
k = len(x0)-3
while k>=1 :
    sss[k]=(b[k]-h[k]*sss[k+1])/a[k]
    k=k-1
sss[0] = 0
sss[len(x0)-1] = 0

plt.ion() #交互式绘图

try:
    for k in range(len(x0)-1):
        #从1,2...到n个点动态展示三次自然样条图像
        plt.pause(0.5)
        xi = np.arange(x0[k],x0[k+1],0.1)
        print("len="+str(len(xi)))
        yi = np.zeros(len(xi))
        for i in range(len(xi)):
            ss = c[k+1]-sss[k+1]*h[k]/6-sss[k]*h[k]/3
            yi[i] = y0[k]+ss*(xi[i]-x0[k])+sss[k]*(xi[i]-x0[k])*(xi[i]-x0[k])/2+(sss[k+1]-sss[k])*((xi[i]-x0[k])**3)/(6*h[k])
        #绘图
        ax.plot(xi,yi)
    plt.pause(100)
except Exception as err:
    print(err)