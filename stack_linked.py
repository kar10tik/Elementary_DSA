#Program to implement stacks using linked lists
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_LL:

    def __init__(self):
        self.head = None
    
    def isempty(self):
        if self.head == None:
            return True
        else: return False
    
    def push(self, data):
        if self.head == None:
            self.head=Node(data)
        else:
            node_b = Node(data)
            node_b.next = self.head
            self.head = node_b

    def pop(self):
        if self.isempty():
            return None
             
        else:
            del_b = self.head
            self.head = self.head.next
            del_b.next=None
            return del_b.data

    def display(self):

        temp = self.head
        print("The nodes are:", end=" ")
        if (self.isempty()):
            print("Stack empty!")
            return
        while (temp):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print()

print("Welcome to the Stack-Linked List Program!")
arr=Stack_LL()
ch='y'
while (ch=='y' or ch=='Y'):
    print("Choices")
    print("1. Push an element into the stack")
    print("2. Pop an element from the stack")
    print("3. View the entire stack")
    print("4. Exit")
    try:
        choice=int(input("Enter your choice"))
        if (choice==1):
            data=int(input("Enter the value to insert"))
            arr.push(data)
        if (choice==2):
            print("Popped value is", arr.pop())
        if (choice==3):
            arr.display()
        if (choice==4):
            break
        if choice not in [i for i in range(5)]:
            print("Invalid Choice!")
        ch=input("Do you want to perform another operation?")
    except ValueError:
        print("Enter an integer!")