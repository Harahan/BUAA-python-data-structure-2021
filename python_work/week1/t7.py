def qsort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[j for j in array[1:] if j<=pivot]
        great=[j for j in array[1:] if j>pivot]
    return qsort(less)+[pivot]+qsort(great)#不改变array0的值
array=[]
array0=[]
i=0
while True:
    array.append(input())
    i+=1
    if len(array[i-1])==0:#空串判断
        break
for j in range(len(array)-1):#转数字列表
    a=int(array[j])
    array0.append(a)
array1=qsort(array0)#数字列表排序
num=int(len(array)/2)
print(f"{array1[-1]}\n{array1[0]}\n{array[num-1]}")
array1.reverse()#无返回值
for i in range(len(array1)):
    print(array1[i],end=" ")
