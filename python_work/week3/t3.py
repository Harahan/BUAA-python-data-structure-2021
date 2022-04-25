from operator import itemgetter
n=int(input())
array=[[]for i in range(n)]
for i in range(0,n):
    array[i].append(input())
    array[i].append(float(input()))
array=sorted(array,key=itemgetter(1))
array.reverse()
for i in range(0,n):
    print(array[i][0],end=", ")
    print("%.2f"%array[i][1])
'''sort 与 sorted 区别：

    sort 是应用在 list 上的方法，属于列表的成员方法，sorted 可以对所有可迭代的对象进行排序操作。
    list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
    sort使用方法为ls.sort()，而sorted使用方法为sorted'''




