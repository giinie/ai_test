import pymupdf # (1) pymupdf 패키지 불러오기

# (2) 텍스트 추출 함수 정의
def get_text_from_page(pdf_data, page_number):
	document = pymupdf.open(pdf_data) 		# PDF 파일 열기
	page = document[page_number-1] 	# 페이지 가져오기
	return page.get_text() 				# 텍스트 추출 후 반환

# (5) 이미지 변환 함수 정의
def convert_pdf_to_images(pdf_data):
	document = pymupdf.open(pdf_data)
	# (6) 이미지를 저장할 빈 리스트 생성
	images = []
	# (7) PDF 페이지를 순회하며 이미지로 변환
	for page_num in range(len(document)):
		page = document[page_num]
		pix = page.get_pixmap(dpi=150) 			# 이미지 생성
		img_path = f"page_{page_num+1}.png" 	# 이미지 저장 경로 설정
		pix.save(img_path) 			# 이미지 저장
		images.append(img_path) 	# 이미지 저장 경로 리스트에 추가
	return images 					# 이미지 저장 경로 리스트 반환

# (3) PDF 파일 경로와 페이지 번호 저장
pdf_data = "sample.pdf" # PDF 파일 경로 저장
page_number = 1 		# 페이지 번호 저장

# (4) 텍스트 추출 함수 호출 및 결과 출력
pdf_text = get_text_from_page(pdf_data, page_number)
print(pdf_text)
# (8) 이미지 변환 함수 호출
convert_pdf_to_images(pdf_data)