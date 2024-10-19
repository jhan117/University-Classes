# Week 7

- [Week 7](#week-7)
  - [강의 날짜](#강의-날짜)
  - [강의 내용](#강의-내용)
    - [Ch04. 언어의 핵심! 함수](#ch04-언어의-핵심-함수)
    - [Ch05. 주요 라이브러리 함수들](#ch05-주요-라이브러리-함수들)

## 강의 날짜

- **1차시**: 2024-10-14
- **2차시**: 2024-10-16

## 강의 내용

### Ch04. 언어의 핵심! 함수

- 재귀함수
  - 디자인 사례: 팩토리얼 계산

### Ch05. 주요 라이브러리 함수들

- 라이브러리

  - 표준 vs 비표준

    - 표준 라이브러리 함수: 운영체제에 따라 달라지지 않음
      - `math.h`
        - `double fabs(double x);`: 절대값 반환
        - `double round(double x);`: 반올림 결과 반환
          - C11 표준에 포함
        - `double sin(double x);`: sin 값 반환 (라디안 입력)
        - `double log(double x);`: 자연로그 값 반환
        - `double pow(double x, double x);`: x의 y승 값 반환
      - `stdlib.h`
        - `int rand(void);`: 0 ~ RAND_MAX(32,767)의 난수 생성
          - rand() % (최대값 - 최소값 + 1) + 최소값
        - `void srand (unsigned int seed);`: rand 함수 사용 전 초기화
          - `srand(time(NULL));`: 정수값이 동일하면 난수 순서 동일
            - `time(NULL)`: 프로그램 실행시마다 달라짐(time.h 파일 필요)
        - `int system (const char *string);`: string 커맨드(도스) 명령어 실행
          - 도스 명령어: 도스창(cmd.exe)를 통해 실행 가능
            - dir, cd, copy, cls...
        - 문자열의 숫자 반환
          - `int atoi (const char *nptr);`: 문자열에 있는 정수값 반환
          - `double atof (const char *nptr);`: 문자열에 있는 실수값 반환
          - 문자열이 숫자로 시작하지 않으면 0 반환
          - 맨 앞의 숫자만 반환함
      - `time.h`
        - `clock_t clock(void);`: 실행된 이후 CPU time(clock)값 반환
          - 프로그램 실행시 내부 clock이 0으로 초기화됨
          - 초당 일정 횟수만큼 증가(CLOCKS_PER_SEC, 1000): 두 지점 사이 경과 시간 알아냄
          - clock_t는 long 타입
    - 비표준 라이브러리 함수: Windows 운영체제에서 제공하는 함수들

      - `conio.h`
        - `int _getch(void);`: 키보드 문자 읽음 그렇지만 화면에 나타나지 않음
          - 문자 하나 입력을 위해 대기함
          - 비버퍼형 입력: 키 입력 즉시 해당 문자 읽어들임
          - scanf와 달리 엔터로 화면에 나오지 않기에 printf 함수로 출력해줘야 함
          - 엔터키는 \r로 입력되기 때문에 \n을 적어야 함
          - 문자는 주로 int형으로 처리
          - 방향키 및 ESC키 입력 방법
            - 방향키의 아스키 코드 값이 다른 문자와 중복되기에 아스키 범위 넘는 256 더하면 가능
            - 방향키 입력 시 입력 전에 0 또는 224의 값이 입력됨
              - 다음 입력 문자를 통해 방향키 인식
            - KEY_ESC는 27로 동일함
        - `int _kbhit(void);`: 키 입력 여부, 키 입력되면 0이 아닌 값 반환
          - 어떤 키인지 관계 없음
      - `Windows.h`

        - 도스창의 좌표 체계
          - 기본 크기 (80, 25)
          - 좌표 체계 (x, y)
        - `void *GetStdHandle(unsigned long nStdHandle);`: 지정한 장치에 대한 핸들(포인터) 반환
          - 표준 입출력 핸들 반환
          - GetStdHandle(STD_OUTPUT_HANDLE): 표준 출력 장치 핸들
        - `int SetConsoleCursorPosition(void *hConsoleOutput, COORD dwCursorPosition);`: 실행 도스창의 커서 위치 이동
          - 출력 내용이 현재 커서 위치에 출력됨 (임의의 위치에 데이터 출력하고자 할 때 활용)
          - COORD pos = {5, 7}; // Coord는 구조체
        - `int SetConsoleCursorInfo(void *hConsoleOutput, const CONSOLE_CURSOR_INFO *IpConsoleCursorInfo);`: 커서 크기 설정, 수김 여부 설정

          - 두번째 매개변수로 CONSOLE_CURSOR_INFO 구조체 변수의 주소 전달

            - ```c
              struct CONSOLE_CURSOR_INFO
              {
                DWORD dwSize;
                BOOL bVisible;
              }
              ```

        - `int SetConsoleTextAttribute(void *hConsoleOutput, unsigned short wAttributes);`: 도스창 출력되는 문자 속성 설정, 문자의 foreground, backgournd 설정
          - 기본색: 흰색 문자, 검정색 배경
          - 뒤에 색을 넣어주면 됨
            - FOREGROUND_BLUE, RED, GREEN, BLUE 등
            - FOREGROUND_INTENSITY: 밝은 색
            - 검은색 색 지정 x, 흰색은 세가지 색을 비트 단위 OR(|)로 연결
        - `void Sleep(unsigned log dwMiliseconds);`: dwMiliseconds에 해당하는 밀리초만큼 프로그램의 실행이 중단됨
          - 1000 밀리초 = 1초
          - 다른 작업을 할 수 없음 clock 함수를 이용해 다른 작업 할 수 있음

- 꿀팁: art + prtsc 키 누르면 창이 그대로 복사 됨
