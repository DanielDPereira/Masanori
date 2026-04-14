#include<stdio.h>

int main(void)
{
    int x = 10;

    int *y = &x; // atribuo o endereço de x à variável y

    printf("%d\n", x); // valor de x
    printf("%d\n", *y); // valor apontado por y (valor de x)
    printf("%p\n", &x); // endereço de x
    printf("%p\n", y); // valor de y (endereço de x)
    printf("%p\n", &y); // endereço de y
}