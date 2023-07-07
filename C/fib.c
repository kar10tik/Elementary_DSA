// Program to compute sum and print Fibonacci series upto a number n 
// Time Complexity O(n)
#include <stdio.h>

int fibnsum(int n)
{
    if (n<=2) return 1;
    return fibnsum(n-1)+fibnsum(n-2);
}

int fibt(int n)
{
    int f[n+2], i, j;
    f[0] = 0;
    f[1] = 1;
    for (i = 2; i <= n; i++)
    {
        f[i] = f[i-1] + f[i-2];
    }
    for (j = 0; j <= n; j++) 
    {printf("%d  ", f[j]);
    }
    return 0;
}
int main()
{
    int num, fib[num], choice, j;
    char ch = 'y';
    do{
        puts("Fibonacci Program. Choices:");
        puts("1. Calculate sum upto nth term of the Fibonacci series");
        puts("2. Print the Fibonacci series upto nth term");
        puts("Enter your choice");
        scanf("%d", &choice);
        switch(choice)
        {
            case 1:
                puts("Enter the term upto which sum is to be calculated");
                scanf("%d", &num);
                fflush(stdin);
                if (num<0) puts("Negative term!");
                else printf("Sum is %d\n",fibnsum(num));
                break;
            case 2:
                puts("Enter the term upto which series is to be printed");
                scanf("%d", &num);
                fflush(stdin);
                if (num<0) puts("Negative term!");
                else 
                {
                    printf("Series is: ");
                    fibt(num);
                }
                break;
        }
        puts("\nWant to try another num? (y or Y if yes)");
        scanf("%c",&ch);
        fflush(stdin);
        }while(ch=='Y'||ch=='y');
return 0;
}