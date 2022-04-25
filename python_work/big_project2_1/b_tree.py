class Node:
    def __init__(self, parent=None):
        self.keys = []
        self.parent: Node = parent
        self.ptr = []

    def insert(self, key):  # 已经找到插入节点，插入
        if key in self.keys:
            pass
        else:
            self.keys.append(key)
            self.keys.sort()
        return len(self.keys)

    def comp(self, key):  # 找key刚好小于的ptr[i]的下标i,除非为叶子节点或者已经存在
        l = len(self.keys)
        if self.ptr == [] or key in self.keys:  # 找到叶子节点，或者已经有key了
            return None
        for i in range(l):
            if key < self.keys[i]:
                return i
        return l

    def get_in_parent_ptr_pos(self):  # 返回在parent.ptr的下标
        if self.parent is not None:
            return self.parent.ptr.index(self)
        else:
            return None

    def get_keys_len(self):  # 返回keys长度
        return len(self.keys)


class b_tree:
    def __init__(self, m):
        self.root = Node()
        self.m = m
        self.mid_index = int((self.m - 1) / 2)  # 裂开要取出的那个元素下标

    def find(self, k, node: Node = None):  # 从node开始递归找k应该插入的节点
        if not node:  # 妙
            _node = self.root
        else:
            _node = node
        result = _node.comp(k)
        if result == None:
            return _node
        else:
            return self.find(k, _node.ptr[result])

    def split(self, node: Node):
        if len(node.keys) <= self.m - 1:
            return
        parent = node.parent
        new_node, l_node, r_node = Node(), Node(), Node()
        mid_index = self.mid_index  # 分配 keys, 找到提升的值
        l_node.keys = node.keys[0:mid_index]
        center = node.keys[mid_index]
        r_node.keys = node.keys[mid_index + 1:]
        if node.ptr:  # 如果非叶子节点
            l_node.ptr = node.ptr[0:mid_index + 1]  # 分配 ptr
            r_node.ptr = node.ptr[mid_index + 1:]
            for i in range(mid_index + 1):  # 改父节点
                node.ptr[i].parent = l_node
            for i in range(mid_index + 1, self.m + 1):
                node.ptr[i].parent = r_node
        if not parent:  # 没有父节点
            parent = new_node
            parent.keys.append(center)
            parent.ptr.insert(0, l_node)
            parent.ptr.insert(1, r_node)
            l_node.parent = parent
            r_node.parent = parent
            self.root = parent
            return
        l_node.parent = parent  # 有父节点
        r_node.parent = parent
        parent.insert(center)
        index = parent.ptr.index(node)
        parent.ptr.pop(index)
        parent.ptr.insert(index, l_node)
        parent.ptr.insert(index + 1, r_node)
        return self.split(parent)  # 递归

    def rotate(self, node: Node, b_node: Node, parent: Node, pre):  # 不会出现b_node不是叶子节点的情况，因为非叶子节点删除后均自下往上补位
        if pre is None:  # b_node为右兄弟
            return self.lrotate(node, b_node, parent)
        else:
            return self.rrotate(node, b_node, parent)

    def lrotate(self, node: Node, b_node: Node, parent: Node):  # b_node在右边
        node.insert(parent.keys.pop(0))
        parent.insert(b_node.keys.pop(0))
        return

    def rrotate(self, node: Node, b_node: Node, parent: Node):  # b_node在左边
        pos = node.get_in_parent_ptr_pos()
        node.insert(parent.keys.pop(pos - 1))
        parent.insert(b_node.keys.pop(-1))
        return

    def merge(self, node: Node, in_parent_ptr_pos):  # 自下往上调整
        if not node.parent:
            return
        if node.get_keys_len() >= self.mid_index:  # 叶子节点删完第一个元素任然大于等于mid_index
            return
        parent = node.parent
        if in_parent_ptr_pos > 0:
            pre = parent.keys[in_parent_ptr_pos - 1]  # 补上去的地方
            b_node = parent.ptr[in_parent_ptr_pos - 1]  # 左边的兄弟节点
        else:  # 递归到第一次替换前的位置就可能出现 == 0情况
            pre = None
            if len(parent.ptr) == 1:
                return
            b_node = parent.ptr[1]  # 右边的兄弟节点
        if b_node.get_keys_len() > self.mid_index:  # 兄弟大于mid_index
            return self.rotate(node, b_node, parent, pre)
        # 兄弟节点等于mid_index, 合并两个节点,并插入它们正上方的父节点的那个key
        if pre is None:  # 合并ptr
            node.insert(parent.keys.pop(0))
            b_node.ptr = node.ptr + b_node.ptr
        else:  # 合并ptr
            node.insert(parent.keys.pop(in_parent_ptr_pos - 1))
            b_node.ptr = b_node.ptr + node.ptr
        b_node.keys += node.keys  # 合并keys
        b_node.keys.sort()
        parent.ptr.remove(node)
        if parent.get_keys_len() == 0 and parent.parent is None:  # 无父节点的父节点且父节点由于合并没了
            self.root = b_node
            return
        elif parent.get_keys_len() < self.mid_index:  # 递归向上合并调整
            return self.merge(parent, parent.get_in_parent_ptr_pos())
        else:
            pass
        return

    def step_cover(self, node: Node, key_pos):  # 自上往下递归删除，并从下往上调整
        if node.ptr == []:
            return self.merge(node, node.get_in_parent_ptr_pos())  # 从叶子节点往上调整
        after = node.ptr[key_pos + 1]  # 如果node不是叶子节点，就将恰好位于key右下方的节点的最小值补上来
        node.insert(after.keys.pop(0))  # 相当于删除了after的第一个key
        return self.step_cover(after, 0)  # 往下递归直到为叶子节点


    def add(self, key):
        node = self.find(key)  # 找到要插入的节点
        l = node.insert(key)  # 返回插入后长度
        if l == self.m:
            self.split(node)  # 递归分裂

    def search(self, key):
        node = self.find(key)
        if key in node.keys:
            return node
        else:
            return None

    def delete(self, key):
        node = self.find(key)  # 找到要删除位置
        if node is None or key not in node.keys:
            return
        else:
            key_pos = node.keys.index(key)
            node.keys.remove(key)
            self.step_cover(node, key_pos)  # 调整

    def level_order_print(self, root):
        if not root:
            return None
        curlevel = [[root]]
        back = []
        while curlevel:
            temp = []
            nextlevel = []
            for elem in curlevel:
                for node in elem:
                    temp.extend(node.keys)
                    if node.ptr:
                        nextlevel.append(node.ptr)
            back.extend(temp)
            curlevel = nextlevel
        for t in back:
            print(t, end=" ")