#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>
#include <Windows.h>

#define KEY_LEFT  (256 + 75)
#define KEY_RIGHT (256 + 77)
#define KEY_UP    (256 + 72)
#define KEY_DOWN  (256 + 80)

#define WIDTH 80
#define HEIGHT 25

#define DIR_UP 0
#define DIR_DOWN 1
#define DIR_LEFT 2
#define DIR_RIGHT 3

#define ANSI_COLOR_RED "\x1b[31m"
#define ANSI_COLOR_RESET   "\x1b[0m"

int direction = DIR_RIGHT;
int foodX, foodY;
int score = 0;
int collision = 0;

void HideCursor();
void GotoXY(int x, int y);
void DrawBorder();
void Draw(int x, int y, char symbol, int isRed);
void Erase(int x, int y);
int GetKey(void);
double GetElapsedTime(clock_t initial_clock, clock_t current_clock);
void MoveCharacter(int* x, int* y);
void GenerateFood(int* foodX, int* foodY);
void DrawFood(int foodX, int foodY);
void DisplayScore();
int IsFoodOnSnake(int foodX, int foodY, int* snakeX, int* snakeY, int snakeLen);
int IsSnakeCollidedWithItself(int headX, int headY, int* snakeX, int* snakeY, int snakeLen);
void UpdateSnakePosition(int* snakeX, int* snakeY, int snakeLen);

int main(void)
{
    srand(time(NULL));
    HideCursor();
    DrawBorder();

    int snakeX[100], snakeY[100];
    int snakeLen = 3;
    snakeX[0] = 10;
    snakeY[0] = 11;
    Draw(snakeX[0], snakeY[0], 'Q', 0);

    GenerateFood(&foodX, &foodY);
    DrawFood(foodX, foodY);

    clock_t initial_clock = clock();

    while (1)
    {
        Sleep(125);
        clock_t current_clock = clock();

        if (GetElapsedTime(initial_clock, current_clock) > 0.01)
        {
            Erase(snakeX[snakeLen - 1], snakeY[snakeLen - 1]);
            UpdateSnakePosition(snakeX, snakeY, snakeLen);
            MoveCharacter(&snakeX[0], &snakeY[0]);

            int isSnakeCollied = IsSnakeCollidedWithItself(snakeX[0], snakeY[0], snakeX, snakeY, snakeLen);
            if (isSnakeCollied || snakeX[0] == 0 || snakeX[0] == WIDTH - 1 || snakeY[0] == 0 || snakeY[0] == HEIGHT - 1)
                collision = 1;

            // 뱀 그리기
            Draw(snakeX[0], snakeY[0], 'Q', collision);
            for (int i = 1; i < snakeLen; i++)
            {
                Draw(snakeX[i], snakeY[i], 'O', 0);
            }

            if (snakeX[0] == foodX && snakeY[0] == foodY)
            {
                score++;
                snakeLen++;
                while (IsFoodOnSnake(foodX, foodY, snakeX, snakeY, snakeLen))
                {
                    GenerateFood(&foodX, &foodY);
                }
                DrawFood(foodX, foodY);
            }

            DisplayScore();
            initial_clock = current_clock;
        }

        if (collision)
        {
            GotoXY(WIDTH / 2 - 4, HEIGHT / 2);
            printf("GAME OVER");
            GotoXY(WIDTH / 2 - 4, HEIGHT / 2 + 1);
            printf("Score: %d", score);
            GotoXY(0, HEIGHT);
            break;
        }

        if (_kbhit())
        {
            int key = GetKey();
            switch (key)
            {
            case KEY_RIGHT:
                if (direction != DIR_LEFT)
                    direction = DIR_RIGHT;
                break;
            case KEY_LEFT:
                if (direction != DIR_RIGHT)
                    direction = DIR_LEFT;
                break;
            case KEY_UP:
                if (direction != DIR_DOWN)
                    direction = DIR_UP;
                break;
            case KEY_DOWN:
                if (direction != DIR_UP)
                    direction = DIR_DOWN;
                break;
            }
        }
    }
    return 0;
}

void HideCursor() {
    CONSOLE_CURSOR_INFO ci = { 100, FALSE };
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &ci);
}

void GotoXY(int x, int y) {
    COORD pos = { x, y };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}

void DrawBorder() {
    for (int i = 0; i < WIDTH; i++)
    {
        GotoXY(i, 0);
        printf(i == 0 ? "┌" : (i == WIDTH - 1 ? "┐" : "─"));
        GotoXY(i, HEIGHT - 1);
        printf(i == 0 ? "└" : (i == WIDTH - 1 ? "┘" : "─"));
    }
    for (int i = 1; i < HEIGHT - 1; i++)
    {
        GotoXY(0, i);
        printf("│");
        GotoXY(WIDTH - 1, i);
        printf("│");
    }
}

void Draw(int x, int y, char symbol, int isRed)
{
    GotoXY(x, y);
    if (isRed)
        printf(ANSI_COLOR_RED "%c" ANSI_COLOR_RESET, symbol);
    else
        printf("%c", symbol);
}

void Erase(int x, int y)
{
    GotoXY(x, y);
    printf(" ");
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

void MoveCharacter(int* x, int* y)
{
    switch (direction)
    {
    case DIR_UP:
        (*y)--;
        break;
    case DIR_DOWN:
        (*y)++;
        break;
    case DIR_LEFT:
        (*x)--;
        break;
    case DIR_RIGHT:
        (*x)++;
        break;
    }
}

void GenerateFood(int* foodX, int* foodY)
{
    // rand() % (max - min + 1) + min
    int x_max = WIDTH - 3;
    int x_min = 3;
    int y_max = HEIGHT - 3;
    int y_min = 3;

    *foodX = rand() % (x_max - x_min + 1) + x_min;
    *foodY = rand() % (y_max - y_min + 1) + y_min;
}

void DrawFood(int foodX, int foodY)
{
    GotoXY(foodX, foodY);
    printf(ANSI_COLOR_RED "a" ANSI_COLOR_RESET);
}

void DisplayScore()
{
    GotoXY(WIDTH - 15, HEIGHT + 1);
    printf("Score: %d", score);
}

int IsFoodOnSnake(int foodX, int foodY, int* snakeX, int* snakeY, int snakeLen)
{
    for (int i = 0; i < snakeLen; i++)
    {
        if (foodX == snakeX[i] && foodY == snakeY[i])
            return 1;
    }
    return 0;
}

int IsSnakeCollidedWithItself(int headX, int headY, int* snakeX, int* snakeY, int snakeLen)
{
    for (int i = 1; i < snakeLen; i++)
    {
        if (headX == snakeX[i] && headY == snakeY[i])
            return 1;
    }
    return 0;
}

void UpdateSnakePosition(int* snakeX, int* snakeY, int snakeLen)
{
    for (int i = snakeLen - 1; i > 0; i--)
    {
        snakeX[i] = snakeX[i - 1];
        snakeY[i] = snakeY[i - 1];
    }
}