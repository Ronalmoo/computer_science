#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define SIZE 1000

int a[SIZE];

int swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int n, min, index;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    for (int i = 0; i < n - 1; i++) {
        int j = i;
        while (j >= 0 && a[j] > a[j + 1]) {
            swap(&a[j], &a[j + 1]);
            j--;
        }
    }
    for (int i = 0; i < n; i++) {
        printf("%d", a[i]);
    }
    system("pause");
    return 0;
}
