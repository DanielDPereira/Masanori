#include<stdio.h>
#include<stdlib.h>

// struct para um item da lista que possui um inteiro
struct ElementoLista
{
    int valor;
    struct ElementoLista *prox;   // ponteiro que aponta para o próximo elemento da lista
};

// define um novo tipo de dados (item)
typedef struct ElementoLista Item;

void imprime(Item *cabeca)
{
    // esse item aponta para o item atual sendo impresso
    // como o item do início é a cabeça, a impressão começa no próximo item
    Item *atual = cabeca->prox;

    // laço que executa até o último item
    int i = 0;
    while (atual != NULL)
    {
        printf("Valor do item: %3d\n", atual->valor);
        i++;

        // faz o atual mover para o próximo item
        atual = atual->prox;
    }

    printf("Total de itens na lista: %d\n", i);
}

void insereFim(Item *cabeca, int valor)
{
    // cria um ponteiro para o novo item e aloca dinamicamente
    Item *novo = (Item*)malloc(sizeof(Item));

    // inicializa novo item
    novo->prox = NULL;      // se torna o último da lista
    novo->valor = valor;    // conteudo do Item

    // varre a lista do começo para chegar na última posição
    Item *atual = cabeca;
    while (atual->prox!=NULL)
    {
        atual = atual->prox;
    }
    
    atual->prox = novo;
}

void libera(Item *cabeca)
{
    // ponteiro para o início da lista
    Item *atual = cabeca->prox;

    // ponteiro para o item a ser liberado
    Item *liberado;

    // parte do início da lista eliminando todos os itens
    while (atual != NULL)
    {
        // o libereado recebe o endereço do atual a ser liberado
        liberado = atual;

        // o atual recebe o  endereço do próximo a ser liberado
        atual = atual->prox;

        printf("Liberando o item de valor %3d na posicao %000000X\n", liberado->valor, liberado);

        // libera o atual
        free(liberado);
    }
}

int main(int argc, char *argv[])
{
    // crio a cabeça da lista
    Item cabeca;
    cabeca.prox = NULL;     // vazia, não aponta para nada (indica o fim da lista)

    // imprimo o tamanho em bytes de um item
    printf("Tamanho do item: %d bytes\n", sizeof(Item));

    // insere ao final da lista um item alocado dinamicamente
    printf("\nInserindo itens novos na lista...\n");
    insereFim(&cabeca, 15);
    insereFim(&cabeca, 125);
    insereFim(&cabeca, 155);

    // aguardo o usuário pressionar uma tecla
    system("PAUSE");

    // funcao para imprimir os itens da lista
    printf("\nImprimindo itens da lista...\n");
    imprime(&cabeca);

    // aguardo o usuário pressionar uma tecla
    system("PAUSE");

    // funcao para liberar a memoria
    printf("\nLiberando a memória dos itens da lista...\n");
    libera(&cabeca);

    return 0;
}