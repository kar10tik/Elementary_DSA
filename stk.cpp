#include <iostream>
#include <bits/stdc++.h>

using namespace std;

#define MAX 10

class Stack
{
    int top;

    public:
        int a[MAX];
        Stack() {top = 0;}
        bool push(int x);
        int pop();
        int peek();
        bool isunderflow();
        bool isoverflow();
        void show();
};

bool Stack :: push(int x)
{
    if (top >= MAX) 
    {
        cout << "Stack Overflow" << endl;
        return false;
    }
    else
    {
        a[top++] = x;
        cout << x << " pushed into stack" << endl;
        return true;
    }
}

bool Stack :: isoverflow()
{
    return (top > MAX);
}

bool Stack :: isunderflow()
{
    return (top == 0);
}

int Stack :: peek()
{
    if (isunderflow())
    {
        cout << "Stack is Empty!" << endl;
        return false;
    }
    return a[top];
}

int Stack :: pop()
{
    if (isunderflow())
    {
        cout << "Stack is Empty!" << endl;
        return false;
    }
    int x = a[top--];
    return x; 
}

void Stack :: show()
{
    if (isunderflow())
    cout << "Stack Empty!" << endl;
    else
    {
        for (int i = top - 1; i >= 0; i--)
            //if (A[i]==0) break;
            cout << a[i];
    cout << endl;
    }
}

int main()
{
    class Stack s;
    char next = 'y';
    int choice, e;
    cout << "Welcome to Stack Menu!" << endl;
    cout << "The stack size is 100" << endl;
    do{
        cout << "Choices:" << endl;
        cout << "1. Push an element into the stack" << endl;
        cout << "2. Pop an element from the stack" << endl;
        cout << "3. View the entire stack" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice:";
        cin >> choice;
        switch (choice)
            {
            case 1:
                cout << "Enter element to push into the stack ";
                cin >> e;
                s.push(e);
                break;
            
            case 2:
                if (!s.isunderflow())
                {
                    cout << "Popped element is " << s.pop() << endl;
                } 
                else cout << "Stack empty!" << endl;
                break;
            
            case 3:
                cout << "The stack is: ";
                s.show();
                break;

            case 4:
                exit(0);
                break;

            default:
                cout << "Invalid Choice!" << endl;
                break;
            }
        cout << "Do you want to perform another operation? Enter y or Y if yes" << endl;
        cin >> next;
    
    }while (next=='y' || next=='Y');
    return 0;
}