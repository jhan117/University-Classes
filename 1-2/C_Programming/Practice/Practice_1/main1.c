//[문제1] 아래의 설명에 맞게 구구단을 출력하는 프로그램을 작성하라.
//> 4개의 정수를 입력받는다.각각을 a, b, c, d라고 하자.
//> 구구단을 a단에서 b단까지 출력한다.
//> 각 단은 x c 에서 x d 까지 출력한다.

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int a, b, c, d;
    printf("4개의 정수 입력 : ");
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