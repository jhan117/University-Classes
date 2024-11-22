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
void Erase(int x, int y);    // (x, y)로 이동하여 공백 문자 출력
void Draw(int x, int y);     // (x, y)로 이동하여 ‘*’ 문자 출력
void draw_border(int width, int height);

int direction = 3;
int dir_diff;
int x_diff = -1;
int y_diff = 0;

#define MAX_SIZE 30

int x_list[MAX_SIZE] = { 15, 16, 17, 18, 19 };
int y_list[MAX_SIZE] = { 10, 10, 10, 10, 10 };
int cur_size = 5;
int head = 0;

void quit_game(const char* message);

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
        {   // 0.5초 경과
            Erase(x, y);

            int new_head = (head - 1 + MAX_SIZE) % MAX_SIZE;
            x_list[new_head] = x_list[head] + x_diff;
            y_list[new_head] = y_list[head] + y_diff;
            head = new_head;

            Draw(x, y);

            if (x == 0 || x == 79 || y == 0 || y == 24)
            {
                quit_game("구에에에게");
                break;
            }

            initial_clock = current_clock;  // 기준 시각 재설정
        }
        if (_kbhit())
        {
            int key = GetKey();

            /*if (key == KEY_LEFT)
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
            }*/
            switch (key)
            {
            case KEY_RIGHT:
                direction = (direction + 1 + 4) % 4;
                break;
            case KEY_LEFT:
                direction = (direction - 1 + 4) % 4;
                break;
            }

            switch (direction)
            {
            case 0: x_diff = 0; y_diff = -1; break;
            case 1: x_diff = 1; y_diff = 0; break;
            case 2: x_diff = 0; y_diff = 1; break;
            case 3: x_diff = -1; y_diff = 0; break;
            }
        }
    }
}
int GetKey(void)
{
    int ch = _getch();

    if (ch == 0 || ch == 224)
        // 방향키의 경우 0 또는 224의 값이 먼저 입력됨
        ch = 256 + _getch();
    // 그 다음에 해당 방향키에 따라 72(Up),
    // 80(Down), 75(Left), 77(Right) 값이 입력됨
    return ch;
}

double GetElapsedTime(clock_t initial_clock, clock_t current_clock)
{
    return (double)(current_clock - initial_clock) / CLOCKS_PER_SEC;
}

void GotoXY(int x, int y)
{
    // COORD 구조체 변수를 통해 이동할 위치 설정
    COORD pos = { x, y };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}

void Erase(int x, int y)
{
    for (int i = 0; i < cur_size; i++)
    {
        int idx = (head + i) % MAX_SIZE;
        GotoXY(x_list[idx], y_list[idx]);
        printf("%c", ' ');
    }
}

void Draw(int x, int y)
{
    for (int i = 0; i < cur_size; i++)
    {
        int idx = (head + i) % MAX_SIZE;
        GotoXY(x_list[idx], y_list[idx]);
        printf("%c", i == 0 ? 'Q' : 'O');
    }
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
    for (int i = 0; i < height; i++)
    {
        GotoXY(0, i);
        printf("*");
        GotoXY(width - 1, i);
        printf("*");
    }
}

void quit_game(const char* message)
{
    GotoXY(35, 10);
    printf(message);
    //printf("[%s]", message);
    GotoXY(0, 25);
    exit(0);
}