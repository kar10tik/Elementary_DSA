#Graph ADT Implementation using Adjacency Lists
class Graph:
    def __init__(self, data):
        self.node = data

print("Welcome to the Graph Implementation Program!")
num = int(input("How many elements to keep in the queue? (max 20)"))
q = Graph(num)
ch = 'y'
while (ch == 'y' or ch == 'Y'):
	print("Choices")
	print("1. Display the Graph")
	print("2. Insert a vertex")
	print("3. Traverse using Depth First Search")
	print("4. Traverse using Breadth First Search")
	print("5. Exit")
	choice = int(input("Enter your choice"))

def delete_node_m(self, data): 
        #Delete node in the middle
        del_m = self.head
        while (del_m):
            if (del_m.data == data): break
            del_before = del_m #del_before is node before node to delete
            del_m = del_m.next
        if(del_m == None):
            return
        del_before.next = del_m.next
        del_m = None

def delete_node_e(self): 
        #Delete node in the end
        last = self.head
        while (last.next):
            del_before = last
            last = last.next
        last.next = del_before.next
        last = None

def insert_node_m(self, prev_node, x): 
        #Insert in middle
	    if (prev_node is None):
		    print("Previous node is in the end.")
		    return
	    new_node = Node(x)
	    new_node.next = prev_node.next
	    prev_node.next = new_node

def insert_node_e(self, x): 
        #Insert node in the end
        node_e = Node(x)
        if self.head is None:
            self.head = node_e
            return
        last = self.head
        while (last.next):
	        last = last.next
        last.next = node_e