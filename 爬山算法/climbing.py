from random import random, randint
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def func(X, Y):
    return 1/(X*X+Y*Y+2)
    #所求函数

def drawPaht(X, Y, Z, px, py, pz):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,  cmap=cm.coolwarm,
                     linewidth=0, antialiased=False ) #绘制3d图像
    ax.set_xlabel('x', color='r')
    ax.set_ylabel('y', color='g')
    ax.set_zlabel('z', color='b')
    ax.plot(px, py, pz, 'r.')  # 绘点
    plt.show()

def hill_climb(X, Y):
    global_X = []
    global_Y = []
    len_x = len(X)
    len_y = len(Y)
    st_x = randint(0, len_x - 1)
    st_y = randint(0, len_y - 1)
    
    def argmax(stx, sty, alisx, alisy):
        cur = func(X[0][stx], Y[sty][0])
        next = func(X[0][alisx], Y[alisy][0])
        if cur < next:
            return alisx, alisy
        return stx, sty
        #比较两点函数值，返回大的

    tmp_x = st_x
    tmp_y = st_y
    while (len_x > st_x >= 0) or (len_y > st_y >= 0):
        if st_x + 1 < len_x:
            tmp_x, tmp_y = argmax(tmp_x, tmp_y, (st_x + 1), st_y)
        if st_x >= 1:
            tmp_x, tmp_y = argmax(tmp_x, tmp_y, st_x - 1, st_y)
        if st_y + 1 < len_x:
            tmp_x, tmp_y = argmax(tmp_x, tmp_y, st_x, st_y + 1)
        if st_y >= 1:
            tmp_x, tmp_y = argmax(tmp_x, tmp_y, st_x, st_y - 1)
        if tmp_x != st_x or tmp_y != st_y:
            st_x = tmp_x
            st_y = tmp_y
        #对周围四个点做比较，选择大的一个
        else:
            break
        global_X.append(X[0][st_x])
        global_Y.append(Y[st_y][0])
    return global_X, global_Y, func(X[0][st_x], Y[st_y][0])


if __name__ == '__main__':
    X = np.arange(-4, 4, 0.1)
    Y = np.arange(-4, 4, 0.1)
    #初始化
    X, Y = np.meshgrid(X, Y)
    Z = func(X, Y)
    px, py, maxhill = hill_climb(X, Y)
    #得到各点坐标和最大值
    print (px)
    print(py)
    print(maxhill)
    #输出
    drawPaht(X, Y, Z, px, py, func(np.array(px), np.array(py)))
    #绘图展示