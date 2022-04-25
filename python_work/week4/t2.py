array=list(input().split())
#print(array)
n=int(array[0])
k=int(array[1])
str='0123456789ABCDEF'
stack=[]
#print(k)
while n!=0:
    stack.append(str[n%k])
    n=n//k
while stack!=[]:
    print(stack.pop(),end='')


