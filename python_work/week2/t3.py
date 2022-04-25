array=list(input())
for i in range(len(array)-1):
    array[i]=int(array[i])
array1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2,]
i=0
sum=0
while i<17:
    sum+=array[i]*array1[i]
    i+=1
i=sum%11
array2=["1","0","X","9","8","7","6","5","4","3","2"]
if array2[i]==str(array[17]):
     print("YES")
else:
     print("NO")


