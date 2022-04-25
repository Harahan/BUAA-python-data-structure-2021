stack = []


def print_postorder(p, i):
    if p == []:
        return
    stack.append(p[0])
    k, l = i.index(p[0]), len(i)
    print_postorder(p[k + 1:l], i[k + 1:l])  # right
    print_postorder(p[1:k + 1], i[0:k])  # left


preorder = list(input().split())
inorder = list(input().split())
print_postorder(preorder, inorder)
while stack != []:
    print(stack.pop(), end=" ")
