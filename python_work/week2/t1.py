array=list(input())
array[0]=array[0].lower()
i=1
while i < len(array) :
    if array[i]<'a':
        array.insert(i,'_')
        i+=1
        array[i]=array[i].lower()
    i+=1
for i in range(len(array)):
    print(array[i],end='')




