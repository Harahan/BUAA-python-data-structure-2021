import re
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from test import test 
import os


def _test(l, j): # l---重复次数   j---数量级
    res = open("res.txt", "w")
    
    x = 1
    while x <= l:
        k = 10
        while k <= j:
            test(k, k, k)
            os.system(".\\test.exe")
            print([x,k])
            k *= 10
        x += 1

    res.close()


def picture_3D(k, r, m):# k---插入次数  r---k//100  m---k//100
    res = open("res.txt", "w")

    x= 100
    while x >= 1:
        y = 100
        while y >= 1:
            test(k, x*r, y*m)
            os.system(".\\test.exe")
            print([x,y])
            y -= 1
        x -= 1
    

    p = re.compile(r"\d+\.\d+")
    arr1, arr2, arr3 = [], [], []
    buf1, buf2, buf3 = [], [], []

    res = open("res.txt", "r")
    i = 1
    while True:
        if i == 4:
            i = 1
        line = res.readline()
        if not line:
            break
        l = re.findall(p, line)
        if l != []:
            if i == 1:
                arr1.extend(l)
            elif i == 2:
                arr2.extend(l)
            else:
                arr3.extend(l)
            i += 1

    i = 0
    while i < len(arr1):
        buf1.append(float(arr1[i]) + float(arr1[i+1]) + float(arr1[i+2]))
        buf2.append(float(arr2[i]) + float(arr2[i+1]) + float(arr2[i+2]))
        buf3.append(float(arr3[i]) + float(arr3[i+1]) + float(arr3[i+2]))
        i += 3

    x1, x2 = [], []
    x, y = 1, 1
    while x >= 0.01:
        for i in range(0, 100):
            x1.append(x)
        x -= 0.01

    for i in range(0, 100):
        while y >= 0.01:
            x2.append(y)
            y -= 0.01
        y = 1

    #########################################################################

    fig1 = plt.figure()
    ax = Axes3D(fig1,auto_add_to_figure=False)
    fig1.add_axes(ax)


    ax.set_zlabel('time/s', fontdict={'size': 10, 'color': 'red'})
    ax.set_ylabel('delete/insert', fontdict={'size': 10, 'color': 'red'})
    ax.set_xlabel('search/insert', fontdict={'size': 10, 'color': 'red'})

    x_new = np.array(x1)
    y_new = np.array(x2)
    t_new = np.array(buf1)

    ax.plot_trisurf(x_new, y_new, t_new, cmap='spring')

    plt.suptitle("avl_tree", color='y', size=10)
    plt.savefig("avl_tree.png",dpi = 500)
    plt.show()

    #########################################################################

    fig2 = plt.figure()
    ax = Axes3D(fig2,auto_add_to_figure=False)
    fig2.add_axes(ax)

    ax.set_zlabel('time/s', fontdict={'size': 10, 'color': 'red'})
    ax.set_ylabel('delete/insert', fontdict={'size': 10, 'color': 'red'})
    ax.set_xlabel('search/insert', fontdict={'size': 10, 'color': 'red'})

    x_new = np.array(x1)
    y_new = np.array(x2)
    t_new = np.array(buf2)

    ax.plot_trisurf(x_new, y_new, t_new, cmap='spring')

    plt.suptitle("b_tree", color='g', size=10)
    plt.savefig("b_tree.png",dpi = 500)
    plt.show()

    ############################################################################

    fig3 = plt.figure()
    ax = Axes3D(fig3,auto_add_to_figure=False)
    fig3.add_axes(ax)

    ax.set_zlabel('time/s', fontdict={'size': 10, 'color': 'red'})
    ax.set_ylabel('delete/insert', fontdict={'size': 10, 'color': 'red'})
    ax.set_xlabel('search/insert', fontdict={'size': 10, 'color': 'red'})

    x_new = np.array(x1)
    y_new = np.array(x2)
    t_new = np.array(buf3)

    ax.plot_trisurf(x_new, y_new, t_new, cmap='spring')

    plt.suptitle("red_black_tree", color="r", size=10)
    plt.savefig("red_black_tree.png",dpi = 500)
    plt.show()

    res.close()
    

