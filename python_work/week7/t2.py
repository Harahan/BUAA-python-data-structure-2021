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
            if l % 2 == 1:
                self.myqueue[(l - 1) // 2].lchild = node
            else:
                self.myqueue[(l - 1) // 2].rchild = node

    def lchild_count(self, root, sum=0):
        if root == None or root.val == "None":
            return sum;
        if root.val != "None" and \
                (root.lchild != None and root.lchild.val != "None"):
            sum += int(root.lchild.val)
        sum = self.lchild_count(root.lchild, sum)
        sum = self.lchild_count(root.rchild, sum)
        return sum


arr = list(input().split())
T1 = BTree()
for elem in arr:
    T1.add(elem)
print(T1.lchild_count(T1.root))
