#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>
#include <Windows.h>

#define KEY_LEFT  (256 + 75)
#define KEY_RIGHT (256 + 77)
#define KEY_UP    (256 + 72)
#define KEY_DOWN  (256 + 80)

int GetKey(void);
double GetElapsedTime(clock_t initial_clock, clock_t current_clock);
void GotoXY(int x, int y);
void Erase(int x, int y);    // (x, y)�� �̵��Ͽ� ���� ���� ���
void Draw(int x, int y);     // (x, y)�� �̵��Ͽ� ��*�� ���� ���
void draw_border(int width, int height);

int direction = 1;
int x_diff = 1;
int y_diff = 0;

int main(void)
{
    srand(time(NULL));

    CONSOLE_CURSOR_INFO ci = { 100, FALSE };
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &ci);
    draw_border(80, 25);

    int x = 70;
    int y = 11;
    Draw(x, y);

    clock_t initial_clock = clock();

    while (1)
    {
        Sleep(1);
        clock_t current_clock = clock();

        if (GetElapsedTime(initial_clock, current_clock) > 0.5)
        {   // 0.5�� ���
            Erase(x, y);

            x += x_diff;
            y += y_diff;

            Draw(x, y);

            if (x == 0 || x == 79 || y == 0 || y == 24)
            {
                GotoXY(39, 11);
                printf("�ٿ���");
                GotoXY(0, 25);
                break;
            }

            initial_clock = current_clock;  // ���� �ð� �缳��
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
        // ����Ű�� ��� 0 �Ǵ� 224�� ���� ���� �Էµ�
        ch = 256 + _getch();
    // �� ������ �ش� ����Ű�� ���� 72(Up),
    // 80(Down), 75(Left), 77(Right) ���� �Էµ�
    return ch;
}

double GetElapsedTime(clock_t initial_clock, clock_t current_clock)
{
    return (double)(current_clock - initial_clock) / CLOCKS_PER_SEC;
}

void GotoXY(int x, int y)
{
    // COORD ����ü ������ ���� �̵��� ��ġ ����
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
    printf("Q");
}

void draw_border(int width, int height)
{
    for (int i = 0; i < width; i++)
    {
        GotoXY(i, 0);
        printf("*");
        GotoXY(i, height - 1);
        printf("*");
    }

    for (int j = 0; j < height; j++)
    {
        GotoXY(0, j);
        printf("*");
        GotoXY(width - 1, j);
        printf("*");
    }
}