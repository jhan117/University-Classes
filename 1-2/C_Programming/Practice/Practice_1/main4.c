//[����4] �Ǽ��� ������ ���е��� Ȯ���غ���.
//
//�Ǽ���(double) ������ 0.1�� �������� �� �� ����� ��Ȯ���� �ʴٴ� ���� ������ ���� �ڷῡ�� Ȯ���ߴ�.
//
//�ݺ����� ����ؼ� �Ǽ��� ������ 0.1�� �����ϸ鼭 ��� ������ �������� �� ������ �߻��ϱ� �����ϴ��� Ȯ���غ���.
//
//�Ʒ��� �̿ϼ� ���� �ڵ带 �ϼ��ؼ� Ȯ������.

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