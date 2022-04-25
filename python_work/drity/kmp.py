def get_next(ptr): # 有效域为next[0]到next[l - 2]
    i, k, l = 1, -1, len(ptr)
    next = [-1] * l
    while i < l - 1:
        while k > -1 and ptr[i] != ptr[k + 1]:
            k = next[k]
        if ptr[i] == ptr[k + 1]:
            k += 1
        if ptr[i + 1] == ptr[k + 1]:  # and k > -1不需要,因为next[-1] = -1
            next[i] = next[k]
        else:
            next[i] = k
        i += 1
    return next


def kmp(str, ptr, next):
    i, k, l = 0, -1, len(str)
    while i < l:
        while k > -1 and str[i] != ptr[k + 1]:
            k = next[k]
        if str[i] == ptr[k + 1]:
            k += 1
        if k == len(ptr) - 1:
            break
        i += 1
    if k == len(ptr) - 1:
        return i - len(ptr) + 1
    else:
        return -1


str=input()
ptr = input()
next = get_next(ptr)
#print(next)
print(kmp(str,ptr,next))
