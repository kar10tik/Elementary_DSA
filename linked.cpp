#include <iostream>
#include <unistd.h> //for NULL
#include <stdio.h>
#include <cstdio>
using namespace std;

struct node
    {
        int data;
        node *next;
    };

node *head = NULL;

void insert_b(int x) //Insert node in beginning
{
    head = new node;
    head->data = x;
    head->next = NULL;
}

void insert_m(int x, int pos) //Insert node in the middle
{
    node *p = head; node *mid;
    mid = new node;
    for (int i = 2; i <= pos-1; i++) 
    {
        p = p->next;
        if (!p) break;
    }
    if (p)
    {

    }
    p->next = new node;
    p = p->next;
    p->data = x;
    p->next = NULL;
}

void insert_e(int x) //Insert node in the end
{
    node *p = head;
    while (p->next) p = p->next;
    p->next = new node;
    p = p->next;
    p->data = x;
    p->next = NULL;
}

void display()
{
    node *p = head;
    while (p)
    {
        cout << p->data << "";
        p = p->next;
    }
}

void delete_b(int n) //Delete node from beginning
{
    ;
}

void delete_m(int n) //Delete middle node
{
    node *p=head;
    for (int i=1; i<n-1;i++) p=p->next;
    node *q=p->next;
    q=q->next;
    delete q;
}

void delete_e(int n) //Delete node in the end
{
    ;
}

int main()
{
    char next='y';
    int choice, e;
    cout << "Welcome to Stack Menu!\n";
    cout << "The stack size is 10\n"; //Try to input stack size from user
    do{
        cout << "Choices:" << endl;
        cout << "1. Push an element into the stack" << endl;
        cout << "2. Pop an element from the stack" << endl;
        cout << "3. View the entire stack" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice:" << endl;
        cin >> choice;
        cin >> ws;
        switch (choice)
            {
            case 1:
                cout << "Enter element to push into the stack" << endl;
                cin >> e;
                cin >> ws;
                
                break;
            
            case 2:
                
                break;
            
            case 3:
                display();
                break;

            case 4:
                exit(0);
                break;

            default:
                cout << "Invalid Choice!" << endl;
                break;
            }
        cout <<"Do you want to perform another operation? Enter y if yes" << endl;
        cin >> next;
    
    }while (next=='y' || next=='Y');
    return 0;
}