class Heap:  # binary heap
	def __init__(self):
		self.que = [-1]  # in order to make the index begin from 1
		self.size = 0
	
	def add(self, x: int) -> None:
		self.que.append(x)
		self.size += 1
		s, p = self.size, self.size >> 1
		while s > 1:
			if self.que[s] < self.que[p]:
				self.que[s], self.que[p] = self.que[p], self.que[s]
			else:
				break
			s = p
			p >>= 1
	
	def pop(self, d: int) -> None:
		self.que[d], self.que[-1] = self.que[-1], self.que[d]
		self.size -= 1
		self.que = self.que[:self.size + 1]
		s, p = d << 1, d
		while s <= self.size:
			if s + 1 <= self.size and self.que[s + 1] < self.que[s]:
				s += 1
			if self.que[s] < self.que[p]:
				self.que[s], self.que[p] = self.que[p], self.que[s]
			else:
				break
			p = s
			s <<= 1


def heapsort(a: list) -> None:
	h, length = Heap(), len(a)
	for val in a:
		h.add(val)
	for i in range(length):
		a.append(h.que[1])
		a.pop(0)
		h.pop(1)


def main():
	arr = [-1, 1, 4, 5, 4, 8, 1, 10, 8, 3, 37, 87, 43, 60]
	heapsort(arr)
	print(arr)


if __name__ == '__main__':
	main()
