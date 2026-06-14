from flask import Flask, render_template, request

app = Flask(**name**)

@app.route("/", methods=["GET", "POST"])
def index():
return render_template("index.html")

if **name** == "**main**":
app.run(debug=True)

