array=list(input().split())
d=dict()
for key in array:
    d[key]=d.setdefault(key,0)+1
key=input()
k=d[key]
array1=[]
for value in d.values():
    array1.append(value)
    array1.sort(reverse=True)
for i in range(len(array1)):
    if k==array1[i]:
        print(1,end=" ")
    else:
        print(0,end=" ")

