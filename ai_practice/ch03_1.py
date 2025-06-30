# 변수 선언과 값 할당
x = 3
print(x)

# 변수 연산
x = x + 3
print(x)

# input() 함수 사용
# name = input("이름을 입력해주세요: ")
# print("안녕하세요. " + name + "님!")

# 정수형과 실수형 데이터 저장
a = 10
b = -5
pi = 3.14
print(a, b, pi)

# 문자형 데이터 저장
greeting = "안녕"
message = '파이썬은 재미있어요.'
multiline_message = """파이썬은
여러 줄 문자열도
쉽게 작성할 수 있어요.
"""
print(greeting)
print(message)
print(multiline_message)

# 불형 데이터 출력
print(3 > 1)
print(5 == 5)
print(10 != 10)

# 불형 데이터 저장
a = 5
b = 5
result = (a == b)
print(result)

# 간단한 사칙연산
print(1 + 3)
print(5 - 2)
print(4 * 3)
print(10 / 2)

# 자료형이 다른 데이터의 연산
# print(3 + '안녕')
print(f"{3} 안녕")

# 문자열의 더하기
print("철수" + "야 " + "안녕!" )
print("반가워! " * 2)

# 변수를 이용한 문자열의 더하기
name = "철수"
greeting = "안녕!"
message = name + "야 " + greeting
print(message)

# f-문자열 사용
name = "철수"
greeting = "안녕!"
message = f"{name}야 {greeting} 반가워!"
print(message)
