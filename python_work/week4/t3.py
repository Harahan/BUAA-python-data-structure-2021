array=list(map(int,input().split()))
stack=[]
while array!=[]:
    k=array.pop(0)
    if stack!=[]and stack[-1]<=k:
        while stack!=[] and stack[-1]<=k:
            stack.pop()
        stack.append(k)
    else:
        stack.append(k)
while stack!=[]:
    print(stack.pop(),end=' ')
