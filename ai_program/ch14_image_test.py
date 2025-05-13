from openai import OpenAI
import base64

# (1) OpenAI 클라이언트 생성
OPENAI_API_KEY = "API_Key_입력" 
client = OpenAI(api_key=OPENAI_API_KEY)

# (2) 이미지 인코딩 함수 정의
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# (3) 이미지 인코딩 함수 호출
base64_image = encode_image("sample_image.png")

# (4) 이미지 분석 함수 정의
def analyze_image(prompt, base64_image):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        # 이미지 분석 요청 프롬프트
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        # base64로 변환된 이미지 데이터
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64, {base64_image}"},
                    },
                ],
            }
        ],
    )
    return response.choices[0].message.content

# (5) 이미지 분석 함수의 프롬프트 작성
prompt = "이 사진이 뭔지 2줄로 요약해줘."

# (6) 이미지 분석 함수 호출 및 결과 출력
result = analyze_image(prompt, base64_image)
print(result)
