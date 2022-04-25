import sys

array1 = list(input())
array2 = list(input())
flag = True
if len(array2) != len(array1):
    flag = False
    print(flag)
    exit(0)
j = 0
key = []
for i in range(len(array2)):
    if array2[i] != array1[i]:
        j += 1
        key.append(i)
if j > 2:
    flag = False
    print(flag)
elif j == 2:
    if array2[key[0]] == array1[key[1]] and array2[key[1]] == array1[key[0]]:
        print(flag)
    else:
        flag = False
        print(flag)
elif j == 1:
    flag = False
    print(flag)
elif j == 0:
    if len(set(array2)) != len(array2):  # tuple(),元组
        print(flag)
    else:
        flag = False
        print(flag)
