n=int(input())
queue=[]
for i in range(n):
    queue.append(int(input()))
m=int(input())
for i in range(m):
    k=input()
    if k=="D":
        print(queue.pop(0))
    else:
        queue.append(int(k))