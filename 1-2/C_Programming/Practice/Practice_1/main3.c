//[����3]  while�� �ۼ��� �Ʒ��� ���� �ڵ带 do~while�� �������� �����϶�.
//
//���� �ڷῡ ���� ���� �ڵ�
//if���� �Բ� ����ؾ� ��ȯ�� ������
//int main(void)
//{
//    int dan = 0, num = 1;
//
//    printf("�� ��? ");
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

    printf("�� ��? ");
    scanf("%d", &dan);

    if (num < 10) {
        do
        {
            printf("%d x %d = %d\n", dan, num, dan * num);
            num++;
        } while (num < 10);
    }
}