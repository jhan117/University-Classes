//[����2] do~while�� �ۼ��� �Ʒ��� ���� �ڵ带 while�� �������� �����϶�.
//int main(void)
//{
//    int total = 0, num = 0;
//    
//    do
//    {
//        printf("���� �Է�(0 to quit): ");
//        scanf("%d", &num);
//        total += num;
//    } while (num != 0);
//
//    printf("�հ�: %d \n", total);
//}


#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int total = 0, num = 0;

    // do ������ �Ѵ�.
    // �׷��� �ߺ� �ڵ�� �Ǿ ���� �ڵ�� �ƴ�.
    printf("���� �Է�(0 to quit): ");
    scanf("%d", &num);
    total += num;

    while (num != 0) {
        printf("���� �Է�(0 to quit): ");
        scanf("%d", &num);
        total += num;
    }

    printf("�հ�: %d \n", total);
}