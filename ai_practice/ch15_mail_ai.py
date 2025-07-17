from email.header import decode_header
import streamlit as st
import pandas as pd
import imaplib
import email


# (1) 메일 수신 함수 정의
def fetch_emails(email_id:str, app_password:str) -> pd.DataFrame:
    try:
        mail = imaplib.IMAP4_SSL("imap.naver.com")
        mail.login(email_id, app_password)
        mail.select("inbox")
        result, data = mail.search(None, "ALL")

        if not data[0]:
            print("메일함이 비어있습니다.")
            return None

        mail_ids = data[0].split()[-10:]
        fetched_emails = []
        for mail_id in mail_ids:
            result, data = mail.fetch(mail_id, "(RFC822)")
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            email_data = {
                "날짜": msg.get("Date"),
                "발신인": decode_mime_words(msg.get("From")),
                "제목": decode_mime_words(msg.get("Subject")),
                "본문": get_email_content(msg),
            }
            fetched_emails.append(email_data)
        fetched_emails.reverse()
        # 결과 리스트를 데이터프레임으로 변환
        df = pd.DataFrame(fetched_emails)
        return df
    except Exception as e:
        st.error(f"메일 로딩 중 오류가 발생했습니다: {str(e)}")
        return None


# (2) 메일 발신인/제목 디코딩 함수 정의
def decode_mime_words(encoded_string):
    if encoded_string is None:
        return ""
    decoded_words = decode_header(encoded_string)
    decoded_string = ""
    for content, charset in decoded_words:
        if isinstance(content, bytes):
            try:
                decoded_string += content.decode(charset or "utf-8")
            except (UnicodeDecodeError, TypeError):
                decoded_string += content.decode("latin1", errors="ignore")
        else:
            decoded_string += content
    return decoded_string


# (3) 메일 본문 가져오기 함수 정의
def get_email_content(message):
    if message.is_multipart():
        parts = [get_email_content(part) for part in message.get_payload()
                 if part.get_content_type() == "text/plain"]
        return "\n".join(parts) if parts else ""
    else:
        content_type = message.get_content_type()
        if content_type == "text/plain":
            content = message.get_payload(decode=True)
            if content:
                charset = message.get_content_charset()
                try:
                    return content.decode(charset or "utf-8")
                except (UnicodeDecodeError, TypeError):
                    return content.decode("latin1", errors="ignore")
        return ""


def main():
    st.set_page_config(layout="wide")
    st.title("메일 자동 응답 프로그램")
    st.caption("최근 수신한 메일을 확인하고 답장 초안을 작성해줍니다.")
    # (4) 주요 세션 상태 변수 선언
    if "openai_api_key" not in st.session_state: # OpenAI API Key
        st.session_state.openai_api_key = None
    if "email_id" not in st.session_state: # 네이버 아이디
        st.session_state.email_id = None
    if "app_password" not in st.session_state: # 네이버 비밀번호
        st.session_state.app_password = None
    if "emails" not in st.session_state: # 메일 데이터프레임
        st.session_state.emails = None
    if "client" not in st.session_state: # OpenAI 클라이언트
        st.session_state.client = None
    if "answer_generated" not in st.session_state: # 답장 초안
        st.session_state.answer_generated = None
    if "final_reply" not in st.session_state: # 최종 메일
        st.session_state.final_reply = None
    # (5) 사이드바 생성
    with st.sidebar:
        st.session_state.openai_api_key = st.text_input(
            "OpenAI API Key",
            type="password",
        )
        st.session_state.email_id = st.text_input(
            "네이버 아이디(@ 이하 제외)", key="id"
        )
        st.session_state.app_password = st.text_input(
            "네이버 비밀번호", key="password", type="password"
        )
    # (6) 열 레이아웃 생성
    col1, col2 = st.columns([1.5, 1])
    with col1:
        if st.button("메일 불러오기"):
            if not (
                st.session_state.openai_api_key
                and st.session_state.email_id
                and st.session_state.app_password
            ):
               st.info("API Key, 네이버 아이디와 비밀번호를 입력하세요.")
               st.stop()
            with st.spinner("메일 불러오는 중..."):
                emails_df = fetch_emails(st.session_state.email_id, st.session_state.app_password)
                # (7) 메일 데이터프레임 세션 상태 변수 선언
                if emails_df is not None:
                    st.session_state.emails = emails_df
        if st.session_state.emails is not None:
            # (8) 메일 데이터프레임 출력
            selected_email = st.dataframe(
                st.session_state.emails[["날짜", "발신인", "제목"]],
                hide_index=True,
                on_select="rerun",
                selection_mode="single-row",
                use_container_width=True,
            )
            # (9) 특정 행 선택 시 해당 내용 출력
            if selected_email["selection"]["rows"]:
                selected_index = selected_email["selection"]["rows"][0]
                selected_row = st.session_state.emails.iloc[selected_index]
                email_subject = selected_row["제목"]
                sender = selected_row["발신인"]
                email_content = selected_row["본문"]
                st.write("제목: ", email_subject)
                st.write("발신인: ", sender)
                st.write(email_content)
            else:
                st.write("메일을 선택하세요.")
    with col2:
        st.write("답장 초안")


if __name__ == "__main__":
    main()
