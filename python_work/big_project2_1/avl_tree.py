class avl_node():
    def __init__(self, val, lchild=None, rchild=None, height=1):
        self.val = val
        self.lchild: avl_node = lchild
        self.rchild: avl_node = rchild
        self.height = height


class avl_tree():
    def __init__(self):
        self.root = None

    def update(self, node: avl_node):
        return max(self.get_height(node.lchild), self.get_height(node.rchild)) + 1

    def get_height(self, node: avl_node):
        if node is None:
            return 0
        return node.height

    def get_max(self, node: avl_node):
        if node.rchild is not None:
            return self.get_max(node.rchild)
        else:
            return node

    def get_min(self, node: avl_node):
        if node.lchild is not None:
            return self.get_min(node.lchild)
        else:
            return node

    def r_rotate(self, node: avl_node):
        p = node.lchild
        node.lchild = p.rchild
        p.rchild = node
        node.height = self.update(node)
        p.height = self.update(p)
        return p

    def l_rotate(self, node: avl_node):
        p = node.rchild
        node.rchild = p.lchild
        p.lchild = node
        node.height = self.update(node)
        p.height = self.update(p)
        return p

    def rl_rotate(self, node: avl_node):
        node.rchild = self.r_rotate(node.rchild)
        node = self.l_rotate(node)
        return node

    def lr_rotate(self, node: avl_node):
        node.lchild = self.l_rotate(node.lchild)
        node = self.r_rotate(node)
        return node

    def add(self, root: avl_node, val):
        if root is None:
            root = avl_node(val)
            return root
        elif root.val > val:
            root.lchild = self.add(root.lchild, val)
            root.height = self.update(root)
            if self.get_height(root.lchild) - self.get_height(root.rchild) == 2:
                if val < root.lchild.val:
                    root = self.r_rotate(root)
                else:
                    root = self.lr_rotate(root)
        elif root.val < val:
            root.rchild = self.add(root.rchild, val)
            root.height = self.update(root)
            if self.get_height(root.rchild) - self.get_height(root.lchild) == 2:
                if val > root.rchild.val:
                    root = self.l_rotate(root)
                else:
                    root = self.rl_rotate(root)
        return root

    def search(self, root: avl_node, val):
        if root is None:
            return None
        if root.val > val:
            return self.search(root.lchild, val)
        elif root.val < val:
            return self.search(root.rchild, val)
        else:
            return root

    def delete(self, root: avl_node, val):
        if root is None:
            return None
        if root.val < val:
            root.rchild = self.delete(root.rchild, val)
            root.height = self.update(root)
            if self.get_height(root.lchild) - self.get_height(root.rchild) == 2:
                if self.get_height(root.lchild.lchild) >= self.get_height(root.lchild.rchild):
                    root = self.r_rotate(root)
                else:
                    root = self.lr_rotate(root)
        elif root.val > val:
            root.lchild = self.delete(root.lchild, val)
            root.height = self.update(root)
            if self.get_height(root.rchild) - self.get_height(root.lchild) == 2:
                if self.get_height(root.rchild.rchild) >= self.get_height(root.rchild.lchild):
                    root = self.l_rotate(root)
                else:
                    root = self.rl_rotate(root)
        else:
            if root.lchild is not None and root.rchild is not None:
                if self.get_height(root.lchild) >= self.get_height(root.rchild):
                    p = root.lchild
                    p = self.get_max(p)
                    root.val = p.val
                    root.lchild = self.delete(root.lchild, p.val)
                    root.height = self.update(root)
                else:
                    p = root.rchild
                    p = self.get_min(p)
                    root.val = p.val
                    root.rchild = self.delete(root.rchild, p.val)
                    root.height = self.update(root)
            else:
                if root.lchild is not None:
                    root = root.lchild
                elif root.rchild is not None:
                    root = root.rchild
                else:
                    root = None
        return root

    def level_order_print(self, root: avl_node):
        if root is None:
            return
        que = [root]
        back = []
        while que:
            temp = []
            nextque = []
            for node in que:
                temp.append(node.val)
                if node.lchild is not None:
                    nextque.append(node.lchild)
                if node.rchild is not None:
                    nextque.append(node.rchild)
            back.extend(temp)
            que = nextque
        for t in back:
            print(t, end=" ")



