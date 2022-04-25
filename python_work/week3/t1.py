n=int(input())
flag=True
i=0
while i<n:
    array=list(map(int,input().split()))
    if len(array)!=n:
        flag=False
        break
    i+=1
if flag:
    print("True")
else:
    print("False")