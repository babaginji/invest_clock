from flask import Flask, render_template

app = Flask(__name__)

TARGET_AGE = 84
ANNUAL_INTEREST = 0.07  # 7%


def calculate_future_value(age):
    """現在年齢ageの1秒=1円を84歳まで複利計算"""
    years_to_go = TARGET_AGE - age
    return 1 * (1 + ANNUAL_INTEREST) ** years_to_go


@app.route("/")
def index():
    default_age = 30
    fv_per_second = calculate_future_value(default_age)
    fv_per_hour = fv_per_second * 3600  # 1時間あたり
    return render_template(
        "clock.html", default_age=default_age, future_value=round(fv_per_hour, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
