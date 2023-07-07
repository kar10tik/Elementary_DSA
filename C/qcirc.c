#include <stdio.h>
#include <stdlib.h>
struct circq
{
    int front;
    int maxnum;
    int *array;
};
int q[10], rear, front; //q is an array/queue of integers

void initialize()
{
    rear=0;
    front=-1;
}

int isoverflow()
{
    if (q[front]!=0 && q[rear]!=0) return 1;
    return 0;
}

int isunderflow()
{
    if (front==rear-1) return 1;
    return 0;
}

int enqueue(int z)
{
    if (isoverflow())
    {
        puts("Queue is full!");
        return 999;
    }
    if (q[rear]==0 && q[front]!=0)
    {
        q[rear]=q[front];
        q[front]=0;
    }
    q[rear]=z;
    rear+=1;
    return 1;
}

int dequeue()
{
    if (isunderflow()) 
    {
        puts("Queue is already empty!");
        return 999;
    }
    return q[front];
    front++;
}

void show()
{
    int i;
    if (isunderflow()) puts("Queue empty!");
    else
    {
        for (i=0; i<10; i++)
        {
            if (q[i]==0) break;
            else printf("%d\t",q[i]);
        }    
    puts(" ");
    }
}

int main()
{
    puts("Program to implement circular queue");
    initialize();
    char next='y';
    int choice, e;
    puts("Welcome to Queue Menu!");
    puts("The queue size is 10"); //Try to input queue size from user
    do{
        puts("Choices:");
        puts("1. Enqueue an element (except 0)");
        puts("2. Dequeue an element");
        puts("3. View the entire queue");
        puts("4. Exit");
        puts("Enter your choice:");
        scanf("%d", &choice);
        fflush(stdin);
        switch (choice)
            {
            case 1:
                puts("Enter element to enqueue");
                scanf("%d", &e);
                fflush(stdin);
                enqueue(e);
                break;
            
            case 2:
                dequeue();
                break;
            
            case 3:
                show();
                break;

            case 4:
                exit(0);
                break;

            default:
                puts("Invalid Choice!");
                break;
            }
        puts("Do you want to perform another operation? Enter y if yes");
        scanf("%c", &next);
    
    }while (next=='y' || next=='Y');
    return 0;
}