a = list(map(int, input().split()))
h = len(a) - 1
L = len(a) - 1
l = 0


while l <= h:
    mid = (h + l) // 2
    if (mid - 1 < 0 or a[mid - 1] != a[mid]) and (mid + 1 > L or a[mid + 1] != a[mid]):
        break
    elif mid % 2 == 0:
        if a[mid - 1] != a[mid]:
            l = mid + 1
        else:
            h = mid - 1
    elif mid % 2 == 1:
        if a[mid - 1] != a[mid]:
            h = mid - 1
        else:
            l = mid + 1


print(a[mid])
