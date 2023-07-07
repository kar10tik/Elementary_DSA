#Program to implement circular queues
class qcirc():

	def __init__(self, size):
		self.size = size
		self.queue = [None for i in range(size)] #initialize
		self.front = self.rear = -1

	def is_full(self):
		if ((self.rear + 1) % self.size == self.front): 
			return 1 

	def is_empty(self):
		if(self.front == -1): 
			return 1

	def enqueue(self, x):
		if (self.is_full()):
                    print("Queue is Full")

		if ((not self.is_full()) and self.front == -1):
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = x

		elif (not self.is_full()):
			self.rear = (self.rear + 1) % self.size
			self.queue[self.rear] = x
			
	def dequeue(self):
		if (self.is_empty()):
			print("Queue is empty!")
			return

		if (self.front == self.rear): #iff one element only
			temp=self.queue[self.front]
			self.front = -1
			self.rear = -1
			return temp

		temp = self.queue[self.front]
		self.front = (self.front + 1) % self.size
		return temp

	def display(self):
		if self.is_empty():
			print("Queue empty!")

		elif (self.rear >= self.front):
			print("Elements in the circular queue are:", end = " ")
			for i in range(self.front, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()
			if self.is_full(): print("Queue is full") 

		else:
			print ("Elements in Circular Queue are: ", end = " ")
			for i in range(self.front, self.size):
				print(self.queue[i], end = " ")
			for i in range(0, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()
			if self.is_full(): print("Queue is full")

print("Welcome to the Circular Queue Program!")
num = int(input("How many elements to keep in the queue? (max 20) "))
q = qcirc(num)
ch = 'y'
while (ch == 'y' or ch == 'Y'):
	print("Choices")
	print("1. Enqueue an element")
	print("2. Dequeue an element")
	print("3. View the entire queue")
	print("4. Exit")
	choice = int(input("Enter your choice "))
	if (choice == 1):
		data = int(input("Enter the element to enqueue "))
		q.enqueue(data)
	if (choice == 2):
		if (q.is_empty()):
			pass
		else:
			print("Dequeued value ", q.dequeue())
	if (choice == 3):
		q.display()
	if (choice == 4):
		break
	if choice not in [i for i in range(5)]: 
		print("Invalid Choice!")
	ch = input("Do you want to perform another operation? ")
