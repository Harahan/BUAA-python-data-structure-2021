def qsort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[j for j in array[1:] if pivot>j]
        great=[j for j in array[1:] if pivot<j]
        return qsort(less)+[pivot]+qsort(great)
k=input()
array=list(map(int,input().split()))
array1=qsort(array)
max=array1[1]-array1[0]
max_num=0
for i in range(1,len(array1)-1):
    if max<array1[i+1]-array1[i]:
        max=array1[i+1]-array1[i]
        max_num=i
print(f"{array1[max_num]} {array1[max_num+1]}")
for i in range(max_num+1,len(array1)-1):
    if max==array1[i+1]-array1[i]:
        print(f"{array1[i]} {array1[i+1]}")

