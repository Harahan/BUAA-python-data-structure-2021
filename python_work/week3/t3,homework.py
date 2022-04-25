n=int(input())
stack=[]
for i in range(n):
    word=input()
    if word =="+":
        stack.append(stack[-2]+stack[-1])
    elif word =="D":
        stack.append(2*stack[-1])
    elif word =="C":
        stack.pop()
    else:
        stack.append(int(word))
print(sum(stack))

