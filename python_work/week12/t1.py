import re

N = int(input())
mat = [[] for i in range(N)]
for i in mat:
	for j in range(N):
		i.append(0)
for i in range(N):
	line = input()
	p = re.compile("[A-Z]:[0-9]+")
	l = re.findall(p, line)
	for item in l:
		mat[ord(line[0]) - ord("A")][ord(item[0]) - ord("A")] = int(item[2:])

for i in range(N):
	for j in range(N):
		print(mat[i][j], end=" ")
	print()  # 输一个回车
