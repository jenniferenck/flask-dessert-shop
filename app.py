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


@app.route("/desserts")
def show_desserts():
    """Display all desserts"""

    return jsonify(dessert_list.serialize())
