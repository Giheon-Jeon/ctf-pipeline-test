from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <h1>🌏 GCP 서버에서 돌아가는 컨테이너!</h1>
    <p>이제 전 세계 어디서나 접속할 수 있어.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)