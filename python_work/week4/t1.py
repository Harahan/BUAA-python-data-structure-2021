n=int(input())
stack=[]
for i in range(n):
    stack.append(int(input()))
m=int(input())
n=[]
for j in range(m):
    a=list(input().split())
    if a[0]=='A':
        stack.append(a[1])
    else:
        if(stack==[]):
            print("No")
            break
        n.append(stack.pop(-1))
if stack!=[]:
    while n!=[]:
        print(n.pop(0),end=' ')
    print("\n",end='')
while stack!=[]:
    print(stack.pop(-1),end=' ')