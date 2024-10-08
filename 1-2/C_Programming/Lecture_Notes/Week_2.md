# Week 1

## 강의 날짜

- **1차시**: 2024-09-09
- **2차시**: 2024-09-11

## 1차시 강의 내용

### 3. 연산을 위한 연산자와 값의 저장을 위한 변수

#### 3.1 덧셈 연산자

덧셈 연산자는 두 개의 값을 더하는 데 사용됩니다. 예를 들어, `a + b`는 `a`와 `b`의 합을 반환합니다.

#### 3.2 변수를 이용한 데이터의 저장

변수는 메모리에서 데이터를 저장하는 공간을 의미합니다. 변수에 값을 저장하고 그 값을 사용할 수 있습니다. 변수를 선언할 때는 자료형을 지정해야 하며, 이는 해당 변수에 저장될 데이터의 종류를 결정합니다.

```c
int number = 5; // 정수형 변수 number에 값 5를 저장
```

#### 3.3 변수의 다양한 선언 및 초기화 방법

변수는 선언 후 값을 나중에 대입할 수도 있고, 선언과 동시에 값을 초기화할 수도 있습니다.

- **선언 후 초기화**:
  ```c
  int a;
  a = 10;
  ```
- **선언과 동시에 초기화**:
  ```c
  int b = 20;
  ```

#### 3.4 변수 선언 시 주의 사항

- **자료형 일치**: 변수에 저장되는 값은 선언된 자료형과 일치해야 합니다.
- **중복 선언 금지**: 동일한 이름의 변수를 두 번 선언하면 컴파일 오류가 발생합니다.
- **변수 범위**: 변수는 선언된 블록(중괄호 `{}`) 내에서만 유효합니다.

#### 3.5 변수의 자료형

변수의 자료형은 변수가 저장할 수 있는 데이터의 종류를 결정합니다. C 언어에서 기본적으로 제공하는 자료형은 다음과 같습니다:

- **int**: 정수
- **float**: 실수
- **double**: 더 큰 범위의 실수
- **char**: 문자

```c
int age = 25;
float weight = 65.5;
char initial = 'A';
```

### 4. C 언어의 다양한 연산자 소개

#### 4.1 대입 연산자와 산술 연산자

- **대입 연산자**(`=`): 변수에 값을 대입하는 데 사용됩니다.
  ```c
  int x = 10;
  ```
- **산술 연산자**: 덧셈(`+`), 뺄셈(`-`), 곱셈(`*`), 나눗셈(`/`), 나머지(`%`) 연산이 가능합니다.
  ```c
  int sum = x + 5;
  int remainder = x % 3;
  ```

#### 4.2 복합 대입 연산자

복합 대입 연산자는 대입과 산술 연산을 함께 수행하는 연산자입니다.

- `+=`, `-=`, `*=`, `/=`, `%=`
  ```c
  x += 5; // x = x + 5와 동일
  ```

#### 4.3 부호 연산자로서의 +, -

`+`와 `-`는 숫자의 부호를 변경하는 데 사용됩니다.

- `+`는 양수를 나타내고, `-`는 음수를 나타냅니다.
  ```c
  int positive = +10;
  int negative = -10;
  ```

#### 4.4 증가 연산자, 감소 연산자

- **증가 연산자**(`++`): 변수의 값을 1 증가시킵니다.
- **감소 연산자**(`--`): 변수의 값을 1 감소시킵니다.
  ```c
  int num = 10;
  num++; // num은 이제 11
  num--; // num은 다시 10
  ```

#### 4.5 관계 연산자

관계 연산자는 두 값 간의 관계를 비교하여 참(`1`) 또는 거짓(`0`)을 반환합니다.

- `==`, `!=`, `>`, `<`, `>=`, `<=`
  ```c
  int result = (a == b); // a와 b가 같으면 1, 그렇지 않으면 0
  ```

#### 4.6 논리 연산자

논리 연산자는 논리적인 조건을 결합하거나 부정할 때 사용됩니다.

- **AND 연산자**(`&&`): 두 조건이 모두 참이면 참
- **OR 연산자**(`||`): 하나라도 참이면 참
- **NOT 연산자**(`!`): 조건을 부정
  ```c
  if (a > 0 && b > 0) {
      // a와 b 모두 양수일 때 실행
  }
  ```

#### 4.7 콤마 연산자

콤마 연산자는 여러 개의 표현식을 나열할 때 사용됩니다. 왼쪽부터 차례로 평가되며, 마지막 표현식의 값이 반환됩니다.

```c
int x, y, z;
x = (y = 10, z = 20); // z = 20의 값이 x에 저장됨
```

#### 4.8 연산자의 우선순위와 결합방향

연산자는 특정 우선순위를 가지며, 동일한 우선순위를 가진 연산자들은 결합 방향에 따라 평가됩니다. 예를 들어, 산술 연산자는 관계 연산자보다 우선순위가 높습니다.

- **우선순위 예시**:
  1. `()`
  2. `*`, `/`, `%`
  3. `+`, `-`

