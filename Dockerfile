# 베이스 이미지로 Python 3.9 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# virtualenv 설치
RUN pip install --no-cache-dir virtualenv

# 가상환경 생성
RUN virtualenv venv

# 가상환경 활성화 및 의존성 설치
COPY requirements.txt .
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY src/ /app/src/

# 가상환경을 활성화하여 스크립트를 실행하도록 CMD 명령 설정
CMD . venv/bin/activate && python src/main.py