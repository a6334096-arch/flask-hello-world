from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route("/")
def home():
    # 取得台灣時間
    taiwan_time = datetime.now(
        ZoneInfo("Asia/Taipei")
    ).strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>我的 Flask 網站</title>

        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                font-family: Arial, "Microsoft JhengHei", sans-serif;
                background: linear-gradient(135deg, #eef6ff, #ffffff);
                color: #333;
            }}

            header {{
                background: #1565c0;
                color: white;
                padding: 22px;
                text-align: center;
            }}

            header h1 {{
                margin: 0;
            }}

            .container {{
                max-width: 900px;
                margin: 60px auto;
                padding: 20px;
            }}

            .card {{
                background: white;
                padding: 45px;
                border-radius: 18px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.12);
                text-align: center;
            }}

            .card h2 {{
                color: #1565c0;
                font-size: 32px;
            }}

            .time {{
                margin-top: 30px;
                padding: 20px;
                background: #f1f7ff;
                border-radius: 12px;
                font-size: 22px;
            }}

            .time strong {{
                color: #1565c0;
            }}

            .status {{
                display: inline-block;
                margin-top: 25px;
                padding: 10px 20px;
                background: #e8f5e9;
                color: #2e7d32;
                border-radius: 20px;
            }}

            footer {{
                margin-top: 50px;
                text-align: center;
                color: #777;
            }}
        </style>
    </head>

    <body>

        <header>
            <h1>我的第一個 Flask 網站</h1>
            <p>Python × Flask × GitHub × Render</p>
        </header>

        <div class="container">

            <div class="card">

                <h2>👋 Hello World!</h2>

                <p>
                    歡迎來到我的 Flask Web Application
                </p>

                <div class="time">
                    🇹🇼 台灣現在時間<br><br>
                    <strong>{taiwan_time}</strong>
                </div>

                <div class="status">
                    ● Flask Server 正常運作
                </div>

            </div>

            <footer>
                Flask Web Project
            </footer>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
