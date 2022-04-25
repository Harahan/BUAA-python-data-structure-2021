from avl_tree import avl_tree
from b_tree import b_tree
from red_black_tree import rb_tree
import random
import time

inf = 2147483647
print("begin or not:",end=" ")
flag = input()
while flag == "begin" or flag == "again":
    print("The amount of node you want to insert:",end=" ")
    k = int(input())
    a = random.sample(range(-inf, inf), k)
    T1 = avl_tree()
    t1 = time.time()
    T1.root = T1.add(None, a[0])
    for i in range(1, len(a)):
        T1.root = T1.add(T1.root, a[i])  # root renew
    t2 = time.time()
    t = t2 - t1
    print("The avl_tree usesd:" + str(t) + "s")
    t1 = time.time()
    m = 3
    T2 = b_tree(m)
    for key in a:
        T2.add(int(key))
    t2 = time.time()
    t = t2 - t1
    print("The b_tree usesd:" + str(t) + "s")
    t1 = time.time()
    T3 = rb_tree()
    for key in a:
        T3.add(int(key))
    t2 = time.time()
    t = t2 - t1
    print("The red_black_tree usesd:" + str(t) + "s")
    print("The amount of node you want to search:",end=" ")
    i = int(input())
    if i != 0:
        b = random.sample(a, i)
        t1 = time.time()
        for key in b:
            T1.search(T1.root, key)
        t2 = time.time()
        t = t2 - t1
        print("The avl_tree usesd:" + str(t) + "s")
        t1 = time.time()
        for key in b:
            T2.search(key) 
        t2 = time.time()
        t = t2 - t1
        print("The b_tree usesd:" + str(t) + "s")
        t1 = time.time()
        for key in b:
            T3.search(T3.root, key)
        t2 = time.time()
        t = t2 - t1
        print("The red_black_tree usesd:" + str(t) + "s")
    print("The amount of node you want to delete:",end=" ")
    j = int(input())
    if j != 0:
        c = random.sample(a, j)
        t1 = time.time()
        for key in c:
            T1.delete(T1.root, key)
        t2 = time.time()
        t = t2 - t1
        print("The avl_tree usesd:" + str(t) + "s")
        t1 = time.time()
        for key in c:
            T2.delete(key)
        t2 = time.time()
        t = t2 - t1
        print("The b_tree usesd:" + str(t) + "s")
        t1 = time.time()
        for key in c:
            T3.delete(key)
        t2 = time.time()
        t = t2 - t1
        print("The red_black_tree usesd:" + str(t) + "s")
    print("again or not:",end=" ")
    flag = input()
print("It's over now.")


