from flask import Flask, render_template, request

app = Flask(__name__)

names = []


@app.route("/")
def hello_world():
    global names
    return render_template("index.html", names=names)


@app.route("/catch", methods=["POST"])
def catch():
    global names
    if request.form.get("name"):
        names.append(request.form.get("name"))
    return render_template("index.html", names=names)