//[���� ����]
//
//�����ڷ� : Ch05_�ֿ� ���̺귯�� �Լ���.pdf
//�����ڵ� : 24p�� ���� ����(1)
//
//1. ��(*)�� ������ �ٿ� �����ϸ� �ٽ� ù�ٷ� �̵��ϵ��� �����Ѵ�.
//2. ���α׷��� �����ϰ� CPU ������ Ȯ���Ѵ�.[������ �۾� ������]
//3. clock() �Լ� ��� Sleep() �Լ��� ����ϵ��� �����Ѵ�.
//Sleep(500); ����..
//4. ���α׷��� �����ϰ� CPU ������ Ȯ���Ѵ�.[������ �۾� ������]
//5. ���α׷��� �����ϱ� ���� �Ŀ��� CPU ������ ��Ѱ� ?
//6. �¿� ����Ű�� ����ؼ� ���� ��ġ�� �ٲ㺸��.���α׷� ���� ���� �Ŀ��� ���̰� �ִ°� ?
//7. ���� 6.���� � ���̰� �������ٸ� �� ���̸� ���̱� ���ؼ� ��� �����ұ� ?
//clock()�� Sleep()�� �Բ� ����Ͽ� �ذ�!

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <Windows.h>
#include <conio.h>

#define KEY_LEFT (256 + 75)
#define KEY_RIGHT (256 + 77)

int GetKey(void);
double GetElapsedTime(clock_t initial_clock, clock_t current_clock);
void GotoXY(int x, int y);
void Erase(int x, int y);
void Draw(int x, int y);

int main(void)
{
    srand(time(NULL));

    int x = rand() % 80;
    int y = 0;
    Draw(x, y);

    clock_t initial_clock = clock();

    while (1)
    {
        Sleep(1);
        clock_t current_clock = clock();

        // 0.5�� ��
        if (GetElapsedTime(initial_clock, current_clock) > 0.1)
        {
            Erase(x, y);
            //y++;
            //if (y == 25)
            //    y = 0;
            y = (y + 1) % 25;
            Draw(x, y);

            //if (y == 24)
            //   break;

            initial_clock = current_clock;
        }

        if (_kbhit())
        {
            int key = GetKey();

            if (key == KEY_LEFT)
            {
                Erase(x, y);
                x--;
                Draw(x, y);
            }
            else if (key == KEY_RIGHT)
            {
                Erase(x, y);
                x++;
                Draw(x, y);
            }
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

// ms -> s
double GetElapsedTime(clock_t initial_clock, clock_t current_clock)
{
    return (double)(current_clock - initial_clock) / CLOCKS_PER_SEC;
}

void GotoXY(int x, int y)
{
    COORD pos = { x, y };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}

void Erase(int x, int y)
{
    GotoXY(x, y);
    printf(" ");
}

void Draw(int x, int y)
{
    GotoXY(x, y);
    printf("*");
}