def picture_2D(k, j, b):# k---从k开始跑第一个点  j---数量级  b---10^b == k
    res = open("res.txt", "w")
    b1 = b
    
    while k <= j:
        test(k, k, k)
        os.system(".\\test.exe")
        print(k)
        k *= 10
    
    p = re.compile(r"\d+\.\d+")
    arr1, arr2, arr3 = [], [], []
    res = open("res.txt", "r")
    i = 1
    while True:
        if i == 4:
            i = 1
        line = res.readline()
        if not line:
            break
        l = re.findall(p, line)
        if l != []:
            if i == 1:
                arr1.extend(l)
            elif i == 2:
                arr2.extend(l)
            else:
                arr3.extend(l)
            i += 1

############################################################################################
        
    y1 = [float(arr1[i]) for i in range(0, len(arr1), 3)]
    y2 = [float(arr2[i]) for i in range(0, len(arr2), 3)]
    y3 = [float(arr3[i]) for i in range(0, len(arr3), 3)]
    x = []

    for i in y1:
        x.append(int(10**b))
        b += 1
        
    plt.plot(x, y1, label='avl_tree', linewidth=2, marker='x',
         markerfacecolor='black', markersize=4)
    plt.plot(x, y2, label='b_tree', linewidth=2, marker='x',
            markerfacecolor='black', markersize=4)
    plt.plot(x, y3, label='red_black_tree', linewidth=2, marker='x',
            markerfacecolor='black', markersize=4)
    plt.xlabel('dot number')
    plt.ylabel('time/s')
    plt.title('insert time contrast')
    plt.legend()
    plt.savefig("insert_comparison.png", dpi=500)
    plt.show()

############################################################################################

    y1 = [float(arr1[i]) for i in range(1, len(arr1), 3)]
    y2 = [float(arr2[i]) for i in range(1, len(arr2), 3)]
    y3 = [float(arr3[i]) for i in range(1, len(arr3), 3)]
    x = []

    b = b1
    for i in y1:
        x.append(int(10**b))
        b += 1

    plt.plot(x, y1, label='avl_tree', linewidth=2, marker='x',
         markerfacecolor='black', markersize=4)
    plt.plot(x, y2, label='b_tree', linewidth=2, marker='x',
            markerfacecolor='black', markersize=4)
    plt.plot(x, y3, label='red_black_tree', linewidth=2, marker='x',
            markerfacecolor='black', markersize=4)
    plt.xlabel('dot number')
    plt.ylabel('time/s')
    plt.title('search time contrast')
    plt.legend()
    plt.savefig("search_comparison.png", dpi=500)
    plt.show()

###################################################################################################

    y1 = [float(arr1[i]) for i in range(2, len(arr1), 3)]
    y2 = [float(arr2[i]) for i in range(2, len(arr2), 3)]
    y3 = [float(arr3[i]) for i in range(2, len(arr3), 3)]
    x = []

    b = b1
    for i in y1:
        x.append(int(10**b))
        b += 1

    plt.plot(x, y1, label='avl_tree', linewidth=2, marker='x',
         markerfacecolor='black', markersize=4)
    plt.plot(x, y2, label='b_tree', linewidth=2, marker='x',
            markerfacecolor='black', markersize=4)
    plt.plot(x, y3, label='red_black_tree', linewidth=2, marker='x',
            markerfacecolor='black', markersize=4)
    plt.xlabel('dot number')
    plt.ylabel('time/s')
    plt.title('delete time contrast')
    plt.legend()
    plt.savefig("delete_comparison.png", dpi=500)
    plt.show()
    
    res.close()


#_test(3, 10000000)
#picture_3D(500000, 5000, 5000)
#picture_2D(1000, 10000000, 3)
