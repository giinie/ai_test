import streamlit as st
import pandas as pd

# (1) 데이터 정의
data = [
    {'영양 성분': '열량', '1봉지당': '85kcal', '총 내용량당': '343kcal', '일일 기준치 대비(%)': '-'},
    {'영양 성분': '나트륨', '1봉지당': '85mg', '총 내용량당': '338mg', '일일 기준치 대비(%)': '17%'},
]
# (2) 데이터프레임 생성
df = pd.DataFrame(data)
# (3) 스트림릿에서 데이터프레임 출력
st.dataframe(df)