#Infix to Postfix Convertor
class stack:
    
    def __init__(self, length):
        self.arr = []
        self.top = -1

    def isunderflow(self):
        if self.top == -1: return 1
        return 0

    def isoverflow(self):
        if self.top == 9: return 1
        return 0

    def push(self, elem):
        if (not self.isoverflow()):
            self.top += 1 
            self.arr.append(elem)

    def pop(self):
        if (not self.isunderflow()): 
            self.top -= 1
            return self.arr.pop()
    
    def peek(self):
        return self.arr[-1]

def in_to_post(exp_in):

    precedence = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}
    operators = list(precedence.keys())
    symbols = operators+['(', ')']
    exp = [i for i in exp_in]
    exp.insert(0, '(')
    exp.append(')')
    
    for j in exp:
        if (j == '('): stk.push(j)

        elif (j.isalnum() or (j not in symbols)): 
            post.append(j)

        elif (j == ')'): 
            while(not stk.isunderflow() and stk.peek() != '('): 
                post.append(stk.pop())

            if (not stk.isunderflow() and stk.peek() != '('):
                return -1
            else: stk.pop()
        
        if j in operators:
            try:
                while (not stk.isunderflow() and (precedence[j] <= precedence[stk.peek()])):
                    post.append(stk.pop())
            except KeyError:
                pass
            stk.push(j)

            if (stk.peek() == '('): stk.pop()

    while (not stk.isunderflow()): post.append(stk.pop())    
    print("The postfix equivalent of", ''.join(exp), "is: ", ''.join(post))

print("Program to convert infix to postfix expressions")
choice = 'y'
stk, post = stack(10), []
while (choice == 'y' or choice == 'Y'):
    exp_in = input("Enter an infix expression ")
    in_to_post(exp_in)
    stk.arr.clear(); post.clear()
    choice = input("Do you want to test for another expression? ")