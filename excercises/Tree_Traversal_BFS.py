class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key



def LevelOrder(root):
    h = height(root)
    for i in range(h+1):
        CurrentLevel(root,i)

def CurrentLevel(root,level):
    if root:
        if level == 1:
            print root.val,
        else:
            CurrentLevel(root.left, level-1)
            CurrentLevel(root.right,level-1)
    else:
        return 0


def height(root):
    if root:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
    else:
        return 0


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

LevelOrder(root)
