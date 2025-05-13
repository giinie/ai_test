# 조건문 작성 및 실행
language = "자바"
if language == "파이썬":
    print("파이썬을 사용합니다.")
elif language == "자바스크립트":
    print("자바스크립트를 사용합니다.")
else:
    print("기타 언어를 사용합니다.")

# for 문 작성 및 실행
departments = ["컴퓨터공학과", "전자공학과", "반도체학과"]
years = ["1학년", "2학년"]
for item in departments:
    for year in years:
        print(f"{item} - {year}")

# range() 함수 사용
for number in range(1, 11):
    print(number)

# while 문 작성 및 실행
number = 1
while number <= 5:
    print(number)
    number = number + 1

# while 문을 for 문으로 변환
for number in range(1, 11):
    print(number)
    if number == 5:
        break