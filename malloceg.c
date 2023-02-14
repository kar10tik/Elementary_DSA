//Malloc Function Practice
#include <stdio.h>
#include <stdlib.h>
#define PI 3.14
int main()
{
    int n, *ptr;
    puts("Enter no of elements");
    scanf("%d", &n);
    ptr = (int*)calloc(n, sizeof(int));
    for (int i=0; i<n; i++)
    {
        ptr[i] = (i+1)*2;
        printf("%d, ", ptr[i]);
    }
    return 0;
}