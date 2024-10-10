//[문제3]  while로 작성된 아래의 예제 코드를 do~while문 형식으로 수정하라.
//
//수업 자료에 나온 예제 코드
//if문을 함께 사용해야 변환이 가능함
//int main(void)
//{
//    int dan = 0, num = 1;
//
//    printf("몇 단? ");
//    scanf("%d", &dan);
//
//    while (num < 10) {
//        printf("%d x %d = %d\n", dan, num, dan * num);
//        num++;
//    }
//}

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int dan = 0, num = 1;

    printf("몇 단? ");
    scanf("%d", &dan);

    if (num < 10) {
        do
        {
            printf("%d x %d = %d\n", dan, num, dan * num);
            num++;
        } while (num < 10);
    }
}