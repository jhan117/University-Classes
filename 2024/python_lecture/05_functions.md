# 함수

- [1. 함수 정의와 호출](#함수-정의와-호출)
- [2. 전역 변수와 지역 변수](#전역-변수와-지역-변수)
- [3. 디폴트 인수와 키워드 인수](#디폴트-인수와-키워드-인수)
- [4. 패킹과 언패킹](#패킹과-언패킹)
- [5. 익명 함수와 람다 함수](#익명-함수와-람다-함수)
- [6. 재귀 함수](#재귀-함수)
- [7. 중첩 함수와 데코레이터](#중첩-함수와-데코레이터)
- [8. 모듈과 패키지](#모듈과-패키지)
- [9. 내장 함수](#내장-함수)

## 함수 정의와 호출

```python
def FunctionName(parameters):
    statement

FunctionName()
```

[ 문제1 ] : 사칙연산 함수 만들기

```python
OPERATOR = ["+", "-", "*", "/"]


def Calc(fNum, sNum):
    if sNum == 0:
        print("나눌 수 없음.")
    else:
        for o in OPERATOR:
            expresss = f"{fNum} {o} {sNum}"
            print(f"{expresss} = {eval(expresss)}")


fNum, sNum = map(int, input("2개의 숫자 입력 : ").split())
Calc(fNum, sNum)
```

[ 문제2 ] : 최소값, 최대값 반환 함수

```python
def GetMinMax(data):
    return min(data), max(data)


min_value, max_value = GetMinMax([5, 6, 3, 9, 8, 1, 4])
print(f"최소값 : {min_value}\n최대값 : {max_value}")
```

```python
def GetMinMax(data):
    """
    max, min 함수 미사용 버전
    """
    max_value = -1
    min_value = float("inf")
    for d in data:
        if max_value < d:
            max_value = d
        if min_value > d:
            min_value = d

    return min_value, max_value
```

## 전역 변수와 지역 변수

- 전역 변수 : 함수 외 및 함수 내 -> 편하지만 권장하지 않음
- 지역 변수 : 함수 내

```python
def GetArea():
    global area # 읽기/쓰기 가능
    area = 3.14 * radius ** 2 # radius 읽기만 가능

radius = 1
```

## 디폴트 인수와 키워드 인수

```python
# y 값을 기본값으로 2로 설정
# (x = 2, y) 불가능 뒤부터 가능
def Power(x, y = 2):
    return x ** y

Power(1, 2) # 위치에 대응하는 것 : 위치 인수
Power(y = 3, x = 1) # 지정해서 주는 것 : 키워드 인수
```

[ 문제 ] : RangeSum(m, n, gap) 함수 만들기

```python
def RangeSum(m, n, gap=1):
    max_num = n if m < n else m
    min_num = m if m < n else n
    result = min_num
    next_num = min_num + gap

    while next_num <= max_num:
        result += next_num
        next_num += gap

    return result
```

## 패킹과 언패킹

- 패킹 : 콤마로 된 데이터를 묶는 것
- 언패킹 : 각각 다른 변수들에 저장하는 것
- \* 사용하면 리스트로 묶어서 가능

```python
tuple1 = 1, 2, 3 # 패킹 튜플
t1, t2, t3 = (1, 2, 3) # 언패킹 튜플
l1, l2, l3 = [1, 2, 3] # 언패킹 리스트
d1, d2 = {"coke" : 100, "sprite" : 50} # 딕셔너리 키 언패킹
s1, s2, s3 = "Ace" # 언패킹 문자열

# 튜플, 리스트, 딕셔너리 모두 *사용시 리스트로 변환됨
t1, *t2, t3, t4 = (1, 2, 3, 4, 5) # 출력 : 1, [2, 3], 4, 5

# 함수 매개변수 전달에 사용해보기
def Sum1(x, *others):
    return x + sum(others)

print(Sum1(*(1, 2, 3))) # 1, (2, 3)으로 전달

# 딕셔너리는 **로 가능
def Sum(coke, sprite, **price):
    # 패킹
    for key in price:
        print(key, ":", price[key])
    return coke, sprite


items = {"coke": 100, "sprite": 50}
print(Sum(**items, coke_price=100, sprite_price=50)) # 언패킹

# for문 언패킹
students = [("홍길동", 100), ("이순신", 90)]

for name, score in students:
    print(name, score)
```

[ 문제 ] : 튜플 패킹, 양수의 합과 음수의 합을 따로 계산하여 반환

```python
def Sum(*numbers):
    positive_sum = 0
    negative_sum = 0
    for n in numbers:
        if n > 0:
            positive_sum += n
        else:
            negative_sum += n

    return positive_sum, negative_sum


print(Sum(1, -2, 3.6, 5, -8.2, 4))
```

## 익명 함수와 람다 함수

- 이름이 없는 함수 = 익명 함수 = 람다 함수

`lambda parameters: expression`

```python
(lambda x, y: x + y)(3, 4)

# 변수 저장
sum1 = lambda x, y: x + y
print(sum1(3, 4))

# 매개변수로 람다를 사용해 함수 전달하기
def Change(method, data):
    new_data = []
    for num in data:
        new_data.append(method(num))
    return nuw_data

values = [1, 2, 3, 4]
print(Change(lambda x: x ** 2, values))

# 기존 함수를 호출하기 힘든 상황
# 함수를 등록만 하고 추후 실행되는 상황에서도 이상 없이 실행 가능
def Sum(x, y):
    return sum(range(x, y + 1))

for i in [1, 2]:
    for j in [10, 20]:
        print((lambda x = i, y = j: Sum(x, y))())
```

[ 문제 ] : turtle 이벤트 함수로 람다 함수 사용, 왼쪽 버튼 빨간색, 오른쪽 버튼 파란색

```python
import turtle as t

t.speed(0)


def Draw(x, y, color):
    t.teleport(x, y)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(20)
    t.end_fill()


s = t.Screen()
s.onclick(lambda x, y: Draw(x, y, "red"), 1)
s.onclick(lambda x, y: Draw(x, y, "blue"), 3)
s.listen()

t.done()
```

## 재귀 함수

- 재귀 호출 : 어떤 함수가 자기 자신을 호출하는 것
- 재귀 함수 : 재귀 호출을 포함하는 함수(무한 루프 주의)

### 예제

```python
def recursion_sum(m, n):
    """
    m부터 n까지 더하는 함수
    """
    if m == n:
        return m    # 탈출 조건
    else:
        return m + recursionSum(m + 1, n)   # 재귀 호출

def hanoi_tower(n, source, auxiliary, destination):
    """
    3 개 기둥, 원판들 다른 곳에 옮기기
    source : 시작
    destination : 도착
    auxiliary : 보조
    [ 조건 ]
    1. 한 번에 하나의 원판
    2. 가장 위의 원판만 다른 기둥의 가장 위에 이동 가능
    3. 더 작은 원판 위로 이동 불가능
    [ 알고리즘 ]
    1. 상위 n - 1개 원판을 auxiliary로 이동(시작은 가장 큰 원판만 남음)
    2. 나머지 큰 원판 1개를 destination으로 이동
    3. auxiliary에 있는 n - 1개 원판을 destination으로 이동
    """
    if n == 1:
        print(source, "=>", destination)
        return
    hanoi_tower(n - 1, source, destination, auxiliary)
    hanoi_tower(1, source, auxiliary, destination)
    hanoi_tower(n - 1, auxiliary, source, destination)

print(recursion_sum(1, 10))
hanoi_tower(3, "A", "B", "C")
```

### 실습

```python
import turtle as t
import math


def draw_triangle(length):
    """
    재귀 함수를 이용해 중첩 삼각형을 turtle로 구현하기
    [ 조건 ]
    1. 한 변의 길이에 따라 삼각형 그리기
    2. 길이가 20보다 작으면 함수 탈출
    3. 길이가 20 이상이면 길이 값을 길이/2로 갱신하고 길이만큼 이동 후 다시 삼각형 그리기
    """
    if length < 20:
        print("삼각형 그리기 종료")
        return

    t.right(60)
    for _ in range(3):
        t.forward(length)
        t.right(120)
    t.forward(length / 2)
    draw_triangle(length / 2)


if __name__ == "__main__":
    L = 1000
    t.teleport(0, L * math.sqrt(3) / 4)
    draw_triangle(L)
    t.exitonclick()
```

## 중첩 함수와 데코레이터

- 중첩 함수 : 함수 내부에 함수를 작성하는 것(중첩 함수 포함하는 함수 내에서만 호출 가능)
- 데코레이터 : 어떤 함수 실행 시 그 전후에 필요한 작업이 있을 때 사용한다.

### 예제

```python
def generate_power_of_n(n):
    """중첩함수 : n의 y승 구하기"""

    def power(y):
        nonlocal n  # 여기서 불필요하지만 nonlocal 읽기/쓰기 모두 가능
        return n**y

    return power # 함수 반환


power_fun1 = generate_power_of_n(2)
print(power_fun1(3))

# 데코레이터 예제
def hello(func):
    """
    기존 방법
    1. A, func, b 실행 -> 번거로움
    2. func를 매개변수로 전달 -> 번거로움 ex) hello(sum_func, x, y) 전달해야 함
    """

    def deco_func(x, y):
        print("함수 시작")
        func(x, y)
        print("함수 종료")

    return deco_func  # 함수 반환


@hello
def sum_func(x, y):
    print(f"+ : {x + y}")


@hello
def sub_func(x, y):
    print(f"- : {x - y}")


sub_func(3, 4)
```

### 실습

```python
def input_output_deco(func):
    """
    2개 입력 받고 결과 출력
    """

    def wrapper():
        x, y = map(int, input("숫자 2개 입력: ").split())
        answer = func(x, y)
        print(f"계산 결과 : {answer}")

    return wrapper


@input_output_deco
def sum_func(x, y):
    return x + y


@input_output_deco
def sub_func(x, y):
    return x - y


sum_func()
sub_func()
```

## 모듈과 패키지

- 모듈 : 파이썬 코드를 포함하고 있는 .py 파일(모듈에 있는 걸 사용하려면 import 필요)
- 모듈명 : 확장자 .py 제외한 파일명
- 패키지 : 1개 이상의 모듈을 포함하는 폴더(import 시 자동 import 됨 \_\_init\_\_.py 파일 포함)

### 예제

```python
# my_math.py
print("my_math 모듈")

def sum_func(x, y):
    return x + y
def avg_func(x, y):
    return (x + y) /2
def pow_func(x, y):
    return x ** y

# print(__name__) -> __main__
if __name__ == "__main__": # 테스트 용도이며 하단의 prog.py에서 실행 안됨
    print("테스트 sum : ", sum_func(3, 4))

# prog.py -> 모듈 import 방법
import my_math  # 모듈만 임포트
from my_math import *   # 모든 함수 임포트
from my_math import sum_func, avg_func  # 특정 함수만
import my_math as mm    # 별칭
from my_math import avg_func as average, pow_func as power  # 각 별칭

print(my_math.__name__) # my_math로 출력됨
```

[ 명령 프롬프트 사용(cmd) ]

```python
# 파이썬 파일 실행 시 데이터 아래처럼 전달
# python 모듈명.py num1 num2
import sys

print(f"전달된 데이터 : {sys.argv}")

if len(sys.argv) != 3:
    print("실행 오류 오른쪽처럼 입력 : python lecture_test.py 3 4")
else:
    num1, num2 = map(int, sys.argv[1:])
    print(f"{num1} + {num2} = {num1 + num2}")
```

[ 패키지 ]

```python
# my_util 폴더
# __init__.py
def sum_func(x, y):
    return x + y
# my_mt.py
def pow_func(x, y):
    return x**y

# test.py
import my_util # 패키지 가져옴 (__init__모듈 사용 가능)
sum_func(3, 4)

# 둘 다 사용 가능
import my_util.my_mt as mt
from my_util import my_mt as mt
mt.pow_func(3, 4)
```

### 실습

```python
import sys

if len(sys.argv) != 4:
    print("실행 오류 : python lecture_test.py * 3 4")
else:
    operator = sys.argv[1]
    num1, num2 = map(int, sys.argv[2:])
    express = f"{num1} {operator} {num2}"
    result = eval(express)
    print(f"{express} = {result}")
```

## 내장 함수

- [내장 함수(링크 확인)](https://docs.python.org/ko/3/library/functions.html) : 별도의 모듈 import 없이 사용 가능

1. filter(function, iterable) : 리스트 요소 중 함수의 반환값이 참인 요소로만 만든 filter 객체 반환
2. map(function, iterable, \*iterables) : 리스트 각 요소에 대해 주어진 함수를 실행한 후 반환 값으로 map 객체 반환
3. enumerate(iterable, start=0) : 리스트 각 요소에 대해 인덱스 부여한 튜플로 이뤄진 enumerate 객체 반환
4. zip(\*iterables, strict=False) : 리스트들의 대응되는 각 요소들을 하나의 튜플로 만듦

```python
ages = [23, 15, 5, 34, 54]
scores = zip(["a", "b", "c"], [100, 90, 80], [3, 2, 1])

for i, s in enumerate(scores):
    print(i, s)

print(dict(zip(["a", "b", "c"], [100, 90, 80])))  # zip 객체 반환


def adult_condition(age):
    return True if age >= 18 else False


print(list(filter(adult_condition, ages)))  # filter 객체 반환
print(list(map(adult_condition, ages)))  # map 객체 반환
```

### 실습

```python
# 3의 배수인 값을 제곱해서 반환
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiple3 = list(filter(lambda x: True if x % 3 == 0 else False, nums))
print(list(map(lambda x: x**2, multiple3)))
```
