#Priority Queue Implementation Using Array
#Here, priority is the numeric value of the integer
class qprior():

    def __init__(self, size):
        self.size = size
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def insert(self, data):
        if (self.is_full()):
            print("Queue is full!")
            return
        self.queue.append(data)

    def delete(self):
        if (self.is_empty()):
            print("Queue is empty!")
            return

        prior = max(self.queue)
        self.queue.remove(prior)
        return prior
    
    def highest_priority(self):
        if (not self.is_empty()):
            return max(self.queue)
        
    def display(self):
        if (self.is_empty()):
            print("Empty queue!")
            return
            
        print("Elements in the priority queue are: ", end = " ")
        print(' '.join(list(map(lambda x: str(x), self.queue))))
        if(self.is_full()):
            print("Queue is full!")

print("Welcome to the Priority Queue Program!")
num=int(input("How many elements to keep in the queue? (max 20) "))
q = qprior(num)
ch = 'y'
while (ch == 'y' or ch == 'Y'):
    print("Choices")
    print("1. Enqueue an element")
    print("2. Dequeue the highest priority element (element with maximum value)")
    print("3. View the highest priority element in the queue")
    print("4. View the entire queue")
    print("5. Exit")
    choice = int(input("Enter your choice "))
    if (choice == 1):
        data = int(input("Enter the element to enqueue "))
        q.insert(data)
    if (choice == 2):
        print ("Dequeued value = ", q.delete())
    if (choice == 3):
        print("The highest-priority element is ", q.highest_priority())
    if (choice == 4):
        q.display()
    if (choice == 5):
        break
    if (choice not in [i for i in range(6)]):
        print("Invalid Choice!")
    ch = input("Do you want to perform another operation? ")