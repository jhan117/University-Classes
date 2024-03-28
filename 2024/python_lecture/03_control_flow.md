# Control Flow Tools

프로그램 실행 흐름

- 순차적 흐름
- 선택적 흐름 : 조건문 (if, match)
- 반복적 흐름 : 반복문 (for, while)

## If statement

```python
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3

# Short Hand If
statement1 if condition1 else statement2 if condition2 else statement3
```

[ 문제1 ] : 가위, 바위, 보 입력 -> 컴퓨터 무작위 생성 -> 승패 판단 출력

```python
import random

WIN = "You win!"
LOSE = "You lose."

user_action = input("가위, 바위, 보 입력: ")
possible_actions = ["가위", "바위", "보"]
computer_action = random.choice(possible_actions)

print(f"\n당신은 {user_action}를 냈습니다.\n컴퓨터는 {computer_action}를 냈습니다.\n")

if user_action == computer_action:
    print("It's a tie!")
elif user_action == "바위":
    if computer_action == "가위":
        print(WIN)
    else:
        print(LOSE)
elif user_action == "보":
    if computer_action == "바위":
        print(WIN)
    else:
        print(LOSE)
elif user_action == "가위":
    if computer_action == "보":
        print(WIN)
    else:
        print(LOSE)
```

[ 문제2 ] : 정수 2개 입력 -> 최댓값 출력

```python
num1, num2 = map(int, input("정수 2개 입력: ").split())

print(num1) if num1 > num2 else print(num2)
```

## Match statement

3.10 버전 이후에 도입되었다.

```python
match subject:
    case pattern1:
        statement1
    case pattern2:
        statement2
    case _:
        statement3
```

[ 문제 ] : 2개 숫자, 연산자 입력 -> 결과 출력

```python
user_input = input("2개의 숫자와 연산자 입력: ").split()
num1, num2 = map(int, user_input[:-1])
operator = user_input[-1]
SENTENCE = f"{num1} {operator} {num2}"

match operator:
    case "+":
        print(f"{SENTENCE} = {num1 + num2}")
    case "-":
        print(f"{SENTENCE} = {num1 - num2}")
    case "*":
        print(f"{SENTENCE} = {num1 * num2}")
    case "/":
        print(f"{SENTENCE} = {num1 / num2}")
```

## While statement

```python
while condition:
    statement
else:
    statement
```

[ 문제1 ] : 구구단 전체 출력

```python
i = 2

while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1
```

[ 문제2 ] : turtle로 정사각형 그리기

```python
import turtle as t

i = 0
LEN = 100
while i < 4:
    t.forward(LEN)
    t.left(90)
    i += 1

t.done()
```

## For statement

```python
for var in iterable:
    statement
else:
    statement
```

sequence object : a list, a tuple, a dictionary, a set, a string...

[ 문제1 ] : 구구단 전체 출력

```python
for i in range(2, 10):
    for j in range(10):
        print(f"{i} x {j} = {i * j}")
```

[ 문제2 ] : 두 숫자 사이의 값들 합산하기

```python
fNum, sNum = map(int, input("정수 2개 입력 : ").split())

ans = 0
for i in range(fNum, sNum+1):
    ans += i

print(f"합계 : {ans}")
```

[ 문제3 ] : turtle로 정사각형 그리기

```python
import turtle as t

LEN = 100
for i in range(4):
    t.forward(LEN)
    t.left(90)

t.done()
```

## pass, break, continue statement

- pass : 나중에 작성할 때 문법 에러 발생 방지용
- break : 반복 루프 빠져나감
- continue : 현재 반복 스킵하고 다시 실행

[ 문제 ] : 1부터 i 까지의 합산 결과가 n을 넘지 않는 가장 큰 i 값 구하기

```python
num = int(input("2 이상의 자연수 1개 입력 : "))

i = 1
total = 0
while True:
    check = total + i

    if check > num:
        print(f"{num}를 넘지 않는 1+...+i의 가장 큰 i값은 {i - 1}이고, 그때 합산 결과는 {total}입니다")
        break

    total += i
    i += 1
```
