#include <stdio.h>

int main()
{
	char num1 = 0x7f;
	int num2 = 0x7fffffff;

	printf("char�� ���� �ʱ갪: %X %d\n", num1, num1);
	printf("�����÷ο�: %X %d\n", ++num1, num1);
	printf("����÷ο�: %X %d\n", --num1, num1);

	printf("int�� ���� �ʱ갪: %X %d\n", num2, num2);
	printf("�����÷ο�: %X %d\n", ++num2, num2);
	printf("����÷ο�: %X %d\n", --num2, num2);

	return 0;
}
