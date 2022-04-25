array=list(map(int,input().split()))
max_num=array[0]
max=0
for i in range(1,len(array)):
    if array[i]>max_num:
        max_num=array[i]
        max=i
print(max+1,end=" ")
for j in range(max+1,len(array)):
   if array[max]==array[j]:
        print(j+1,end=" ")