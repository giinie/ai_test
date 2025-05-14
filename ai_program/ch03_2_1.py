# 리스트 생성 및 조회
departments = ["컴퓨터공학과", "전자공학과", "심리학과"]
print(departments)

# 리스트의 요소 개수 조회
print(len(departments))

# 리스트의 개별 요소 조회
print(departments[0])
print(departments[1])

# 음수 인덱스 조회
print(departments[-1])
print(departments[-2])

# 범위를 지정해 조회
print(departments[0:2]) # 0번, 1번 인덱스 조회
print(departments[0:3]) # 0번, 1번, 2번 인덱스 조회

# 리스트에 요소 삽입
departments.append("영어영문학과")
print(departments)

# 리스트에 요소 삽입(변수 사용)
new_department = "반도체학과"
departments.append(new_department)
print(departments)

# 리스트의 요소 삭제
departments.pop() # 마지막 요소 삭제
print(departments)
departments.remove("전자공학과") # 전자공학과 삭제
print(departments)

# 리스트 연결
new_departments = ["기계공학과", "산업공학과"]
departments.extend(new_departments)
print(departments)
