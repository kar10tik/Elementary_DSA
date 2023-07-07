//DLL in C++
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

class Node
{
    public:
        Node *next;
        Node *prev;
        int data;
};

Node *head = NULL;

void insert_node_b(Node **ref, int x) //ref is the head pointer
{
    Node *head = new Node();
    head -> data = x;
    head -> next = *ref;
    head -> prev = NULL;
    if ((*ref) != NULL)
        (*ref)->prev = head;
    *ref = head;
}

void insert_node_m(Node *prev_node, int x)
{
    if (prev_node == NULL)
    {
        cout<< "The previous node cannot be NULL" << endl;
        return;
    }

    Node* new_node = new Node();
    new_node -> data = x;
    new_node -> next = prev_node -> next;
    prev_node -> next = new_node;
    new_node->prev = prev_node;
    if (new_node -> next != NULL)
        new_node->next->prev = new_node;
}

void insert_node_e(Node **ref, int x)
{
    Node* new_node = new Node();
    new_node->data = x;
    new_node->next = NULL;
 
    if (*ref == NULL)
    {
        new_node->prev = NULL;
        *ref = new_node;
        return;
    }

    Node* last = *ref;

    while (last->next != NULL)
        last = last->next;
    last->next = new_node;
    new_node->prev = last;
    return;
}

void delete_node_b(Node **ref) //delete the head pointer
{
    *ref -> next -> prev = NULL;
}

void delete_node_m(int n)
{
    Node *p = head;
    for (int i = 0; i < n-1; i++)
        p = p -> next;
    Node *q = p -> next;
    p -> next = p -> next -> next;
    delete q;
}

void delete_node_e()
{
    ;
}

void display()
{
    Node *p = head;
    while (p)
    {
        cout << p -> data << " ";
        p = p -> next; 
    }
}

int search(Node** ref, int x)
{
    Node* temp = *ref;
    int pos = 0;

    while (temp->data != x && temp->next != NULL) {
        pos++;
        temp = temp->next;
    }

    if (temp->data != x)
        return -1;
    return (pos + 1);
}

int main()
{
    return 0;
}