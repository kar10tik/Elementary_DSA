class Node:
	
	def __init__(self, num):
		self.data = num
		self.next = None

class Queue_LL:
	
        def __init__(self):
                self.front = None
                self.rear = None

        def isempty(self):
                return self.front == None
	
        def enqueue(self, num):
                temp = Node(num)

                if not self.rear:
                        self.front = self.rear = temp
                        return
                self.rear.next = temp
                self.rear = temp

        def dequeue(self):	
                if self.isempty(): 
                        print("Queue empty!")
                        return
                temp = self.front
                self.front = temp.next
                if (not self.front):
                        self.rear = None
                return temp.data

        def display(self):
                temp = self.front
                if (self.isempty()): 
                        print("Queue empty!")
                        return
                print("The nodes are:", end = " ")
                while (temp):
                    print(temp.data, "->", end = " ")
                    temp = temp.next
                print()

print("Welcome to the Queue-Linked List Program!")
arr = Queue_LL()
ch = 'y'
while (ch == 'y' or ch == 'Y'):
        print("Choices")
        print("1. Enqueue an element")
        print("2. Dequeue an element")
        print("3. View the entire queue")
        print("4. Exit")
        try:
                choice = int(input("Enter your choice"))
                if (choice == 1):
                        data=int(input("Enter the value to insert"))
                        arr.enqueue(data)
                if (choice == 2):
                        print("Dequeued value is", arr.dequeue())
                if (choice == 3):
                        arr.display()
                if (choice == 4):
                        break
                if choice not in [i for i in range(5)]:
                        print("Invalid Choice!")
                ch=input("Do you want to perform another operation?")
        except ValueError:
                print("Enter an integer!")