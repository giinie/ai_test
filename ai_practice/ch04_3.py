import streamlit as st

# 페이지 환경 설정
st.set_page_config(
    page_title = "AI 프로그램",  # 웹 페이지 제목
    page_icon = "🤖",          # 웹 페이지 아이콘
    layout = "wide",           # 웹 페이지 레이아웃: 넓게
)

# 인사말 출려
col1, col2 = st.columns(2)  # 두 개의 열 생성 후 각 열을 변수에 저장
with col1:                  # 왼쪽 열 활성화
    st.write("첫 번째 열입니다")     # 왼쪽 텍스트 출력
    st.write("안녕하세요!")
with col2:                  # 오른쪽 열 활성화
    st.write("두 번째 열입니다.")   # 오른쪽 텍스트 출력
    st.write("반갑습니다.")

