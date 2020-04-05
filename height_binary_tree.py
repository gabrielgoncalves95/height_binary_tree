class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root):
    root = set_level(root)
    if root is None:
        return 0
    else:
        l_depth = height(root.left)
        r_depth = height(root.right)
        if l_depth > r_depth:
            if root.level > 0:
                return l_depth + 1
            else:
                return l_depth
        else:
            if root.level > 0:
                return r_depth + 1
            else:
                return r_depth


def set_level(root):
    if root is None:
        return root
    if root.level is None:
        root.level = 0
    if root.right is not None and root.right.level is None:
        root.right.level = root.level + 1
    if root.left is not None and root.left.level is None:
        root.left.level = root.level + 1
    return root


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
