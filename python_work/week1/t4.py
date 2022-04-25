num=int(input())
sum=[]
for i in range(num):
    sum+=input().split(" ")
d=dict()
for key in sum:#频率统计
    key=key.lower()
    # setdefault()函数,如果键不存在于字典中，将会添加键并将值设为默认值
    d[key]=d.setdefault(key,0)+1
max=0
for value in d.values():
    if value>max:
        max=value
print(f"{max}")
for key,value in d.items():
    if value==max:
        print(key)
