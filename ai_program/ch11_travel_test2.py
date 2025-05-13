from openai import OpenAI

# (1) OpenAI 클라이언트 생성
openai_api_key = "API_Key_입력"
client = OpenAI(api_key=openai_api_key)

# (2) 이미지 생성 함수 정의
def generate_image_url(prompt: str):
	response = client.images.generate(
		model="dall-e-3",
		prompt=prompt,
	)
	return response.data[0].url

# (3) 프롬프트 작성
prompt = "멋진 이스탄불 저녁"

# (4) 이미지 생성 함수 호출 및 결과 출력
image_url = generate_image_url(prompt)
print(image_url)