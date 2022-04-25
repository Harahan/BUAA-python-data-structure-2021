n=int(input())
m=int(input())
dq=[i for i in range(1,n+1)]
while len(dq)!=1:
    for i in range(1,m):
        dq.append(dq.pop(0))
    dq.pop(0)
print(dq.pop())