#Program to evaluate result of postfix expression
stack=[]
top=0

def isunderflow():
    if len(stack)==0: return 1
    return 0

def isoverflow():
    if len(stack)==10: return 1
    return 0

def push(elem):
    if (not isoverflow()): 
        stack.append(elem)
        global top
        top+=1

def pop():
    if (not isunderflow()): 
        temp=stack.pop()
        global top
        top-=1
        return temp

operators=['+', '-', '*', '/', '%', '//']
print("This program evaluates a postfix expression")
exp=input("Enter a postfix expression")

for i in range(len(exp)):
    if exp[i].isdigit(): push(int(exp[i]))
    if exp[i] in operators:
        if (exp[i]=='+'):
            res1=pop()
            res2=pop()
            res=res1+res2
            push(res)
        if (exp[i]=='-'):
            res1=pop()
            res2=pop()
            res=res2-res1
            push(res)
        if (exp[i]=='*'):
            res1=pop()
            res2=pop()
            res=res1*res2
            push(res)
        if (exp[i]=='/'):
            res1=pop()
            res2=pop()
            res=res1/res2
            push(res)

print("The result is", pop())