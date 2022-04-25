import re

str = input()
k = re.findall(r"dividend = (-?\d+), divisor = (-?\d+)", str)  # 负号注意
if k == [] or k[0][1] == '0':
    print("No")
else:
    print(int(k[0][0]) // int(k[0][1]))
