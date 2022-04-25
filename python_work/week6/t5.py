arr = list(map(int, input().split()))
k = int(input())
c = 0
buf = []
for i in range(len(arr)):
    a = arr[i]
    c = 1
    if a >= k:
        buf.append(c)
        break  # 如果此时大于等于了，那么可以直接出循环了
    for j in range(i + 1, len(arr)):
        a += arr[j]
        c += 1
        if a >= k:
            buf.append(c)
            break

if buf != []:
    buf.sort()
    print(buf[0])
else:
    print(-1)
# 3 4 -1 6
