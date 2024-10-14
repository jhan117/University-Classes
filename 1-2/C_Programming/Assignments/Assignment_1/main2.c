#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    float num1;
    double num2;

    printf("숫자 입력: ");
    scanf("%f", &num1);
    printf("%0.30f\n", num1);

    printf("숫자 입력: ");
    scanf("%lf", &num2);
    printf("%0.30f\n", num2);

    return 0;
}