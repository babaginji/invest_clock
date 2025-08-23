from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# 設定
TARGET_AGE = 84
ANNUAL_INTEREST = 0.07  # 7%


def calculate_future_value(age):
    """
    現在年齢ageの1秒=1円を84歳まで複利計算
    """
    years_to_go = TARGET_AGE - age
    principal_per_second = 1  # 1秒1円
    fv = principal_per_second * (1 + ANNUAL_INTEREST) ** years_to_go
    return fv


def current_time_value(age):
    """
    現在価値の1時間あたりの値段を計算
    """
    fv = calculate_future_value(age)
    return fv / (365.25 * 24)  # 1時間あたり


@app.route("/")
def index():
    # 年齢はクライアント側(localStorage)で管理するのでサーバーでは固定値不要
    default_age = 30  # 初回表示用
    time_value = current_time_value(default_age)
    return render_template(
        "clock.html", time_value=round(time_value, 2), default_age=default_age
    )


if __name__ == "__main__":
    app.run(debug=True)
