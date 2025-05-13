# (1) 패키지 불러오기
from openai import OpenAI

# (2) OpenAI 클라이언트 생성
client = OpenAI(
	api_key="API_Key_입력",
)
# (3) 대화 내역을 저장할 리스트 선언
message_history = []
# (4) 대화 시작
while True:
	user_input = input("사용자: ")
	# (5) 사용자의 질문을 리스트에 추가
	message_history.append({"role": "user", "content": user_input})
	# (6) API 요청 및 응답
	chat_completion = client.chat.completions.create(
		model="gpt-4o",
		messages=message_history,
	)
	# (7) 챗봇의 응답을 리스트에 추가
	assistant_response = chat_completion.choices[0].message.content
	message_history.append({"role": "assistant", "content": assistant_response})
	# (8) 응답 결과 출력
	print(f"챗봇: {assistant_response}")