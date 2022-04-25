class Node:
    def __init__(self,elem = "None", lchild = None, rchild = None):
        self.val = elem
        self.lchild = lchild
        self.rchild = rchild


class BTree:
    def __init__(self):
        self.root = Node()
        self.myqueue = []

    def add(self, val):
        l, node = len(self.myqueue), Node(val) # index of node
        self.myqueue.append(node)
        if l == 0:
            self.root = node
        else:
            if l % 2 == 1:
                self.myqueue[(l - 1) // 2].lchild = node
            else:
                self.myqueue[(l - 1) // 2].rchild = node

    def inorder_print(self, root):
        stack, p = [], root
        while True:
            while p != None and p.val != "None":
                stack.append(p)
                p = p.lchild
            p = stack.pop()
            print(p.val, end = " ")
            if p.rchild != None and p.rchild.val != "None":
                p = p.rchild
            elif stack == []:
                break
            else:
                p = stack.pop()
                print(p.val, end = " ")
                p = p.rchild


arr = list(input().split())
T1 = BTree()
for elem in arr:
    T1.add(elem)
T1.inorder_print(T1.root)

