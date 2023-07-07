//SLL in C++
#include <iostream>
#include <cstdlib>
#include <bits/stdc++.h>

using namespace std;

class Node
{
    public:
        Node *next;
        int data;
};

Node *head = NULL;

// Insert a node at the stack top
void insert_node_b(int x)
{
    head = new Node();
    head -> data = x;
    head -> next = NULL;
}

// Insert a node in the middle of the stack
void insert_node_m(int n)
{
    Node *p = head;
    for (int i = 0; i < n-1; i++)
        p = p -> next;
    Node *q = p -> next;
}

// Insert a node at the end of the stack
void insert_node_e(int x)
{
    Node *p = head;
    while (p -> next)
        p = p -> next;
    p -> next = new Node();
    p = p -> next;
    p -> data = x;
    p -> next = NULL;
}

// Delete a node from the beginning of the stack
void delete_node_b()
{
    if (head == NULL)
        return;
 
    Node* temp = head;
    head = head->next;
    delete temp;
}

// Delete a node from the middle of the stack
void delete_node_m(int n)
{
    Node *p = head;
    for (int i = 0; i < n-1; i++)
        p = p -> next;
    Node *q = p -> next;
    p -> next = p -> next -> next;
    delete q;
}

// Delete a node from the end of the stack
void delete_node_e()
{
    Node *p = head;
    if(p == NULL)  
    cout << "List is empty";  
    else if(p -> next == NULL)  
        {  
            p = NULL;  
            free(p);  
            cout << "Only node of the list deleted" << endl;  
        }  
    
    else  
        {  
        p = head;   
        while(p -> next != NULL)  
            {  
                p = p ->next;  
            }  
        p -> next = NULL;  
        free(p);  
        }
}

// Display the stack
void display()
{
    Node *p = head;
    while (p)
    {
        cout << p -> data << " ";
        p = p -> next; 
    }
}

bool search(Node* head, int x)
{
    Node* current = head;
    while (current != NULL)
    {
        if (current->data == x)
            return true;
        current = current->next;
    }
    return false;
}

int main()
{
    Node* head = NULL;
    int x = 21;
    insert_node_b(10);
    insert_node_b(30);
    insert_node_b(11);
    insert_node_b(21);
    insert_node_b(14);
    search(head, 25) ? cout<< "Yes" : cout << "No";
    return 0;
}