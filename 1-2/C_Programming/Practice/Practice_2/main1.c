//[문제 내용]
//
//수업자료 : Ch05_주요 라이브러리 함수들.pdf
//예제코드 : 24p의 종합 예제(1)
//
//1. 별(*)이 마지막 줄에 도착하면 다시 첫줄로 이동하도록 수정한다.
//2. 프로그램을 실행하고 CPU 사용률을 확인한다.[윈도우 작업 관리자]
//3. clock() 함수 대신 Sleep() 함수를 사용하도록 수정한다.
//Sleep(500); 정도..
//4. 프로그램을 실행하고 CPU 사용률을 확인한다.[윈도우 작업 관리자]
//5. 프로그램을 수정하기 전과 후에서 CPU 사용률이 어떠한가 ?
//6. 좌우 방향키를 사용해서 별의 위치를 바꿔보자.프로그램 수정 전과 후에서 차이가 있는가 ?
//7. 만약 6.에서 어떤 차이가 느껴졌다면 이 차이를 줄이기 위해서 어떻게 수정할까 ?
//clock()과 Sleep()을 함께 사용하여 해결!

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

        // 0.5초 후
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