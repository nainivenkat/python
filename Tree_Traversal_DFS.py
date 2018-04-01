class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def preOrder(root):
    if root:
        print root.val,
        preOrder(root.left)
        preOrder(root.right)


def Inorder(root):
    if root:
        preOrder(root.left)
        print root.val,
        preOrder(root.right)

def PostOrder(root):
    if root:
        preOrder(root.left)
        preOrder(root.right)
        print root.val,



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preOrder(root)
print "\n"
Inorder(root)
print "\n"
PostOrder(root)
        
