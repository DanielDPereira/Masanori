#include<stdio.h>
#include<stdlib.h>

// Ex01: Defina uma struct No que contenha um valor inteiro e um ponteiro para o próximo No.
// Em seguida, escreva uma função que crie um novo nó na memória usando malloc e retorne o ponteiro para ele.
typedef struct No
{
    int valor;
    struct No *prox;
} No;

No* novoNo(int valor)
{
    No *novo = (No*)malloc(sizeof(No));

    novo->valor = valor;
    novo->prox = NULL;

    return novo;
}

// Ex02: Escreva uma função void insere_inicio(struct No **cabeca, int valor).
void insere_inicio(No **cabeca, int valor)
{
    No *novo = novoNo(valor);
    novo->prox = *cabeca;   // O novo nó aponta para o antigo primeiro
    *cabeca = novo;   // A cabeça agora aponta para o novo nó
}

// Ex03: Escreva uma função que receba o ponteiro para o primeiro nó e imprima todos os valores da lista até chegar no NULL.
void imprimir(No *cabeca)
{
    No *atual = cabeca;

    while (atual != NULL)
    {
        printf("%d\n", atual->valor);
        atual = atual->prox;
    }
    
}

int main(void)
{
    No *minha_lista = NULL; // Lista começa vazia

    insere_inicio(&minha_lista, 10);
    insere_inicio(&minha_lista, 20);
    insere_inicio(&minha_lista, 30);

    imprimir(minha_lista); // Saída esperada: [30] [20] [10] 

    return 0;
}