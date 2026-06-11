from flask import Flask, render_template, request

app = Flask(__name__)

def analyze_risk(temperature, humidity):
    if temperature > 30 and humidity > 80:
        return "Высокий риск порчи зерна", "Необходимо включить вентиляцию и снизить влажность."
    elif temperature > 25 or humidity > 70:
        return "Средний риск", "Рекомендуется усилить контроль температуры и влажности."
    else:
        return "Низкий риск", "Условия хранения стабильные."

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    recommendation = None

    if request.method == "POST":
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        result, recommendation = analyze_risk(temperature, humidity)

    return render_template("index.html", result=result, recommendation=recommendation)

if __name__ == "__main__":
    app.run(debug=True)
