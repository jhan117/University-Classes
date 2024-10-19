// 예제코드 : 24p의 종합 예제(1)

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
        clock_t current_clock = clock();

        // 0.5초 후
        if (GetElapsedTime(initial_clock, current_clock) > 0.5)
        {
            Erase(x, y);
            y++;
            Draw(x, y);

            if (y == 24)
                break;

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