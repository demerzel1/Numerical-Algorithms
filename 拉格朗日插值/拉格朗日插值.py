import matplotlib.pyplot as plt
import numpy as np

fig= plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_ylim(-50,50)
#建立图像
a = np.array([0,10,20,30,40,50,60,70,80,90,100,110,120],np.float32)
b = np.array([3.2,5,7,7.2,4.5,4.9,8,16.3,7,-8,-2,3.4,15],np.float32)
#随机的初始插值点
def Larange(x,y,a,tlen):
    ans = 0.0
    for i in range(tlen):
        t = y[i]
        for j in range(tlen):
            if i != j:
                t *= (a-x[j])/(x[i]-x[j])
        ans += t
    return ans
#拉格朗日插值
ax.plot(a,b,'--*')
#绘制初始点连线图
xi = np.arange(0,120,1)
yi = np.zeros(len(xi))

plt.ion() #交互式绘图
try:
    for i in range(len(b)+1):
        #从1，2，3...n个点进行插值 以动态观察插值函数的变化
        yi=np.zeros(len(xi))
        for j in range(len(xi)):
            yi[j]=Larange(a,b,xi[j],i)
        #得到插值点
        ax.plot(xi,yi)
        plt.pause(0.5) #停顿以动态观察
        if i!=len(b):
            ax.lines.pop(1) #删掉上一根线
    plt.pause(100)
except Exception as err:
    print(err)
