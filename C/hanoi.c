//Program to simulate steps involved in the solution of Towers of Hanoi
//Complexity 2**n (exp)
#include <stdio.h>
#include <string.h>
int hanoirecur(int n_disc, char tow1, char tow2, char tow3) //tow1=src, tow2=dst, tow3=aux
{
    if (n_disc==1)
    {
        printf("Move disc 1 from stick %c to stick %c \n", tow1, tow2);
        return 0;
    }
    hanoirecur(n_disc-1, tow1, tow3, tow2); //Relocate discs from tow1 to tow3 using tow2
    printf("Move disc %d from stick %c to stick %c\n", n_disc, tow1, tow2);
    hanoirecur(n_disc-1, tow3, tow2, tow1); //Relocate discs from tow3 to tow2 using tow1
}

int main()
{
    puts("Recursive solution to Towers of Hanoi");
    int n;
    puts("How many discs?");
    scanf("%d",&n);
    fflush(stdin);
    int r1[3], r2[3], r3[3];
    hanoirecur(n, 'A', 'C', 'B'); //r1, r2, r3 are src, aux, and dst rods/sticks
    return 0;
}