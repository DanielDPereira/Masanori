#include <stdio.h>
#include <stdlib.h>

int main() {
    int var = 15;
    // estou armazenando var em um endereço na memória e colocando o conteúdo 15 dentro dela

    int *p;
    // declarando um ponteiro

    p = &var;
    // apontando para o endereço de var (estou atribuindo a p o conteúdo e endereço de var)

    printf("Conteúdo de var = %d\n", var);
    printf("Endereço de var = %p\n", &var);
    printf("Conteúdo apontado por p = %d\n", *p);
    printf("Endereço apontado por p = %p\n", p);
    printf("Endereço de p           = %p\n", &p);

    *p = 73;
    // atribuindo 73 como conteúdo da variável apontada pelo ponteiro
    // estou utilizando o ponteiro para atualizar o conteúdo do endereço onde a variável var está

    printf("\n\n");
    printf("Conteúdo de var = %d\n", var);
    printf("Endereço de var = %p\n", &var);
    printf("Conteúdo apontado por p = %d\n", *p);
    printf("Endereço apontado por p = %p\n", p);
    printf("Endereço de p           = %p\n", &p);

    printf("\n\nPressione ENTER para sair.");

    fflush(stdout);

    getchar();
    return 0;
}

// Ponteiros:
// *p : o apontado por (conteúdo do endereço da variável que p aponta)
//  p : o endereço da variável
// &p : o endereço do ponteiro