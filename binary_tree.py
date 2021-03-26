
class Node():
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, value):
        self.value = value


obj = BinaryTree(Node(4))

obj.left = Node(3)
obj.left.left = Node(7)
obj.left.right = Node(2)

obj.right = Node(2)
obj.right.left = Node(9)
obj.right.right = Node(10)
obj.right.right.right = 19


print(obj.right.right.right)

