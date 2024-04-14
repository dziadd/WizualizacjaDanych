#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//int main() {
//    printf("Wprowadz tekst: ");
//    int c;
//    while ((c = getchar()) != '\n' && c != EOF) {
//        if (islower(c))
//            putchar(toupper(c));
//        else if (isupper(c))
//            putchar(tolower(c));
//        else
//            putchar(c);
//    }
//    return 0;
//}


//int main() {
//    int mala_litera = 0, duza_litera = 0, cyfra = 0;
//    char c;
//
//    printf("Wprowadz tekst: ");
//
//    while ((c = getchar()) != '\n') {
//        if (islower(c))
//            mala_litera++;
//        else if (isupper(c))
//            duza_litera++;
//        else if (isdigit(c))
//            cyfra++;
//    }
//
//    printf("Male litery: %d\n", mala_litera);
//    printf("Duze litery: %d\n", duza_litera);
//    printf("Cyfry: %d\n", cyfra);
//
//    return 0;
//}




//int main() {
//    int c;
//    while ((c = getchar()) != EOF) {
//        if (c == '\t') {
//            printf("    ");
//        } else {
//            putchar(c);
//        }
//    }
//    return 0;
//}


//int main() {
//    int c;
//    while ((c = getchar()) != EOF) {
//        putchar(c);
//        putchar(c);
//    }
//    return 0;
//}


//int main() {
//    char c;
//    while ((c = getchar()) != EOF) {
//        printf("%d ", c);
//    }
//    return 0;
//}

//gcc main.c -o char_to_code



//int main() {
//    const int N = 1000;
//    int n;
//
//    printf("Podaj liczbe z przedzialu [1, %d]: ", N);
//    scanf("%d", &n);
//
//    srand(time(0));
//
//    int tabela[n];
//
//
//    for (int i = 0; i < n; i++) {
//        tabela[i] = rand() % 100 + 1;
//    }
//
//    for (int i = 0; i < n; i++) {
//        printf("%d ", tabela[i]);
//    }
//
//    for (int i = 0; i < n; ++i) {
//        if (tabela[i] <= 0) {
//            continue;
//        }
//        if (tabela[i] % 2 == 1) {
//            tabela[i] = 3 * tabela[i] + 1;
//        } else {
//            do {
//                tabela[i] /= 2;
//            } while (tabela[i] % 2 == 0);
//        }
//    }
//    printf("\n");
//
//    for (int i = 0; i < n; i++) {
//        printf("%d ", tabela[i]);
//    }
//
//
//    return 0;
//}



//int main() {
//    const int N = 1000;
//    int n;
//
//    printf("Podaj liczbe z przedzialu [1, %d]: ", N);
//    scanf("%d", &n);
//
//    srand(time(0));
//
//    int tabela[n];
//
//    for (int i = 0; i < n; i++) {
//        tabela[i] = rand() % 100 + 1;
//        printf("%d ", tabela[i]);
//    }
//    printf("\n");
//
//    int lewy, prawy;
//    printf("Podaj liczbe 'lewy' (0 <= lewy < %d): ", n);
//    scanf("%d", &lewy);
//    printf("Podaj liczbe 'prawy' (0 <= prawy < %d): ", n);
//    scanf("%d", &prawy);
//
//
//    if (lewy < 0 || lewy >= n || prawy < 0 || prawy >= n) {
//        printf("Niepoprawne wartosci 'lewy' lub 'prawy'. Zakres to [0, %d).\n", n);
//        return 1;
//    }
//
//
//    while (lewy < prawy) {
//        int temp = tabela[lewy];
//        tabela[lewy] = tabela[prawy];
//        tabela[prawy] = temp;
//        lewy++;
//        prawy--;
//    }
//
//
//    int parzyste = 0, nieparzyste = 0;
//    for (int i = 0; i < n; ++i) {
//        if (tabela[i] % 2 == 0) {
//            parzyste++;
//        } else {
//            nieparzyste++;
//        }
//    }
//
//    printf("Odwrocona tablica:\n");
//    for (int i = 0; i < n; i++) {
//        printf("%d ", tabela[i]);
//    }
//    printf("\n");
//
//    printf("Ilosc parzystych elementow: %d\n", parzyste);
//    printf("Ilosc nieparzystych elementow: %d\n", nieparzyste);
//
//
//    int max = tabela[0];
//    int imax = 1;
//    for (int i = 1; i < n; ++i) {
//        if (tabela[i] > max) {
//            max = tabela[i];
//            imax = 1;
//        } else if (tabela[i] == max) {
//            imax++;
//        }
//    }
//
//    printf("Najwiekszy element: %d\n", max);
//    printf("Ilosc wystapien najwiekszego elementu: %d\n", imax);
//
//    return 0;
//}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 1000

