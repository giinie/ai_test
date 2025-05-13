from openai import OpenAI

# (1) OpenAI 클라이언트 생성
OPENAI_API_KEY = "API_Key_입력" 
client = OpenAI(api_key=OPENAI_API_KEY)

# (2) 음성 파일 경로 설정
mp3_file = "sample_meeting.mp3"

# (3) 파일 읽어오기
audio_content = open("sample_meeting.mp3", "rb")

# (4) API 요청 및 응답 처리
transcription = client.audio.transcriptions.create(
	model="whisper-1",
	file=audio_content,
	response_format="text",
)

# (5) 변환 결과 출력
print(transcription)