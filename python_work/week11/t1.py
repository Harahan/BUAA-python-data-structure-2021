class Node:
    def __init__(self):
        self.keys = []
        self.parent = None
        self.ptr = []

    def insert(self, key): # 叶子节点，非满, 分裂时用
        if key in self.keys:
            pass
        else:
            self.keys.append(key)
            self.keys.sort()
        return len(self.keys)

    def comp(self, key): # 找ptr[i]的下标i,除非为叶子节点或者已经存在
        l = len(self.keys)
        if self.ptr == [] or key in self.keys: # 找到叶子节点，或者已经有key了
            return None
        for i in range(l):
            if key < self.keys[i]:
                return i
        return l


class B_tree:
    def __init__(self, m):
        self.root = Node()
        self.m = m
        self.mid_index = int((self.m - 1) / 2) #裂开要取出的那个元素下标

    def find(self, k, node: Node = None):# 从node开始递归找k应该插入的节点
        if not node: # 妙
            _node = self.root
        else:
            _node = node
        result = _node.comp(k)
        if result is None:
            return _node
        else:
            return self.find(k, _node.ptr[result])

    def split(self, node: Node):
        if len(node.keys) <= self.m - 1:
            return 0
        parent = node.parent
        new_node, l_node, r_node = Node(), Node(), Node()
        mid_index = self.mid_index # 分配 keys, 找到提升的值
        l_node.keys = node.keys[0:mid_index]
        center = node.keys[mid_index]
        r_node.keys = node.keys[mid_index + 1:]
        if node.ptr:# 如果非叶子节点
            l_node.ptr = node.ptr[0:mid_index + 1] # 分配 ptr
            r_node.ptr = node.ptr[mid_index + 1:]
            for i in range(mid_index + 1): # 改父节点
                node.ptr[i].parent = l_node
            for i in range(mid_index + 1, self.m + 1):
                node.ptr[i].parent = r_node
        if not parent: # 没有父节点
            parent = new_node
            parent.keys.append(center)
            parent.ptr.insert(0, l_node)
            parent.ptr.insert(1, r_node)
            l_node.parent = parent
            r_node.parent = parent
            self.root = parent
            return 0
        l_node.parent = parent # 有父节点
        r_node.parent = parent
        parent.insert(center)
        index = parent.ptr.index(node)
        parent.ptr.pop(index)
        parent.ptr.insert(index, l_node)
        parent.ptr.insert(index + 1, r_node)
        return self.split(parent) #递归

    def insert(self, key):
        node = self.find(key)
        l = node.insert(key)
        if l == self.m:
            self.split(node)

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


m = int(input())
T = B_tree(m)
a = input().split()
for key in a:
    T.insert(int(key))
T.level_order_print(T.root)






