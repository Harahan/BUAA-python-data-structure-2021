num=int(input())
a=True
if num<=1:
    a=False
else:
    for i in range(2,int(num/2)):#除法加int
        if num%i==0:
            a=False
            break
if a:
    print("Y")
else:
    print("N")