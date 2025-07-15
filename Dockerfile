# 1. 베이스 이미지 선택 (Python 3.10 이상 권장)
FROM python:3.10-slim

# 2. 작업 디렉토리 생성 및 이동
WORKDIR /app

# 3. 시스템 패키지 설치 (tesseract-ocr 등)
RUN sudo apt-get update && \
    sudo apt-get install -y tesseract-ocr libglib2.0-0 libsm6 libxext6 libxrender-dev && \
    sudo rm -rf /var/lib/apt/lists/*

# 4. 프로젝트 파일 복사
COPY . .

# 5. 파이썬 패키지 설치
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. 포트 오픈
# EXPOSE 8080

# 7. 컨테이너 시작 시 실행할 명령
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

# Render가 제공하는 PORT 환경변수를 사용하도록 수정
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]