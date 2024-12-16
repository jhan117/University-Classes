#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>
#include <Windows.h>

#define KEY_LEFT  (256 + 75)
#define KEY_RIGHT (256 + 77)
#define KEY_UP    (256 + 72)
#define KEY_DOWN  (256 + 80)
#define MAX_SIZE 30

int direction = 3;
int x_diff = -1;
int y_diff = 0;
double speed = 0.5;
int isMaking = 0;

COORD snake[MAX_SIZE] = { {15, 10}, {16, 10}, {17, 10}, {18, 10}, {19, 10} };
int cur_size = 5;
int head = 0;
int left = 0, right = 79, top = 0, bottom = 24;

int GetKey(void);
double GetElapsedTime(clock_t initial_clock, clock_t current_clock);
void SetPosition(int x, int y);
void ClearScreen();
void DrawSnake();
void DrawBorder(int width, int height);
void ExitGame(const char* message);
int CheckCollisionWithBorder(int left, int right, int top, int bottom);
void UpdateDirection(int direction, int* x_diff, int* y_diff);
void AddAppleEffect();
void AddSpeedEffect();
double ChangeSpeed(double current, double diff);
void ChangeSnakeLength(int* length, char apple);

int main(void)
{
    srand(time(NULL));

    CONSOLE_CURSOR_INFO ci = { 100, FALSE };
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &ci);

    DrawBorder(80, 25);
    DrawSnake();

    clock_t initial_clock = clock();

    while (1)
    {
        Sleep(1);
        clock_t current_clock = clock();

        if (GetElapsedTime(initial_clock, current_clock) > speed)
        {
            ClearScreen();

            int new_head = (head - 1 + MAX_SIZE) % MAX_SIZE;
            snake[new_head].X = snake[head].X + x_diff;
            snake[new_head].Y = snake[head].Y + y_diff;
            head = new_head;

            DrawSnake();

            if (CheckCollisionWithBorder(left, right, top, bottom))
                ExitGame("²Ù¿¡¿¡¿¢");

            initial_clock = current_clock;
        }

        if (_kbhit())
        {
            int key = GetKey();

            switch (key)
            {
            case KEY_RIGHT:
                direction = (direction + 1 + 4) % 4;
                break;

            case KEY_LEFT:
                direction = (direction - 1 + 4) % 4;
                break;

            case KEY_UP:
                speed = ChangeSpeed(speed, -0.1);
                AddSpeedEffect();
                break;

            case KEY_DOWN:
                speed = ChangeSpeed(speed, 0.1);
                AddSpeedEffect();
                break;

            case 'a':
            case 'A':
                ChangeSnakeLength(&cur_size, key);
                AddAppleEffect();
                break;

            case 'q':
            case 'Q':
                ExitGame("¾È³ç!");
                break;
            }

            UpdateDirection(direction, &x_diff, &y_diff);
        }
    }
}

void ChangeSnakeLength(int* length, char apple)
{
    int diff = apple == 'A' ? 1 : -1;

    if (diff == -1)
        ClearScreen();

    int l = *length;
    l += diff;
    if (l < 1)
        l = 1;
    if (l > MAX_SIZE)
        l = MAX_SIZE;
    *length = l;

    if (diff == -1)
        DrawSnake();
}
double ChangeSpeed(double current, double diff)
{
    current += diff;
    if (current < 0.1)
        return 0.1;
    if (current > 1.0)
        return 1.0;

    return current;
}
void AddSpeedEffect()
{
    SetPosition(0, 26);
    int adjustSpeed = (1.0 - speed) * 10.0;
    printf("¼Óµµ: %d\n", adjustSpeed);
}
void AddAppleEffect()
{
    SetPosition(0, 25);
    printf("»ç°ú ³È³È! ±æÀÌ: %d\n", cur_size);
}
void UpdateDirection(int direction, int* x_diff, int* y_diff)
{
    switch (direction)
    {
    case 0: *x_diff = 0; *y_diff = -1; break;
    case 1: *x_diff = 1; *y_diff = 0; break;
    case 2: *x_diff = 0; *y_diff = 1; break;
    case 3: *x_diff = -1; *y_diff = 0; break;
    }
}
int GetKey(void)
{
    int ch = _getch();
    if (ch == 0 || ch == 224)
        ch = 256 + _getch();
    return ch;
}
double GetElapsedTime(clock_t initial_clock, clock_t current_clock)
{
    return (double)(current_clock - initial_clock) / CLOCKS_PER_SEC;
}
void SetPosition(int x, int y)
{
    COORD pos = { x, y };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}
void ClearScreen()
{
    for (int i = 0; i < cur_size; i++)
    {
        int idx = (head + i) % MAX_SIZE;
        SetPosition(snake[idx].X, snake[idx].Y);
        printf(" ");
    }
}
void DrawSnake()
{
    for (int i = 0; i < cur_size; i++)
    {
        int idx = (head + i) % MAX_SIZE;
        SetPosition(snake[idx].X, snake[idx].Y);
        printf("%c", i == 0 ? 'Q' : 'O');
    }
}
void DrawBorder(int width, int height)
{
    for (int i = 0; i < width; i++)
    {
        SetPosition(i, 0);
        printf("*");
        SetPosition(i, height - 1);
        printf("*");
    }

    for (int i = 0; i < height; i++)
    {
        SetPosition(0, i);
        printf("*");
        SetPosition(width - 1, i);
        printf("*");
    }
}
void ExitGame(const char* message)
{
    SetPosition(35, 10);
    printf("%s", message);
    SetPosition(0, 25);
    exit(0);
}
int CheckCollisionWithBorder(int left, int right, int top, int bottom)
{
    if (snake[head].X == left || snake[head].X == right ||
        snake[head].Y == top || snake[head].Y == bottom)
        return 1;
    return 0;
}