### 5. 키보드로부터의 데이터 입력과 C 언어 키워드

#### 5.1 키보드로부터 정수 입력: scanf 함수

`scanf` 함수는 사용자가 키보드로부터 입력한 값을 변수에 저장하는 데 사용됩니다. `%d`는 정수를 입력받을 때 사용되는 형식 지정자입니다.

```c
int num;
scanf("%d", &num); // 사용자로부터 정수 입력을 받아 num에 저장
```

#### 5.2 입력의 형태를 다양하게 지정 가능

`scanf` 함수는 다양한 자료형에 맞는 입력 형식 지정자를 사용할 수 있습니다:

- **정수**: `%d`
- **문자**: `%c`
- **실수**: `%f`
  ```c
  float f;
  scanf("%f", &f); // 사용자로부터 실수 입력을 받아 f에 저장
  ```

#### 5.3 C 언어의 표준 키워드

C 언어는 특정 의미를 가진 키워드를 미리 정의하고 있으며, 이 키워드는 변수명으로 사용할 수 없습니다. 예를 들어, `int`, `return`, `if` 등은 모두 C 언어의 키워드입니다.

### 6. scanf() vs scanf_s()

`scanf_s`는 보안 강화를 위한 함수로, 입력받는 데이터의 크기를 명시적으로 지정해야 합니다. 예를 들어, 문자열을 입력받을 때는 버퍼의 크기도 함께 전달해야 합니다.

- **scanf 함수**:

  ```c
  char str[20];
  scanf("%s", str);
  ```

- **scanf_s 함수**:
  ```c
  char str[20];
  scanf_s("%s", str, (unsigned)_countof(str));
  ```

`scanf_s`는 C11 표준에서 도입된 함수로, 더 안전한 데이터 입력을 보장합니다.

- Visual C++에서 scanf 함수 사용하는 법
  - 시작 부분에 `#define _CRT_SECURE_NO_WARNINGS` 추가

## 2차시 강의 내용

### 데이터 표현 방식의 이해

#### 1. 컴퓨터가 데이터를 표현하는 방식

컴퓨터는 데이터를 주로 **2진수**로 처리하며, 2진수는 0과 1로 이루어진 숫자 체계입니다. 하지만 이를 사람에게 더 쉽게 표현하기 위해 8진수, 16진수도 자주 사용됩니다.

- **2진수 (Binary)**: 컴퓨터의 기본 데이터 표현 방식. 0과 1로만 구성.
- **10진수 (Decimal)**: 인간이 주로 사용하는 숫자 체계. 0~9의 숫자로 구성.
- **8진수 (Octal)**: 0에서 7까지의 숫자를 사용하여 2진수를 간단히 표현하는 방식.
- **16진수 (Hexadecimal)**: 0~9와 A~F(10~15)를 사용하여 2진수를 간결하게 표현하는 방식.

##### 데이터 표현 단위

- **비트(Bit)**: 컴퓨터가 표현할 수 있는 가장 작은 데이터 단위. 0 또는 1.
- **바이트(Byte)**: 8개의 비트로 구성된 데이터 단위. 일반적으로 하나의 문자를 표현할 수 있음.
- **메모리의 주소**: 메모리는 1바이트 단위로 할당되며, 각 주소는 1바이트 크기의 데이터를 참조. 데이터는 주로 바이트 단위로 처리됨.

##### 2진수를 8진수 또는 16진수로 변환

2진수를 직접 변환할 때는 2진수의 자릿수를 묶어 변환합니다:

- **2진수 → 8진수**: 3자리씩 묶어 변환 (예: `101110` → `056`).
- **2진수 → 16진수**: 4자리씩 묶어 변환 (예: `11111111` → `0xFF`).

##### 8진수와 16진수 데이터 표현

- **8진수**는 `0`로 시작, `%o`로 출력 (`0123`),
- **16진수**는 `0x`로 시작, `%x`로 출력 (`0x1A`).
- 양의 정수에만 표현하며, 음의 정수에는 잘 사용되지 않음.

---

#### 2. 2진수와 10진수 변환

##### 2진수 → 10진수

2진수는 각 자리에 해당하는 2의 거듭제곱을 곱하여 10진수로 변환합니다.

- 예: `1101` (2진수) → (1 × 2^3 + 1 × 2^2 + 0 \* 2^1 + 1 × 2^0 = 13) (10진수)

##### 10진수 → 2진수

10진수를 2로 계속 나누어 몫이 0이 될 때까지 나누고, 나머지를 역순으로 나열합니다.

- 예: 13 (10진수) → 1101 (2진수)
  10진수 소수를 2진수로 변환할 때는 소수 부분을 2로 곱하고 정수 부분을 따로 기록합니다. 이 과정을 소수가 0이 될 때까지 반복합니다.
- 예: `0.625`를 2진수로 변환하면, 0.625×2=1.250.625 × 2 = 1.250.625×2=1.25, 0.25×2=0.50.25 × 2 = 0.50.25×2=0.5, 0.5×2=1.00.5 × 2 = 1.00.5×2=1.0이므로 `0.101` (2진수)로 표현됩니다.

