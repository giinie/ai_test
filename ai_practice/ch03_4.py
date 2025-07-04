# 함수 정의
def say_hello(name):
    greeting = "안녕!"
    print(f"{name} {greeting}")
    return greeting  # greeting 값을 반환


# say_hello1 함수에서 greeting 변수 사용
def say_hello1(name):
    greeting = "안녕!"
    print(f"{name} {greeting}")


# say_hello2 함수에서 greeting 변수 사용
def say_hello2(name):
    greeting = "안녕하세요."
    print(f"{name} {greeting}")


# 함수 호출
returned_greeting = say_hello("철수")
print(returned_greeting)
say_hello1("철수")
say_hello2("영희")

# 함수 밖에서 greeting 변수 사용
greeting = "이게 진짜 인사입니다."
print(greeting)
