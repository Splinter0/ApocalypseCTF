from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    print(request.headers)
    return render_template("index.html")

app.run(host="0.0.0.0", port=8000)