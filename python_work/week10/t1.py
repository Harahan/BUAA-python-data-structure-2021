a = list(map(int, input().split()))
high = len(a) - 1
low = 0
k = int(input())

while low <= high:
    mid = (high + low) // 2
    if a[mid] == k:
        break
    elif a[mid] < k:
        low = mid + 1
    else:
        high = mid - 1

if a[mid] == k:
    print(mid)
else:
    print(-1)
