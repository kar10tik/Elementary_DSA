//Stack Menu Program
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//Globals
int top, A[10];

void initialize()
{
    top = 0;
}

int isoverflow()
{
    if (top == 10) return 1;
    return 0;
}

int isunderflow()
{
    if (top == 0) return 1;
    return 0;
}

void push(int x)
{
    if (isoverflow()) puts("Stack is full!");
    else
    {
        A[top] = x;
        top ++;
    }
}

int pop()
{
    if (isunderflow())
    {
        puts("Stack is empty!");
        return -999;
    }
    int temp=A[top-1];
    top--;
    A[top]=0;
    return temp;
}

void show()
{
    int i;
    if (isunderflow()) puts("Empty!");
    else
    {
        for (i=top-1; i>=0; i--)
        {
            //if (A[i]==0) break;
            printf("%d\t", A[i]);
        }
        
    puts(" ");
    }
}

int main()
{
    char next='y';
    int choice, e;
    puts("Welcome to Stack Menu!");
    puts("The stack size is 10");
    do{
        puts("Choices:");
        puts("1. Push an element into the stack");
        puts("2. Pop an element from the stack");
        puts("3. View the entire stack");
        puts("4. Exit");
        puts("Enter your choice:");
        scanf("%d", &choice);
        fflush(stdin);
        switch (choice)
            {
            case 1:
                puts("Enter element to push into the stack");
                scanf("%d", &e);
                fflush(stdin);
                push(e);
                break;
            
            case 2:
                if (!isunderflow())
                {
                    printf("Popped element is %d", pop());
                    printf("\n");
                } 
                else puts("Stack empty!");
                break;
            
            case 3:
                printf("The stack is: ");
                show();
                break;

            case 4:
                exit(0);
                break;

            default:
                puts("Invalid Choice!");
                break;
            }
        puts("Do you want to perform another operation? Enter y or Y if yes");
        scanf("%c", &next);
    
    }while (next=='y' || next=='Y');
    return 0;
}