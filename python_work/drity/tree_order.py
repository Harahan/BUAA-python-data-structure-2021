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

    def postorder_print(self, root):
        stack1, stack2, p = [], [], root
        while True:
            while p != None and p.val != "None":
                stack1.append(p)
                stack2.append(0)
                p = p.lchild
            if stack1 == []:
                break
            p = stack1[-1]
            if stack2[-1] == 0:
                p = p.rchild
                stack2[-1] = 1
            else:
                print(p.val,end=" ")
                stack2.pop()
                stack1.pop()
                p = None
    '''
    def preorder_print(self, root):
        stack, p = [], root
        if p == None or p == "None":
            return
        while True:
            print(p.val, end=" ")
            q = p.rchild
            if q != None and q.val != "None":
                stack.append(q)
            p = p.lchild
            if p == None or p == "None":
                if stack == []:
                    break
                p = stack.pop()
    '''

    def inorder_print(self, root):
        stack, p = [], root
        if p == None or p.val == "None":
            return
        while True:
            while p != None and p.val != "None":
                stack.append(p)
                p = p.lchild
            if stack == []:
                break
            else:
                p = stack.pop()
            print(p.val, end = " ")
            p = p.rchild


    def preorder(self, root):
        stack, p = [], root
        if p == None or p == "None":
                return
        while True:
            while p is not None and p.val != 'None':
                print(p.val, end=" ")
                if p.rchild is not None and p.rchild.val != 'None':
                    stack.append(p.rchild)
                p = p.lchild
            if stack == []:
                return
            else:
                p = stack.pop()


    def levelorder_print(self, root):
        p, que, j = root, [], 1
        if p == None or p == "None":
            return
        que.append(p)
        while True:
            if p.lchild != None and p.lchild.val != "None":
                que.append(p.lchild) 
            if p.rchild != None and p.rchild.val != "None":
                que.append(p.rchild) 
            if j == len(que):
                break
            p, j = que[j], j+1
        while que != []:
            print(que.pop(0).val, end=" ")

arr = list(input().split())
T1 = BTree()
for elem in arr:
    T1.add(elem)
T1.preorder(T1.root)
