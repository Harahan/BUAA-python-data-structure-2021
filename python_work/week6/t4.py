n = int(input())
array = []
for i in range(n):
    array.append(input())
flag = len(array[0])
for i in range(n):
    if len(array[i]) < flag:
        flag = len(array[i])
j, tag = 0, True
while j < flag:
    for i in range(n):
        if array[0][j] != array[i][j]:
            tag = False
            break
    if tag == False:
        break
    else:
        j += 1
if j == 0:
    print("No")
else:
    for i in range(j):
        print(array[0][i], end='')
