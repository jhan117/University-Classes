//[����1] �Ʒ��� ���� �°� �������� ����ϴ� ���α׷��� �ۼ��϶�.
//> 4���� ������ �Է¹޴´�.������ a, b, c, d��� ����.
//> �������� a�ܿ��� b�ܱ��� ����Ѵ�.
//> �� ���� x c ���� x d ���� ����Ѵ�.

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int a, b, c, d;
    printf("4���� ���� �Է� : ");
    scanf("%d%d%d%d", &a, &b, &c, &d);
    int i, j;
    for (i = a; i <= b; i++)
    {
        for (j = c; j <= d; j++)
        {
            printf("%d x %d = %d\n", i, j, i * j);
        }
        printf("\n");
    }
    return 0;
}