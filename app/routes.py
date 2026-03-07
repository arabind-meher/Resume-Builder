from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return redirect(url_for("main.home"))

@main.route("/home")
def home():
    return render_template("home.html")

@main.route("/editor")
def editor():
    return render_template("editor.html")

@main.route("/history")
def history():
    return render_template("history.html")