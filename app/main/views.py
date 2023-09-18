from flask import render_template, request, jsonify
from . import bp

@bp.route("/")
@bp.route("/home")
def index():
    return render_template("index.html")

@bp.route("/form")
def form():
    return render_template("form.html")

@bp.route("/form_post", methods=["POST"])
def form_post():
    data = request.get_json()
    print(data)
    return 200