#Program to find sum, difference, and product of two polynomials using Linked Lists
import sys
class Node:

    def __init__(self, num, power):
        self.coeff = num
        self.exp = power
        self.next = None

class poly:
	
    def __init__(self):        
        self.head = None
    
    def construct_node(self, head1, num, power):
        #nomial is the input string
        polyc = Node(num, power)
        if (not head1):
            return polyc
        ptr = head1
        while (ptr.next):
            ptr = ptr.next
        ptr.next = polyc
        return head1

    def show(self):
        temp = self.head
        while (temp.next):
            print(str(temp.coeff)+ 'x^' + str(temp.exp), end = ' ')
            if(temp.next and temp.next.coeff >= 0):
                print('+', end = ' ')
            temp = temp.next
        print(temp.coeff)

    def add_poly(self, poly1, poly2):
        summed = poly()
        temp1 = poly1.head
        temp2 = poly2.head
        while (temp1 and temp2):
            if (temp1.exp == temp2.exp):
                summed.coeff = temp1.coeff + temp2.coeff
                temp1.next
                temp2.next
        print("Sum is:", end = '')
        summed.show()   

    def difference_poly(self, poly1, poly2):
        diff = poly()
        temp1 = poly1.head
        temp2 = poly2.head
        while (temp1 and temp2):
            if (poly1.temp1.exp == poly2.temp2.exp):
                diff.coeff = temp1.coeff - temp2.coeff
                temp1.next
                temp2.next
        print("Difference is:", end = '')
        diff.show()

    def multiply_poly(self, poly1, poly2):
        ptr1 = poly1
        ptr2 = poly2

        while (ptr1 != None):
            while (ptr2 != None):
                coeff = ptr1.coeff * ptr2.coeff
                power = ptr1.power + ptr2.power
                poly3 = construct_node(poly3, coeff, power)
                ptr2 = ptr2.next
            ptr2 = poly2
            ptr1 = ptr1.next
        return poly3

ch = 'y'
print("Program to find sum, difference, and product of two polynomials using Linked Lists")

while (ch == 'y' or ch == 'Y'):
    print("Input single-variable polynomials in the following format")
    print("ax^n + ... + bx^6 + cx^5 + ... + kx^1 + zx^0")
    p1 = input("Enter polynomial 1 ")
    p2 = input("Enter polynomial 2 ")

    term1 = p1.split("+")
    
    poly1 = poly()
    for i in range(len(term1)):
        term = term1[i].split("x^")
        poly1 = poly1.construct_node(poly1, int(term[0]), int(term[1]))
    
    poly2 = poly()
    term2 = p2.split("+")
    for j in range(len(term2)):
        term = term2[i].split("x^")
        poly2 = poly2.construct_node(poly2, int(term[0]), int(term[1]))
        
    print(poly1.head)
    poly1.show()
    poly2.show()
    print("Choices")
    print("1. Add the two polynomials")
    print("2. Subtract the two polynomials")
    print("3. Multiply the two polynomials")
    print("4. Exit")
    choice = int(input("Enter your choice "))

    if (choice == 1):
        add_poly(poly1, poly2)
        
    if (choice == 2):
        difference_poly(poly1, poly2)

    if (choice == 3):
        multiply_poly(poly1, poly2)

    if (choice == 4):
        sys.exit(0)
        
    if choice not in [i for i in range(5)]:
        print("Invalid Choice!")
    
    ch = input("Do you want to perform another operation? ")