class rb_node():
    def __init__(self, val, lchild = None, rchild =None, parent =None, color="red"):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
        self.parent = parent
        self.color = color


class rb_tree():
    def __init__(self):
        self.root = None

    def find(self, val, root: rb_node):
        if root is None:
            return None
        if val < root.val:
            self.find(val, root.lchild)
        elif val > root.val:
            self.find(val, root.rchild)
        else:
            return root

    def find_min(self, node: rb_node):
        while node.lchild is not None:
            node = node.lchild
        return node

    '''
    def find_max(self, node: rb_node):
        while node.rchild is not None:
            node = node.rchild
        return node
    '''

    def transplant(self, u: rb_node, v: rb_node):  # 用v替代u,相当于使v的父节点与u一致，支持替换空节点
        if u.parent is None:
            self.root = v
        elif u == u.parent.lchild:
            u.parent.lchild = v
        else:
            u.parent.rchild = v
        # v.color = u.color  # 替换不改变颜色
        if v is not None:
            v.parent = u.parent

    def l_rotate(self, node: rb_node):  # 注意改父节点
        p = node.rchild
        node.rchild = p.lchild
        if p.lchild is not None:
            node.rchild.parent = node
        p.lchild = node
        p.parent = node.parent
        node.parent = p
        if p.parent is None:
            self.root = p
        else:  # 改grand节点的子节点
            if p.parent.lchild == node:
                p.parent.lchild = p
            else:
                p.parent.rchild = p

    def r_rotate(self, node: rb_node):  # 注意改父节点
        p = node.lchild
        node.lchild = p.rchild
        if p.rchild is not None:
            node.lchild.parent = node
        p.rchild = node
        p.parent = node.parent
        node.parent = p
        if p.parent is None:
            self.root = p
        else:  # 改grand节点的子节点
            if p.parent.lchild == node:
                p.parent.lchild = p
            else:
                p.parent.rchild = p

    def add_fix(self, node: rb_node):
        # father 为黑色不用进入循环调整
        while node.parent is not None and node.parent.color == "red":  # 只要进入循环就必有祖父节点，否则父节点就是根节点为黑色，矛盾
            if node.parent == node.parent.parent.lchild:
                uncle = node.parent.parent.rchild
                if uncle is not None and uncle.color == "red":  # 刚开始有uncle，一定为红色，father,uncle置黑，grand置红
                    node.parent.color = "black"
                    uncle.color = "black"
                    uncle.parent.color = "red"
                    node = uncle.parent
                    continue
                # 刚开始uncle为黑色，即没有uncle
                elif node == node.parent.rchild:  # 插在lr，先左旋，再交换此时father,grand颜色，再右旋
                    self.l_rotate(node.parent)  # 传一个指针
                    node = node.lchild  # ！！！
                node.parent.color = "black"  # 插在ll，交换此时father,grand颜色，再右旋
                node.parent.parent.color = "red"
                self.r_rotate(node.parent.parent)
                return
            elif node.parent == node.parent.parent.rchild:
                uncle = node.parent.parent.lchild
                if uncle is not None and uncle.color == "red":  # 刚开始有uncle，一定为红色，father,uncle置黑，grand置红
                    node.parent.color = "black"
                    uncle.color = "black"
                    uncle.parent.color = "red"
                    node = uncle.parent
                    continue
                # 刚开始uncle为黑色，即没有uncle
                elif node == node.parent.lchild:  # 插在rl,先右旋，再交换此时father,grand颜色，再左旋
                    self.r_rotate(node.parent)
                    node = node.rchild  # ! ! ！
                node.parent.color = "black"  # 插在rr，交换此时father,grand颜色，再左旋
                node.parent.parent.color = "red"
                self.l_rotate(node.parent.parent)
                return
        self.root.color = "black"  # 保持根节点颜色
        return

    def delete_fix(self, node: rb_node, father: rb_node):  # node有可能是根节点
        # 只有一棵子树 node.color 为红色
        if node is not None and node.color == "red":
            node.color = "black"
            return
        # 没有子树，node is None，必有brother，如果没有，则删除那个节点为红色（唯一子树一定为红）就不会进来
        # 由于None也被认为是一个黑色节点故要调整
        while (node is None or node.color == "black") and node != self.root:
            if (node is None and father.lchild == None) or (node is not None and node == father.lchild):  # 左孩子
                brother = father.rchild
                # brother.color == "red"
                if brother.color == "red":  # 必有两个黑色的孩子
                    father.color = "red"
                    brother.color = "black"
                    self.l_rotate(father)
                    brother = father.rchild
                # brother.color == "black"
                if (brother.lchild is None or brother.lchild.color == "black")and \
                (brother.rchild is None or brother.rchild.color == "black") :  # parent为红或黑，brother为黑，brother无孩子
                    brother.color = "red"
                    node = father  # parent为黑（思考），需要进行下一轮调整，parent为红直接出循环，然后令它为黑
                else:  # brother为黑且有孩子
                    # 无右孩子
                    if brother.rchild is None or brother.rchild.color == "black":
                        brother.color = "red"
                        brother.lchild.color = "black"
                        self.r_rotate(brother)
                        brother = father.rchild
                    # 有右孩子
                    brother.color = father.color
                    father.color = "black"
                    brother.rchild.color = "black"
                    self.l_rotate(father)
                    break
            else:  # 右孩子
                brother = father.lchild
                # brother.color == "red"
                if brother.color == "red":  # 必有两个黑色的孩子
                    father.color = "red"
                    brother.color = "black"
                    self.r_rotate(father)
                    brother = father.lchild
                # brother.color == "black"
                if (brother.lchild is None or brother.lchild.color == "black") and \
                (brother.rchild is None or brother.rchild.color == "black"):  # parent为红或黑，brother为黑，brother无孩子
                    brother.color = "red"
                    node = father  #parent为黑（思考），需要进行下一轮调整，parent为红直接出循环，然后令它为黑
                else:  # brother为黑且有孩子
                    #无左孩子
                    if brother.lchild is None or brother.lchild.color == "black":
                        brother.color = "red"
                        brother.rchild.color = "black"
                        self.l_rotate(brother)
                        brother = father.lchild
                    # 有左孩子
                    brother.color = father.color
                    father.color = "black"
                    brother.lchild.color = "black"
                    self.r_rotate(father)
                    break
        if self.root is not None:
            self.root.color = "black"
        return

    def add(self, val):
        node, father, son = rb_node(val), None, self.root
        while son is not None:
            father = son
            if val == son.val:
                return
            elif val < son.val:
                son = son.lchild
            else:
                son = son.rchild
        if father is None:  # 无根节点
            self.root = node
            node.color = "black"
            return
        elif node.val < father.val:
            father.lchild = node
            node.parent = father
        else:
            father.rchild = node
            node.parent = father
        self.add_fix(node)  # 调整树

    def search(self, root: rb_node, val):
        if root is None:
            return root
        if root.val > val:
            return self.search(root.lchild, val)
        elif root.val < val:
            return self.search(root.rchild, val)
        else:
            return root

    def delete(self, val):  # 注意transplant已经更改了根节点了
        node = self.search(self.root, val)
        if node is None:
            return
        color = node.color  # 要删除节点的颜色
        # 若只有一棵子树必然该子树只有一个节点， 注意只有一颗子树，该子树必为红色，该节点为黑色 ！ ！ ！
        # 若为叶子节点，为红色，无需调整，为黑色就调整
        if node.lchild is None:
            p = node.rchild
            father = node.parent
            self.transplant(node, node.rchild)
        elif node.rchild is None:
            p = node.lchild
            father = node.parent
            self.transplant(node, node.lchild)
        else:  # 既有左子树又有右子树,用右子树中最小的替代，注意替代后颜色不变，转为上面两种情况
            node_min = self.find_min(node.rchild)
            color = node_min.color
            p = node_min.rchild
            father = node_min.parent
            if node_min.parent != node:
                self.transplant(node_min, node_min.rchild)
                node_min.rchild = node.rchild  # ! ! !
                node_min.rchild.parent = node_min
            self.transplant(node, node_min)
            node_min.lchild = node.lchild
            node_min.lchild.parent = node_min
            node_min.color = node.color  # 颜色不变
        if color == "black":  # 要删除节点颜色为黑色
            self.delete_fix(p, father)  # 传入被替换之后的节点，至多只有一棵子树
        return

    def level_order_print(self, root: rb_node):
        if root is None:
            return
        que = [root]
        back = []
        while que:
            temp = []
            nextque = []
            for node in que:
                temp.append((node.val, node.color))
                if node.lchild is not None:
                    nextque.append(node.lchild)
                if node.rchild is not None:
                    nextque.append(node.rchild)
            back.extend(temp)
            que = nextque
        for t in back:
            print(t, end=" ")
