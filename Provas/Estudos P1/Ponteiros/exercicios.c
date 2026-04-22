#include <stdio.h>

// Ex01: Escreva uma função void swap(int *a, int *b) que receba dois ponteiros para inteiros e inverta os valores das variáveis originais.
void swap(int *a, int *b)
{
    int valor1 = *a;
    int valor2 = *b;

    *a = valor2;
    *b = valor1;
}

// Ex02: Escreva uma função int soma_array(int *arr, int tamanho) que calcule a soma de todos os elementos de um array sem usar colchetes [] dentro da função.
int soma_array(int *arr, int tamanho)
{
    int soma = 0;

    for (int i = 0; i < tamanho; i++)
    {
        soma = soma + *(arr + i);
    }
    return soma;
}

// Ex03: Escreva uma função void encontra_min_max(char *s, char *min, char *max) que percorra uma string s e encontre o caractere com o menor e o maior valor ASCII.
void encontra_min_max(char *s, char *min, char *max)
{
    *min = *s;
    *max = *s;

    while (*s != '\0')
    {
        if (*s > *max)
        {
            *max = *s;
        }
        if (*s < *min)
        {
            *min = *s;
        }
        s++;
    }
}

int main(void)
{
    // Ex01
    int x = 5;
    int y = 10;

    swap(&x, &y);

    printf("%d\n", x);
    printf("%d\n", y);


    printf("\n");


    // Ex02
    int vetor[] = {1, 2, 3, 4};

    printf("%d", soma_array(&vetor[0], 4));


    printf("\n");


    // Ex03
    char palavra[] = "fatec";
    char menor, maior;

    encontra_min_max(palavra, &menor, &maior);

    printf("%c %c", menor, maior);

    return 0;
}