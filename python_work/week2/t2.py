array=list(input())
for i in range(len(array)):
    array[i]=array[i].lower()
array[0]=array[0].upper()
i=1
while i<len(array)-1:
    if (array[i-1]=='.'and array[i]==' ') or ((array[i]<'a'or array[i]>'z')and \
      (array[i+2]<'a'or array[i+2]>'z')and array[i+1]=='i'):
        i+=1
        array[i]=array[i].upper()
    i+=1
for i in range(len(array)):
    print(array[i],end='')
