class Node():
    def __init__(self, elem="None", lchild=None, rchild=None):
        self.val = elem
        self.lchild = lchild
        self.rchild = rchild


class BTree():
    def __init__(self):
        self.root = Node()
        self.myqueue = []
        self.lis = []

    def add(self, val):
        l, node = len(self.myqueue), Node(val)  # index of node
        self.myqueue.append(node)
        if l == 0:
            self.root = node
        elif l > 0:
            while self.myqueue[(l - 1) // 2].val == "None":
                self.myqueue.append(Node("None"))
                self.myqueue.append(Node("None"))
                l = len(self.myqueue)
            if l % 2 == 1:
                self.myqueue[(l - 1) // 2].lchild = node
            else:
                self.myqueue[(l - 1) // 2].rchild = node

    def count_k(self, k, c=0):
        if 2 ** (k - 1) - 1 >= len(self.myqueue):
            return 0
        else:
            m = 2 ** (k - 1) - 1
            n = 2 ** k - 1
            for j in range(m, n):
                if self.myqueue[j] != None and self.myqueue[j].val != "None":
                    c += int(self.myqueue[j].val)
        return c


arr = list(input().split())
k = int(input())
T1 = BTree()
for elem in arr:
    T1.add(elem)
print(T1.count_k(k))
