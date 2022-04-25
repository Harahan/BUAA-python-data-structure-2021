def matches(open,close):
    opens="{[(<"
    closes="}])>"
    return opens.index(open)==closes.index(close)

array=list(input())
stack=[]
flag=True
for i in range(len(array)):
    if array[i] in "{[(<":
        stack.append(array[i])
    elif array[i] in "}]>)" :
        if len(stack)!=0 and matches(stack[-1],array[i]):
                stack.pop()
        else:
            flag=False
            break
    else:
        pass
if flag and len(stack)==0:
    print("Yes")
else:
    print("No")



