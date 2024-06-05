"""
실습: combinations()

정수값들로 이루어진 리스트가 주어질 때 3개를 선택하는 조합들 중 합이 10인 조합을 추출한다.
그리고 각 조합에 대해 곱셈을 적용한 결과를 출력하라.
- combinations 함수를 사용하라.
"""

import itertools


data = [5, 2, 3, 7, 1, 7, 8, 5, 9, 4, 6]

comb_data = itertools.combinations(data, 3)
filter_data = itertools.filterfalse(lambda x: list(itertools.accumulate(x))[-1] != 10, comb_data)

for d in filter_data:
    (a, b, c) = d
    print(f"{a} * {b} * {c} = {a * b * c}")
