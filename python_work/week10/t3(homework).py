class node():
    def __init__(self, val, height=1, lchild=None, rchild=None):
        self.val = val
        self.height = height
        self.lchild = lchild
        self.rchild = rchild


class avl_tree():
    def __init__(self):
        self.root = None

    def update(self, node: node):
        node.height = max(node.lchild.height if node.lchild is not None else 0, \
                          node.rchild.height if node.rchild is not None else 0) + 1

    def rrotate(self, node: node):
        p = node.lchild
        node.lchild = p.rchild
        p.rchild = node
        self.update(node)
        self.update(p)
        return p

    def lrotate(self, node: node):
        p = node.rchild
        node.rchild = p.lchild
        p.lchild = node
        self.update(node)
        self.update(p)
        return p

    def add(self, root: node, key):
        if root is None:
            root = node(key)
            return root
        elif root.val > key:
            root.lchild = self.add(root.lchild, key)
            self.update(root)
            if (root.lchild is not None and root.rchild is not None and \
            root.lchild.height - root.rchild.height == 2) \
            or (root.rchild is None and root.lchild is not None and \
            root.lchild.height == 2):
                if key < root.lchild.val:
                    root = self.rrotate(root)
                else:
                    root.lchild = self.lrotate(root.lchild)
                    root = self.rrotate(root)
        elif root.val < key:
            root.rchild = self.add(root.rchild, key)
            self.update(root)
            if (root.lchild is not None and root.rchild is not None and \
            root.lchild.height - root.rchild.height == -2) \
            or (root.lchild is None and root.rchild is not None and \
            root.rchild.height == 2):
                if key < root.rchild.val:
                    root.rchild = self.rrotate(root.rchild)
                    root = self.lrotate(root)
                else:
                    root = self.lrotate(root)
        return root

    def preprint(self, root: node):
        if root is None:
            return
        else:
            print(root.val, end=" ")
            self.preprint(root.lchild)
            self.preprint(root.rchild)
            return


T = avl_tree()
a = list(input().split())
T.root = T.add(None, a[0])
for i in range(1, len(a)):
    T.root = T.add(T.root, a[i])  # root renew
T.preprint(T.root)
