# Python3 program to for tree traversals

# A class that represents an individual node in a
# Binary Tree
#     a
#    /  \
#   b    c
#  / \     \
# d   e     f

# DFS = a, b, d, e, c, f

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A function to do preorder tree traversal
def invertTree(root):
    if not root:  # Base Case
        return root
    invertTree(root.left)  # Call the left substree
    invertTree(root.right)  # Call the right substree
    # Swap the nodes
    root.left, root.right = root.right, root.left
    return root  # Return the root

def treeinclues(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    return treeinclues(root.left, target) or treeinclues(root.right, target)

def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)

if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    # print("Preorder traversal of binary tree is")
    # printPreorder(a)
    # x = invertTree(a)
    print(treeinclues(a, '5'))
