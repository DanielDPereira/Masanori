#include <stdio.h>
#include <stdlib.h>

#define ELEMENTOS_FILA 4

typedef struct {
    int vetor[ELEMENTOS_FILA];
    int fim;
} Fila;

int main(void) {
    Fila f;
    f.fim = 0;   // inicializando a fila vazia

    // incluir elementos na fila
    f.vetor[f.fim] = 10;
    f.fim ++;

    f.vetor[f.fim] = 20;
    f.fim ++;

    f.vetor[f.fim] = 30;
    f.fim ++;

    // excluir elemento
    printf("Elemento saindo da fila: %d\n", f.vetor[0]);

    // deslocamento da fila
    // f.vetor[0] = f.vetor[1];
    // f.vetor[1] = f.vetor[2];
    // f.fim --;   ultima posicao recuou

    // deslocar elemento por elemento em uma lista grande é inviável, por isso é usado o laço for

    for (int i = 0; i < (f.fim - 1); i++)   // f.fim é 0, então eu preciso parar o laço uma posição antes
    {
        f.vetor[i] = f.vetor[i+1];
    };
    f.fim --;

    // imprimir fila
    for (int i = 0; i < f.fim; i++)
    {
        printf("%02d ", f.vetor[i]);
    };

    return 0;
}
