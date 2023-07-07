#Program to implement linked list
import sys
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None  # Initialize next as null

class Linked_List:

    def __init__(self):
        self.head = None
   
    def insert_node_b(self, x): 
        #Insert in beginning
	    node_b = Node(x)
	    node_b.next = self.head
	    self.head = node_b
    
    def delete_node_b(self): 
        #Delete node in the beginning
        del_b = self.head
        if (del_b):
            self.head = del_b.next
            del_b = None
            return
    
    def search(self, x):
        current = self.head
        while (current != None):
            if current.data == x:
                return True # data found
            current = current.next
        return False
    
    def display(self):
        temp = self.head
        print("The nodes are:", end = " ")
        while (temp):
            print(temp.data, end = " ")
            temp = temp.next

    def rev_list(self, temp):
        if temp:
            self.rev_list(temp.next)
            print(temp.data, end = ' ')
        else: return

print("Welcome to the Linked List Program!")
link = Linked_List()
ch = 'y'
while (ch == 'y' or ch == 'Y'):
    print("Choices")
    print("1. Insert a node at the beginning")
    print("2. Delete the node at the beginning")
    print("3. Check if a node exists (Search)")
    print("4. Display the linked list")
    print("5. Display the linked list in reverse order")
    print("6. Exit")
    choice = int(input("Enter your choice "))
    
    if (choice == 1):
        data = int(input("Enter the value to insert "))
        link.insert_node_b(data)

    if (choice == 2):
        link.delete_node_b()

    if (choice == 3):
        data = int(input("Enter the node to search for "))
        if(link.search(data)):
            print("Node found!")
        else: print("Not found")

    if (choice == 4):
        link.display()

    if (choice == 5):
        link.rev_list(link.head)

    if (choice == 6):
        sys.exit(0)

    if choice not in [i for i in range(7)]:
        print("Invalid Choice!")

    ch = input("Do you want to perform another operation? ")