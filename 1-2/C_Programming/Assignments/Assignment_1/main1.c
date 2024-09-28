#include <stdio.h>

int main()
{
	char num1 = 0x7f;
	int num2 = 0x7fffffff;

	printf("char형 변수 초깃값: %X %d\n", num1, num1);
	printf("오버플로우: %X %d\n", ++num1, num1);
	printf("언더플로우: %X %d\n", --num1, num1);

	printf("int형 변수 초깃값: %X %d\n", num2, num2);
	printf("오버플로우: %X %d\n", ++num2, num2);
	printf("언더플로우: %X %d\n", --num2, num2);

	return 0;
}
