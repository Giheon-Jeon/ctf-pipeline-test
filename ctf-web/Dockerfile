FROM python:3.11-slim

WORKDIR /app

# 베이스 이미지의 취약 패키지 업그레이드
RUN pip install --upgrade "jaraco.context>=6.1.0" "wheel>=0.46.2"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]