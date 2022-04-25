array=[]
i=0
j=0
while True:
    array.append(int(input()))
    if array[i]==-1:
        break
    else:
        i+=1
for i in range(len(array)-1):
    if array[i]==1:
        j+=1
if 2*j>=len(array)-1:#注意减一
    print("Yes")
else:
    print("No")