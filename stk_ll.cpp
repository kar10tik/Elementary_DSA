//Stack Using Linked List
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

class Node
{
    public:
        Node *next;
        int data;
};

Node *head = NULL;

void push(int x)
{
    Node *p = new Node;
    p -> data = x;
    p -> next = head;
    head = p;
}

bool isunderflow()
{
    if (head == NULL)
        return true;
    return false;
}

int pop()
{
    if (isunderflow())
    {
        cout << "Stack empty" << endl;
        return -99;
    }
    Node* temp = head;
    head = head->next;
    return temp -> data;
    delete temp;
}

int peek()
{
    if (not isunderflow())
    return head -> data;
    return -99; 
}

void display()
{
    Node *p = head;
    if (isunderflow())
    {
        cout << "Stack empty" << endl;
        return;
    }
    while (p)
    {    
        cout << p -> data << " ";
        p = p -> next; 
    }
}

int main()
{
    char next='y';
    int choice, e;
    do{
        cout << "Stack Using LL" << endl;
        cout << "Choices:" << endl;
        cout << "1. Push an element into the stack " << endl;
        cout << "2. Pop an element from the stack (-99 if empty)" << endl;
        cout << "3. View the entire stack " << endl;
        cout << "4. Peek (-99 if empty)" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice: " << endl;
        cin >> choice;
        switch (choice)
            {
            case 1:
                cout << "Enter element to push into the stack ";
                cin >> e;
                push(e);
                break;
            
            case 2:
                if (!isunderflow())
                {
                    cout << "Popped element is " << pop() << endl;
                } 
                else cout << "Stack empty!";
                break;
            
            case 3:
                cout << "The stack is: ";
                display();
                break;

            case 4:
                cout << "The top element is " << peek() << endl;
                break;

            case 5:
                exit(0);

            default:
                cout << "Invalid Choice!";
                break;
            }
        cout << "Do you want to perform another operation? Enter y if yes";
        cin >> next;
    
    }while (next=='y' || next=='Y');
    return 0;
}