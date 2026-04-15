#include <stdio.h>
#include <stdlib.h>

void display( int var, int *p);
void update(int *p2);

int main() {
    int var = 15;
    int *p;

    p = &var;

    display(var, p);

    update(&var);

    display(var, p);

    printf("\n\nPressione ENTER para sair.");

    fflush(stdout);

    getchar();
    return 0;
}

void display(int var, int *p) {
    printf("\n\n");
    printf("Conteúdo de var = %d\n", var);
    printf("Endereço de var = %p\n", &var);
    printf("Conteúdo apontado por p = %d\n", *p);
    printf("Endereço apontado por p = %p\n", p);
    printf("Endereço de p           = %p\n", &p);
}

void update(int *p2) {
    *p2 = *p2 + 1;
}

// Ponteiros:
// *p : o apontado por, conbteúdo do endereço da variável que p aponta
//  p : o endereço da variável
// &p : o endereço do ponteiro