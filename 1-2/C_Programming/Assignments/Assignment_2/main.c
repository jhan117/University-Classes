#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void print_gugu(int a, int b, int c, int d);
void print_dan(int i, int c, int d);
void print_line(int i, int j);

int main(void)
{
    int a, b, c, d;
    printf("a, b, c, d ют╥б: ");
    scanf("%d%d%d%d", &a, &b, &c, &d);

    print_gugu(a, b, c, d);

    return 0;
}

void print_gugu(int a, int b, int c, int d)
{
    for (int i = a; i <= b; i++)
    {
        print_dan(i, c, d);
    }
}

void print_dan(int i, int c, int d)
{
    for (int j = c; j <= d; j++)
    {
        print_line(i, j);
    }

    printf("\n");
}

void print_line(int i, int j)
{
    printf("%d X %d = %d\n", i, j, i * j);
}
