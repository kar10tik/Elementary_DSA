#PreOrder
import sys
class Node:
    def __init__(self, num):
        self.data = num
        self.right = None
        self.left = None

def preorder(val):
#Display Binary Tree in Pre-order Traversal
    if (not val): return
    print(val.data, end = " ")
    preorder(val.left)
    preorder(val.right)

def insert_logic(num, arg1):

    if (arg1.data==None):
        root.data = num
        return
    q = []
    q.append(arg1)

    while (len(q)):
        arg1 = q[0]
        q.pop(0)
 
        if (not arg1.left and not arg1.right):
            if (num%2!=0): 
                arg1.left = Node(num)
                break
            elif (num%2==0): 
                arg1.right = Node(num)
                break

        elif (arg1.left != None and arg1.right != None):
            if (num%2 != 0): 
                q.append(arg1.left)
            elif (num%2 == 0): 
                q.append(arg1.right)

        elif(arg1.left or arg1.right):
            if (not arg1.left): 
                arg1.left = Node(num)
                break
            if (not arg1.right): 
                arg1.right = Node(num)
                break

def create_tree():
    create = 'y'
    while (create == 'y'):
        num = int(input("Enter a node value to insert "))
        insert_logic(num, root)
        create = input("Do you want to add another number? ")

def traverse_tree():
    traverse = 'y'
    while (traverse == 'y' or traverse == 'Y'):
        preorder(root)
        traverse = input("\nDo you want to traverse this tree again (y) or change the tree/exit (n)/(e)? ")
    if (traverse == 'e' or traverse == 'E'):
        sys.exit(0)
    if (traverse != 'y' or traverse != 'Y'):
        create_tree()
        traverse_tree()

root = Node(None)
print("Program to create a binary tree and traverse it")
print("Create the numeric-node tree")
create_tree()
traverse_tree()