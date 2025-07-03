import os

from openai import OpenAI

# (1) OpenAI 클라이언트 생성
openai_api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)


# (2) 문서 요약 함수 정의
def summarize_text(prompt, text):
    # (3) 최종 프롬프트 완성
    # content = "다음 문서를 요약해주세요." + "\n" + text
    content = prompt + "\n" + text
    # (4) API 요청 및 응답
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": content}],
    )
    return response.choices[0].message.content


# (5) 샘플 문서 작성
sample_text = """
프롬프트 엔지니어링이란 무엇인가요?
프롬프트 엔지니어링은 생성형 AI로부터 원하는 결과를 얻기 위한 질문의 기술입니다. 생성형 AI는 인간을 모방하려고
시도하지만 고품질의 결과를 만들어내려면 자세한 지침이 필요합니다. 프롬프트 엔지니어링은 생성형 AI가 사용자와
더 의미있게 상호작용할 수 있도록 가장 적절한 형식, 구문, 단어, 기호를 사용하게 해줍니다. 사용자가 창의력을
발휘하면서도 여러 번의 시행착오를 거쳐 최적의 결과물을 얻을 수 있게 합니다.
프롬프트란 무엇인가요?
프롬프트는 특정 작업을 수행하도록 생성형 AI에 요청하는 자연어 텍스트입니다. 생성형 AI는 스토리, 대화, 동영상,
이미지, 음악과 같은 새로운 컨텐츠를 만들어내는 인공지능 솔루션으로, 방대한 양의 데이터로 사전 훈련된 심층 신경망을
사용하는 대규모 기계 학습(ML) 모델을 기반으로 합니다.
"""
# (6) 문서 요약 함수 호출 및 결과 출력
sample_prompt = "다음 문서를 요약해주세요."
result = summarize_text(sample_prompt, sample_text)
print(result)
