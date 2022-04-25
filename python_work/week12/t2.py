import re

v = [0]*100

def bfs(g, start, N):
	q = []
	vis = [0] * (N + 5)
	q.append(start)
	vis[start] = 1
	while q != []:
		x = q.pop(0)
		print(chr(x + ord("A")), end=" ")  # chr asicl转字母
		for i in range(N):
			if g[x][i] == 1 and vis[i] == 0:
				q.append(i)
				vis[i] = 1

def dfs(g, start, N):
	global v
	if v[start] == 1:
		return
	v[start] = 1
	print(chr(start + ord("A")), end=" ")
	for i in range(N):
		dfs(g, i, N)


if __name__ == '__main__':
	a = input().split()
	N = int(a[0])
	start = a[1]
	mat = [[] for i in range(N + 5)]
	for i in mat:
		for j in range(N + 5):
			i.append(0)
	for i in range(N):
		line = input()
		p = re.compile("[A-Z]:[0-9]+")
		l = re.findall(p, line)
		for item in l:
			mat[ord(line[0]) - ord('A')][ord(item[0]) - ord('A')] = int(item[2:])  # ord 字母转 ascil
	# bfs(mat, ord(start) - ord("A"), N)
	dfs(mat, ord(start) - ord("A"), N)
'''
4 A
A: {B:1, C:1, D:1}
B: {A:1, C:1, D:1}
C: {A:1, B:1, D:1}
D: {A:1, B:1, C:1}
'''
