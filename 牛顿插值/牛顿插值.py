import matplotlib.pyplot as plt
import numpy as np

fig= plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_ylim(-50,50)
#建立图像
x0 = np.array([0,10,20,30,40,50,60,70,80,90,100,110,120],np.float32)
y0 = np.array([3.2,5,7,7.2,4.5,4.9,8,16.3,7,-8,-2,3.4,15],np.float32)
#初始化插值点
def get_an(x,y,a,tlen):
    for i in range(tlen):
        a[i] = y[i]
    for i in range(tlen):
        if i == 0 :
            continue
        j=tlen-1
        while j>= i:
            a[j]=(a[j]-a[j-1])/(x[j]-x[j-i])
            j=j-1
    return a
#得到牛顿插值的a参数
def newton(x,y,xx,a,tlen):
    ans=a[tlen]
    i=tlen-1
    while i>=0:
        ans=ans*(xx-x[i])+a[i]
        i=i-1
    return ans
#牛顿插值
ax.plot(x0,y0,'--*')

xi = np.arange(0,120,1)
yi = np.zeros(len(xi))

plt.ion()#交互式绘图
try:
    for i in range(len(y0)+1):
    #从1，2，3...n个点进行插值 以动态观察插值函数的变化
        yi=np.zeros(len(xi))
        for j in range(len(xi)):
            a = np.zeros(i+10)
            a=get_an(x0,y0,a,i)
            yi[j]=newton(x0,y0,xi[j],a,i)
        #得到插值图像
        ax.plot(xi,yi)
        plt.pause(0.5)
        if i!=len(y0):
            ax.lines.pop(1) #删除上一个插值图
    plt.pause(100)
except Exception as err:
    print(err)
 