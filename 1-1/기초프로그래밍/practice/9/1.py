"""
실습: 무한한 임의의 값 생성하기

리스트로 만들어 반환하는 경우 무한한 요소를 갖는 리스트를 만들 수 없다.
제너레이터 함수를 사용하여 next 함수 또는 for 문을 통해 1과 10 사이의 값이 무한히 제공될 수 있도록 만들어 보라.
이때 몇 번째 생성되는 값인지도 함께 전달받도록 하라.
"""
import random


# GetANumber 함수를 작성하라.
def get_number():
    count = 0

    while True:
        count += 1
        yield count, random.randint(1, 10)


var = get_number()
count, value = next(var)
print(f"{count} : {value}")

for count, value in var:
    print(f"{count} : {value}")
    
    if count == 5:
        break