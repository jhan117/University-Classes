"""
실습: Point 클래스 객체 파일 쓰기/읽기

다음 코드에는 Point 객체 pt1, pt2, pt3이 있다.
이 코드를 포함하고, pickle 모듈을 사용하여 pt1, pt2, pt3을 차례로 "point.dat" 파일로 저장한 후
다시 하나씩 읽어서 화면에 출력(print 함수 사용) 해 보라.
"""
import pickle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, pt):
        new_pt = Point(self.x + pt.x, self.y + pt.y)
        return new_pt

    def __str__(self):
        return f"({self.x}, {self.y})"


pt1 = Point(1, 2)
pt2 = Point(3, 4)
pt3 = pt1 + pt2

file = open("resource/point.dat", "wb")
pickle.dump(pt1, file)
pickle.dump(pt2, file)
pickle.dump(pt3, file)
file.close()

re_open = open("resource/point.dat", "rb")
pt1 = pickle.load(re_open)
pt2 = pickle.load(re_open)
pt3 = pickle.load(re_open)
re_open.close()

print(pt1, pt2, pt3, sep="\n")
