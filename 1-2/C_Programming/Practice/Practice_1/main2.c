//[문제2] do~while로 작성된 아래의 예제 코드를 while문 형식으로 수정하라.
//int main(void)
//{
//    int total = 0, num = 0;
//    
//    do
//    {
//        printf("정수 입력(0 to quit): ");
//        scanf("%d", &num);
//        total += num;
//    } while (num != 0);
//
//    printf("합계: %d \n", total);
//}


#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int total = 0, num = 0;

    // do 역할을 한다.
    // 그러나 중복 코드로 되어서 좋은 코드는 아님.
    printf("정수 입력(0 to quit): ");
    scanf("%d", &num);
    total += num;

    while (num != 0) {
        printf("정수 입력(0 to quit): ");
        scanf("%d", &num);
        total += num;
    }

    printf("합계: %d \n", total);
}