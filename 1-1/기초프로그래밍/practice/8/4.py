"""
실습: pickle load 메서드 실행 시 예외 처리

다음 코드는 pickle 모듈을 통해 int 객체 n 개를 "test.dat" 파일로 저장하고 있다.
pickle 모듈의 load 메서드를 사용하여 해당 파일로부터 첫 번째 int 객체부터 마지막 int 객체까지 하나씩 차례로 읽어들이고 값을 화면에 출력하라.
현재 ”test.dat" 파일에는 몇 개의 int 객체가 저장되어 있는지 알 수 없다고 가정한다.

- load 메서드는 더 이상 읽을 데이터가 없다면 EOFError 예외를 발생시킨다.
- finally 블록을 통해 파일을 닫도록 하라.
"""
import pickle
import sys

n = int(input("몇 개의 int를 저장할까요? "))
file = open("resource/test.dat", "wb")

for i in range(n):                    # 0부터 차례로
    pickle.dump(i, file)              # int 객체 쓰기

file.close()


read_file = open("resource/test.dat", "rb")

try:
    while True:
        data = pickle.load(read_file)
        print(data)
except EOFError as e:
    print("EOFError 발생: ", e)
finally:
    read_file.close()
