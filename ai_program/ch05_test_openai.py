# (1) 패키지 불러오기
import os
from openai import OpenAI

# (2) OpenAI 클라이언트 생성
client = OpenAI(
    # 발급받은 API Key 입력
	api_key="API_Key_입력"
)
# (3) API 요청 및 응답
chat_completion = client.chat.completions.create(
	messages=[
		{
			"role": "user",
			"content": "Say this is a test.",
		}
	],
	model="gpt-4o",
)
# (4) 응답 결과 출력
print(chat_completion.choices[0].message.content)