---

#### 3. 정수와 실수의 표현 방식

##### 정수의 표현 방식

- **부호와 크기(Sign and magnitude)**: 첫 비트는 부호(0은 양수, 1은 음수)를 나타내고 나머지 비트는 숫자의 크기를 나타냄.
  - **MSB (Most Significant Bit)**: 최상위 비트로, 일반적으로 부호를 나타냄.
  - **LSB (Least Significant Bit)**: 최하위 비트로, 실제 값의 가장 작은 자릿수를 나타냄.
- **2의 보수(Two's complement)**: 음수를 표현하는 가장 널리 쓰이는 방법으로, 양수와 음수를 동일한 방식으로 처리할 수 있음. 최상위 비트는 여전히 부호를 나타냄.

##### 2의 보수 표기법의 특징

- 2의 보수는 음수를 쉽게 표현할 수 있고, 음수와 양수의 덧셈을 동일한 방식으로 처리할 수 있다는 장점이 있습니다.
- 음수 계산: 숫자를 비트 단위로 뒤집고 1을 더하면 음수로 변환됩니다.
- 절댓값이 동일한 양수와 음수 간에는 일정한 관계가 성립합니다.
  - 오른쪽에서 왼쪽으로 읽어나갈 때 첫 번째 1을 만나는 위치까지는 서로 동일함.
  - 그다음 위치는 서로 보수 형태의 패턴으로 구성됨.
- 최상위 비트가 부호 비트로 사용되기 때문에 3비트로 나타낼 수 있는 값의 범위는 -4~3입니다.

##### 정수 연산 시 오버플로우 문제

컴퓨터에서 정수 연산 시 표현할 수 있는 범위를 넘어서는 경우 **오버플로우**가 발생합니다. 예를 들어 8비트 정수에서 `255`(최댓값)에 1을 더하면 다시 `0`으로 돌아갑니다.
부호 비트를 조사하여 오버플로우의 발생 여부를 확인할 수 있습니다.

- 양수끼리 더했을 때 부호가 음수가 되는 경우
- 음수끼리 더했을 때 부호가 양수가 되는 경우

##### 실수의 표현 방식

실수는 **부동소수점(Floating-point)** 방식으로 표현됩니다. 이는 정규화된 수와 지수를 사용하여 실수를 표현하는 방법입니다.

- 예: `123.45`는 `1.2345 x 10^2`로 표현됨.
  **부동소수점**은 실수를 **부호 비트**, **지수**, **가수**로 나누어 표현합니다. - **부호 비트**: 수의 양/음 부호를 나타냅니다. - **지수**: 수의 크기를 나타내며, 8비트의 경우 정숫값 -127을 적용하여 표기됩니다. - **가수**: 소수점 이하의 유효숫자를 나타냅니다.
  실제 `float` 타입과 `double` 타입의 표현 방식
- **float**: 32비트, 부호 비트(1비트), 지수(8비트), 가수(23비트).
- **double**: 64비트, 부호 비트(1비트), 지수(11비트), 가수(52비트).
  **지수**: 정숫값 -127 초과 표기법을 사용 (8비트의 경우).

##### 실수 표현 시 오차

부동소수점 방식은 근사치로 표현되므로 연산 시 **소수점 오차**가 발생할 수 있습니다. 이는 특히 매우 큰 수나 매우 작은 수를 다룰 때 두드러집니다.

---

#### 4. 비트 연산자

비트 연산자는 데이터를 비트 수준에서 조작하는 연산자입니다.

##### & 연산자: 비트 단위 AND

- 두 비트가 모두 1일 때만 결과가 1.
- 예: `1101 & 1011` → `1001`

##### | 연산자: 비트 단위 OR

- 하나라도 1이면 결과가 1.
- 예: `1101 | 1011` → `1111`

##### ^ 연산자: 비트 단위 XOR

- 두 비트가 다를 때만 1.
- 예: `1101 ^ 1011` → `0110`

##### ~ 연산자: 비트 단위 NOT

- 각 비트를 반전(0 → 1, 1 → 0).
- 예: `~1101` → `0010`

##### << 연산자: 비트 단위 왼쪽 이동 (Shift)

- 각 비트를 왼쪽으로 이동. 오른쪽은 0으로 채움. 한 번 이동할 때마다 2배씩 커짐.
- 예: `1011 << 1` → `10110` (2진수), 즉 `11 << 1 = 22` (10진수)

##### >> 연산자: 비트 단위 오른쪽 이동 (Shift)

- 각 비트를 오른쪽으로 이동. 왼쪽은 부호 비트로 채움(정수는 0, 음수는 1). 한 번 이동할 때마다 2배씩 작아짐.
- 예: `1011 >> 1` → `101` (2진수), 즉 `11 >> 1 = 5` (10진수)
- **논리적 이동**과 **산술적 이동**이 있습니다. 논리적 이동은 부호 비트를 고려하지 않으며, 산술적 이동은 부호 비트를 유지합니다. CPU마다 그 동작이 다를 수 있습니다.
