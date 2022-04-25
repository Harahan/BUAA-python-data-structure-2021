num=int(input())
for i in range(num):
    for j in range(num):
        if j==i:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print("\n")