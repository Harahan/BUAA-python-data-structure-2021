class Node:
    def __init__(self, elem="None", lchild=None, rchild=None):
        self.val = elem
        self.lchild = lchild
        self.rchild = rchild


class BTree:
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

    def list_leaf(self, root):
        if root == None or root.val == "None":
            return
        if root.val != "None" and \
                (root.lchild == None or root.lchild.val == "None") and \
                (root.rchild == None or root.rchild.val == "None"):
            self.lis.append(root.val)
        self.list_leaf(root.lchild)
        self.list_leaf(root.rchild)


arr = list(input().split())
buf = list(input().split())
T1 = BTree()
T2 = BTree()
for elem in arr:
    T1.add(elem)
for elem in buf:
    T2.add(elem)
T1.list_leaf(T1.root)
T2.list_leaf(T2.root)
if T1.lis == T2.lis:
    print(True)
else:
    print(False)
