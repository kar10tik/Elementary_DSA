#Doubly Linked List Implementation
import sys
class Node:

    def __init__(self, next = None, prev = None, data = None):
        self.next = next 
        self.prev = prev
        self.data = data

class double_linked_list:

    def __init__(self):
        self.head = None
    
    def insert_node(self, new_data):
        new_node = Node(data = new_data)
        new_node.next = self.head
        new_node.prev = None

        if (self.head):
            self.head.prev = new_node
        self.head = new_node

    def forward_display(self, node):
        while node:
            print("{}".format(node.data), end = ' ')
            last = node
            node = node.next
        print()

    def reverse_display(self, node):
        while node:
            last = node
            node = node.next
        while last:
            print(" {}".format(last.data), end = ' ')
            last = last.prev
        print()

print("Welcome to the Doubly Linked List Program!")
link = double_linked_list()
ch = 'y'
while (ch == 'y' or ch == 'Y'):
    print("Choices")
    print("1. Insert a node at the beginning")
    print("2. Display the linked list in forward direction")
    print("3. Display the linked list in reverse direction")
    print("4. Exit")
    choice = int(input("Enter your choice "))
    if (choice == 1):
        data = int(input("Enter the value to insert "))
        link.insert_node(data)

    if (choice == 2):
        link.forward_display(link.head)

    if (choice == 3):
        link.reverse_display(link.head)

    if (choice == 4):
        sys.exit(0)
    ch = input("Do you want to perform another operation? ")