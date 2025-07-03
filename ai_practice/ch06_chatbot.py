import os

import streamlit as st
from openai import OpenAI  # (9) openai 패키지에서 OpenAI 클래스 불러오기


# (1) main() 함수 선언
def main():
    # (2) 메인 화면 구성
    st.set_page_config(layout="wide")
    st.title("친근한 AI 챗봇")
    st.caption("스트림릿과 OpenAI API를 활용한 간단한 챗봇")
    # (3) 사이드바 구성
    with st.sidebar:
        st.subheader("OpenAI API Key 설정")
        # (4) 입력 위젯 유형 설정(비밀번호)
        ai_test_api_key = os.environ.get("OPENAI_API_KEY")
        openai_api_key = st.text_input("OpenAI API Key", type="password", value=ai_test_api_key)
        st.write("[OpenAI API Key 받기](https://platform.openai.com/account/api-keys)")
    # (13) 시스템 프롬프트 추가
    system_message = """
    너의 이름은 친구 봇이야.
    너는 항상 반말을 하는 챗봇이야. 절대로 다나까 같은 높임말을 사용하지 마.
    항상 반말로 친근하게 대답해줘.
    영어로 질문을 받아도 무조건 한글로 대답해줘.
    한글이 아닌 답변을 하게 되면 다시 생각해서 답변을 꼭 한글로 만들어줘.
    모든 답변 끝에 답변에 맞는 이모티콘도 추가해줘.
    """
    # (14) 대화 내용 관리를 위한 세션 상태 설정
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": system_message}]
    # (15) 기존 대화 내역 표시
    idx = 0  # 대화 내역 순번 기록용
    for message in st.session_state.messages:
        if idx > 0:  # 시스템 프롬프트는 표시하지 않음
            with st.chat_message(message["role"]):
                st.write(message["content"])
        idx = idx + 1
    # (10) OpenAI 클라이언트 생성
    client = OpenAI(api_key=openai_api_key)
    # (6) 입력창과 대화창 구현
    user_input = st.chat_input("무엇이 궁금한가요?")
    if user_input:
        # (16) 세션 상태 리스트에 사용자의 질문 추가
        st.session_state.messages.append({"role": "user", "content": user_input})
        # (7) 사용자의 질문 출력
        with st.chat_message("user"):
            st.write(user_input)
        # (17) API 요청 및 응답
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages,
                stream=True,
            )
            response = st.write_stream(stream)
        # (18) 세션 상태 리스트에 챗봇의 응답 추가
        st.session_state.messages.append({"role": "assistant", "content": response})
        # (11) API 요청 및 응답
        # (8) 챗봇의 응답 출력
        # with st.chat_message("assistant"):
        #     # st.write("안녕! 난 친구 봇이야.")
        #     response = client.chat.completions.create(
        #         model="gpt-4o-mini",
        #         messages=[{"role": "assistant", "content": user_input}],
        #         stream=True,
        #     )
        # (12) 응답 결과 출력
        # st.write_stream(response)


# (5) main() 함수 실행
if __name__ == "__main__":
    main()
