import os
from openai import OpenAI

# OpenAI 클라이언트 생성
# openai_api_key = "test"
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    # api_key = openai_api_key,
)

# API 요청 및 응답
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test.",
        }
    ],
    model="gpt-4o-mini",
)

# 응답 결과 출력
print(chat_completion.choices[0].message.content)
