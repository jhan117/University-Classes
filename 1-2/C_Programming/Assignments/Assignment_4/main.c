#include <stdio.h>
#include <stdlib.h>

int* copy_int_array(int* src, int size);

int main()
{
    int a[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    int size = sizeof(a) / sizeof(int);
    for (int i = 0; i < size; i++)
        printf("%d ", a[i]);
    printf("\n");

    int* b = copy_int_array(a, size);
    if (b == NULL)
        return 1;
    for (int i = 0; i < size; i++)
        printf("%d ", b[i]);

    free(b);
    return 0;
}

int* copy_int_array(int* src, int size)
{
    if (size < 1 || src == NULL)
        return NULL;

    int* arr = malloc(sizeof(int) * size);

    if (arr == NULL)
        return NULL;

    for (int i = 0; i < size; i++)
    {
        arr[i] = src[i];
    }

    return arr;
}