array=list(input())
'''i=0
while i<len(array)-1:
    if array[i]==array[i+1]:
        array.pop(i)
        array.pop(i)
        i=-1
    i+=1
for i in range(len(array)):
    print(array[i],end="")'''
stack=[]

for i in range(len(array)):
    stack.append(array[i])
    if len(stack)>=2 and stack[-1]==stack[-2]:
        stack.pop()
        stack.pop()
for i in range(len(stack)):
    print(stack[i],end="")




