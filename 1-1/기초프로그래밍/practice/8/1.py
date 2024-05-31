"""
실습: 특정 문자열 변경 후 저장

사용자로부터 입력 파일 이름과 출력 파일 이름, 그리고 찾을 문자열과 변경 문자열을 입력받은 후
입력 파일 내에서 찾을 문자열을 모두 변경 문자열로 변경하고 출력 파일로 저장하라.
- 문자열(str) 클래스의 replace 메서드를 사용할 수 있다.
"""

input_f_name = input("입력 파일 이름: ")
output_f_name = input("출력 파일 이름: ")
before_string = input("변경 전 문자열: ")
after_string = input("변경 후 문자열: ")

input_file = open(f"resource/{input_f_name}", "r", encoding="utf-8")

output_file = open(f"resource/{output_f_name}", "w", encoding="utf-8")
output_file.write(input_file.read().replace(before_string, after_string))

input_file.close()
output_file.close()

print("파일 변경 및 복사 작업 성공!!!")