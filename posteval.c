#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int top; int stack[10];
void initialize()
{
    top=0;
}

int isoverflow()
{
    if (top==10) return 1;
    return 0;
}

int isunderflow()
{
    if (top==0) return 1;
    return 0;
}

void push(int x)
{
    if (isoverflow()) puts("Stack is full!");
    else
    {
        stack[top]=x;
        top++;
    }
}

int pop()
{
    if (isunderflow())
    {
        puts("Stack is empty!");
        return -999;
    }
    int temp=stack[top-1];
    top--;
    return temp;
}

int main()
{
    char exp[10];
    puts("This program evaluates a postfix expression");
    puts("Enter a postfix expression with numbers and operators only");
    gets(exp);
    int i, o1, o2, res;
    while (exp[i]!='\0')
    {
        if (isdigit(exp[i])) push((int) exp[i]-48);
        if (exp[i]=='+') 
        {
            o1=pop();
            o2=pop();
            res=o1+o2;
            push(res);
        }
        if (exp[i]=='-')
        {
            o1=pop();
            o2=pop();
            res=o1-o2;
            push(res);
        }
        if (exp[i]=='*')
        {
            o1=pop();
            o2=pop();
            res=o1*o2;
            push(res);
        }
        if(exp[i]=='/')
        {
            o1=pop();
            o2=pop();
            res=o1/o2;
            push(res);
        }
        i++;
    }
    printf("The result is %d", stack[top-1]);
    return 0;
}