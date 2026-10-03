from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    # 啟動本機開發伺服器，開啟 debug 模式便於除錯與即時更新
    app.run(host='127.0.0.1', port=5000, debug=True)
