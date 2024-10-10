//[문제4] 실수형 변수의 정밀도를 확인해보자.
//
//실수형(double) 변수에 0.1을 누적했을 때 그 결과가 정확하지 않다는 것을 이전의 수업 자료에서 확인했다.
//
//반복문을 사용해서 실수형 변수에 0.1을 누적하면서 어느 정도로 누적했을 때 오차가 발생하기 시작하는지 확인해보자.
//
//아래의 미완성 예제 코드를 완성해서 확인하자.

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    double dsum = 0;
    int isum = 0;

    int i;
    for (i = 0; i < 100; i++)
    {
        dsum += 0.1;
        isum += 1;
        printf("%f %d\n", dsum, isum);
        if (dsum != (double)isum / 10)
        {
            break;
        }
    }
    printf("%0.30f %d\n", dsum, isum);
    return 0;
}