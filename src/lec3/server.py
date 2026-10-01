from flask import Flask, render_template, request
import os

app = Flask(__name__)

names = [os.environ["FIRST_NAME_IN_LIST"]]


@app.route("/")
def hello_world():
    global names
    return render_template("index.html", names=names)


@app.route("/catch", methods=["POST"])
def catch():
    global names
    if request.form.get("name"):
        names.append(request.form.get("name"))
    elif request.form.get("delete"):
        names.remove(request.form.get("delete"))
    return render_template("index.html", names=names)