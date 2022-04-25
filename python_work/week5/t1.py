ar = list(input().split())
n = int(ar[0])
m = int(ar[1])
stack = []
str = '0123456789ABCDEF'
while n != 0:
    q = n % m
    stack.append(str[q])
    n = n // m
while stack != []:
    print(stack.pop(), end='')
