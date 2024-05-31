"""
실습: 파일 데이터 읽기

score.txt 파일의 내용을 읽어 화면에 출력하고 마지막에 점수를 합산한 결과를 출력하라.
"""

result = 0

file = open(f"resource/score.txt", "rt+", encoding="utf-8")

for line in file:
    name, score = line.split()
    print(name, score)
    result += int(score)

print(f"합계: {result}")

file.close()
