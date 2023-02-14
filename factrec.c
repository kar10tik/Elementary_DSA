//Program to compute factorial recursively Time Complexity O(n)
#include <stdio.h>

int fact_rec(int n)
{
    if (n<2) return 1;
    else return n*fact_rec(n-1);
}

int main()
{
    puts("Recursively calculate factorial");
    int n; char ch = 'y';
    do{
        puts("Enter the number");
        scanf("%d",&n);
        fflush(stdin);
        if (n<0) puts("Factorial does not exist!");
        else printf("The factorial of %d is %d\n", n, fact_rec(n));
        puts("Want to try another number? (y or Y if yes)");
        scanf("%c",&ch);
        fflush(stdin);
    }while(ch=='Y'||ch=='y');
    return 0;
}