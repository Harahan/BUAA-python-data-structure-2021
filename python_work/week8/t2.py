class Node:
    def __init__(self, elem="None", lchild=None, rchild=None):
        self.val = elem
        self.lchild = lchild
        self.rchild = rchild


class BTree:
    def __init__(self):
        self.root = Node()
        self.myqueue = []

    def add(self, val):
        l, node = len(self.myqueue), Node(val)  # index of node
        self.myqueue.append(node)
        if l == 0:
            self.root = node
        else:
            if l % 2 == 1:
                self.myqueue[(l - 1) // 2].lchild = node
            else:
                self.myqueue[(l - 1) // 2].rchild = node

    def preorder_print(self, root):
        if root == None or root.val == "None":
            return
        else:
            print(root.val, end=" ")
            self.preorder_print(root.lchild)
            self.preorder_print(root.rchild)
            return


arr = list(input().split())
T1 = BTree()
for elem in arr:
    T1.add(elem)

T1.preorder_print(T1.root)
