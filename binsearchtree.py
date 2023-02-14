#Binary Search Tree ADT Implementation
import sys
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def insert(data, root):
    if (not root): 
        return Node(data)
    else:
        if (root.val == data):
            return root
        elif (root.val < data):
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root
 
def inorder(root):
    traverse = 'y'
    while (traverse == 'y' or traverse == 'Y'):
        if root:
            inorder(root.left)
            print(root.val)
            inorder(root.right)
        traverse = input("\nDo you want to traverse this tree again (y) or exit (e)? ")
    if (traverse == 'e' or traverse == 'E'):
        sys.exit(0)

root = Node(int(input("Enter the root node value ")))
create = 'y'
while (create == 'y'):
    num = int(input("Enter a node value to insert "))
    root = insert(num, root)
    create = input("Do you want to add another number? ")
inorder(root)