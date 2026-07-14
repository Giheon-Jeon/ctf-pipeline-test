FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# 런타임에 불필요한 빌드 도구 제거 (vendored 취약점 제거 + 공격 표면 감소)
RUN pip uninstall -y setuptools wheel

COPY app.py .

CMD ["python", "app.py"]