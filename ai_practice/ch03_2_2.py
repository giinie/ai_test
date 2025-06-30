# 딕셔너리 생성 및 조회
department = {"학과명": "수학과", "인원": 120, "설립연도": 1985}
print(department)
print(department["인원"])

# 모든 키, 모든 값, 모든 키-값 조회
print(department.keys())
print(department.values())
print(department.items())

# 키-값 쌍 삽입
department["건물명"] = "자연관"
print(department)

# 건물명 키 삭제
del department["건물명"]
print(department)

# 인원 키 값 수정
department["인원"] = 130
print(department)

# 여러 키-값 쌍 수정
department.update({"설립연도": 1990, "건물명": "과학관"})
print(department)

