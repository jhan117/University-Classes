//[문제 내용]
//
//문제1에서 만든 코드를 다시 아래의 요구에 맞게 수정해보자.
//
//** 요구 내용**
//1. clock() 함수 대신 Sleep() 함수를 사용하자.
//Sleep(200);  //  clock()은 더 이상 사용하지 않는다. 이 문제에서 clock()은 필요없다.
//2. 커서를 숨기자.[수업 자료 참고]
//3. q나 Q를 입력하면 프로그램을 종료한다.
//4. 별(*)의 최초 위치(x, y)를 무작위로 결정하자. (0~79, 0~24)
//5. 별의 시작 움직임은 x, y 모두 + 1 씩 증가하면서 대각선으로 움직인다.이후에 아래와 같이 방향을 바꾸면서 움직인다.
//6. 공간 내에서 별(*)이 움직이다가 상하좌우의 벽을 만나면 움직이는 방향을 바꾼다.
//왼쪽 벽을 만나면 오른쪽으로 이동(x + 1)
//오른쪽 벽을 만나면 왼쪽으로 이동(x - 1)
//윗쪽 벽을 만나면 아랫쪽으로 이동(y + 1)
//아랫쪽 벽을 만나면 윗쪽으로 이동(y - 1)
//7. 현재 별의 위치를 좌표(0, 0)에 다음과 같은 형식으로 출력한다.
//[7, 20]
//8. 프로그램 수정 후 필요없어진 코드를 삭제하자.

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
    // 커서 숨김
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
    // 흰색
    GotoXY(x, y);
    printf(" ");
}

void Draw(int x, int y)
{
    // 노란색
    GotoXY(x, y);
    printf("*");
}