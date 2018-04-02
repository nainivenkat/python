class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def BinarySearchTree(root, key):
    if root:
        if root.val == key:
            return True
        if root.val < key:
            return BinarySearchTree(root.right,key)
        else:
            return BinarySearchTree(root.left,key)
    else:
        return False   

def insert(root,node):
    if root:
        if root.val < node.val:
            if root.right is None:
                root.right = Node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = Node
            else:
                insert(root.left,node)

def PreOrder(root):
    if root is None:
        return
    print root.val,
    PreOrder(root.left)
    PreOrder(root.right)

def Inorder(root):
    if root is None:
        return
    Inorder(root.left)
    print root.val,
    Inorder(root.right)
    
        
def PostOrder(root):
    if root is None:
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print root.val,


    
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(13)

key = 7
insert(root,Node(30))
print BinarySearchTree(root, key)

PreOrder(root)
print "\n"
Inorder(root)
print "\n"
PostOrder(root)
