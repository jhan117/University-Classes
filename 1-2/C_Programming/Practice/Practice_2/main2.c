//[���� ����]
//
//����1���� ���� �ڵ带 �ٽ� �Ʒ��� �䱸�� �°� �����غ���.
//
//** �䱸 ����**
//1. clock() �Լ� ��� Sleep() �Լ��� �������.
//Sleep(200);  //  clock()�� �� �̻� ������� �ʴ´�. �� �������� clock()�� �ʿ����.
//2. Ŀ���� ������.[���� �ڷ� ����]
//3. q�� Q�� �Է��ϸ� ���α׷��� �����Ѵ�.
//4. ��(*)�� ���� ��ġ(x, y)�� �������� ��������. (0~79, 0~24)
//5. ���� ���� �������� x, y ��� + 1 �� �����ϸ鼭 �밢������ �����δ�.���Ŀ� �Ʒ��� ���� ������ �ٲٸ鼭 �����δ�.
//6. ���� ������ ��(*)�� �����̴ٰ� �����¿��� ���� ������ �����̴� ������ �ٲ۴�.
//���� ���� ������ ���������� �̵�(x + 1)
//������ ���� ������ �������� �̵�(x - 1)
//���� ���� ������ �Ʒ������� �̵�(y + 1)
//�Ʒ��� ���� ������ �������� �̵�(y - 1)
//7. ���� ���� ��ġ�� ��ǥ(0, 0)�� ������ ���� �������� ����Ѵ�.
//[7, 20]
//8. ���α׷� ���� �� �ʿ������ �ڵ带 ��������.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <Windows.h>
#include <conio.h>

#define KEY_LEFT (256 + 75)
#define KEY_RIGHT (256 + 77)

int GetKey(void);
void GotoXY(int x, int y);
void Erase(int x, int y);
void Draw(int x, int y);

int main(void)
{
    // Ŀ�� ����
    CONSOLE_CURSOR_INFO ci = { 0, FALSE };
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &ci);

    srand(time(NULL));

    int x_diff = 1;
    int y_diff = 1;

    int x = rand() % 80;
    int y = rand() % 25;
    Draw(x, y);

    clock_t initial_clock = clock();

    while (1)
    {
        Sleep(20);

        {
            //Erase(x, y);

            if (x == 0) x_diff = 1;
            if (x == 79) x_diff = -1;
            if (y == 0) y_diff = 1;
            if (y == 24) y_diff = -1;

            x += x_diff;
            y += y_diff;

            GotoXY(0, 0);
            printf("[%2d, %2d]", x, y);

            Draw(x, y);
        }

        if (_kbhit())
        {
            int key = GetKey();

            if (key == 'q' || key == 'Q')
                break;
        }
    }
}

int GetKey(void)
{
    int ch = _getch();

    if (ch == 0 || ch == 224)
        ch = 256 + _getch();
    return ch;
}

void GotoXY(int x, int y)
{
    COORD pos = { x, y };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}

void Erase(int x, int y)
{
    // ���
    GotoXY(x, y);
    printf(" ");
}

void Draw(int x, int y)
{
    // �����
    GotoXY(x, y);
    printf("*");
}