void print_array(int tab[], int n) {
    for (int i = 0; i < n; ++i) {
        printf("%d ", tab[i]);
    }
    printf("\n");
}

void generuj(int* tabela, int* n){

    printf("Podaj liczbe z przedzialu [1, %d]: ", N);
    scanf("%d", n);

    srand(time(0));

    for (int i = 0; i < *n; i++) {
        tabela[i] = rand() % 100 + 1;
    }

    print_array(tabela, *n);
}

void collatz(int tab[], int n) {
    for (int i = 0; i < n; ++i) {
        if (tab[i] <= 0) {
            continue;
        }
        if (tab[i] % 2 == 1) {
            tab[i] = 3 * tab[i] + 1;
        } else {
            while (tab[i] % 2 == 0) {
                tab[i] /= 2;
            }
        }
    }
    print_array(tab, n);
}

void zmien(int tab[], int n) {
    for (int i = 0; i < n; ++i) {
        if (tab[i] % 2 == 0) {
            tab[i] = -tab[i];
        } else {
            tab[i] *= 2;
        }
    }
    print_array(tab, n);
}

void signum(int tab[], int n) {
    for (int i = 0; i < n; ++i) {
        if (tab[i] > 0) {
            tab[i] = 1;
        } else if (tab[i] < 0) {
            tab[i] = -1;
        }
    }
    print_array(tab, n);
}


void odwroc(int tab[], int n){
    int lewy, prawy;
    printf("Podaj liczbe 'lewy' (0 <= lewy < %d): ", n);
    scanf("%d", &lewy);
    printf("Podaj liczbe 'prawy' (0 <= prawy < %d): ", n);
    scanf("%d", &prawy);


    if (lewy < 0 || lewy >= n || prawy < 0 || prawy >= n) {
        printf("Niepoprawne wartosci 'lewy' lub 'prawy'. Zakres to [0, %d).\n", n);
        return 1;
    }


    while (lewy < prawy) {
        int temp = tab[lewy];
        tab[lewy] = tab[prawy];
        tab[prawy] = temp;
        lewy++;
        prawy--;
    }
    print_array(tab, n);
}

int parzystosc(int tab[], int n){
    int parzyste = 0, nieparzyste = 0;
    for (int i = 0; i < n; ++i) {
        if (tab[i] % 2 == 0) {
            parzyste++;
        } else {
            nieparzyste++;
        }
    }
    printf("Ilosc parzystych elementow: %d\n", parzyste);
    printf("Ilosc nieparzystych elementow: %d\n", nieparzyste);
}

int ileMaksymalnych(int tab[], int n){
    int max = tab[0];
    int imax = 1;
    for (int i = 1; i < n; ++i) {
        if (tab[i] > max) {
            max = tab[i];
            imax = 1;
        } else if (tab[i] == max) {
            imax++;
        }
    }

    printf("Najwiekszy element: %d\n", max);
    printf("Ilosc wystapien najwiekszego elementu: %d\n", imax);
}

int main() {
    int tabela[N];
    int n;
    generuj(tabela, &n);
    parzystosc(tabela, n);
    ileMaksymalnych(tabela, n);
    odwroc(tabela, n);
    collatz(tabela, n);
    zmien(tabela, n);
    signum(tabela, n);

    return 0;
}
