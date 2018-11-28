from flask import Flask, render_template, request, jsonify
from desserts import dessert_list

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'whatever'

debug = DebugToolbarExtension(app)


@app.route("/")
def home():
    """Return home page with basic info"""

    return render_template("index.html")


@app.route("/desserts", methods=["GET", "POST"])
def show_desserts():
    """Display all desserts"""
    if request.method == "GET":
        return jsonify(dessert_list.serialize())
    else:
        dessert_list.add(
            name=request.json["name"],
            description=request.json["description"],
            calories=request.json["calories"])
        dessert = dessert_list.desserts[-1]
        return jsonify(dessert.serialize())