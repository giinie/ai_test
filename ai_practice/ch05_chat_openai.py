from openai import OpenAI

# (1) OpenAI 클라이언트 생성
openai_api_key = "test"
client = OpenAI(
    # api_key=os.environ.get("OPENAI_API_KEY"),
    api_key=openai_api_key
)

# (2) 대화 내역을 저장할 리스트 선언
message_history = []

# (3) 대화 시작
while True:
    user_input = input("사용자: ")
    # (4) 사용자의 질문을 리스트에 추가
    message_history.append({"role": "user", "content": user_input})
    # (5) API 요청 및 응답
    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=message_history,
    )
    # (6) 챗봇의 응답을 리스트에 추가
    assistant_response = chat_completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": assistant_response})
    # (7) 응답 결과 출력
    print(f"챗봇: {assistant_response}")
