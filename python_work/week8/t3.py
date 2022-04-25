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


def path_count(root, sum=0, count=0):  # 注意count的传入与返回
    if root == None or root.val == "None":
        return sum
    elif (root.lchild == None or root.lchild.val == "None") and \
            (root.rchild == None or root.rchild.val == "None"):
        sum += count * 10 + int(root.val)
        return sum
    count = count * 10 + int(root.val)
    sum = path_count(root.lchild, sum, count)
    sum = path_count(root.rchild, sum, count)
    return sum


arr = list(input().split())
T1 = BTree()
for elem in arr:
    T1.add(elem)

print(path_count(T1.root))
