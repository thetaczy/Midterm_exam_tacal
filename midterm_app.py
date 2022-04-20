from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request

midtermapp = Flask(__name__)

@midtermapp.route("/", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@midtermapp.route("/reg")
def register():
    return render_template("registration.html")

if __name__ == "__main__":
    midtermapp.run(host="0.0.0.0", port = 5000, debug = True)
