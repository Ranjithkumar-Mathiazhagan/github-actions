from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hello from Python Backend with postgresql!"

app.run(host="0.0.0.0", port=5001, debug=True)
