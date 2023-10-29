from flask import render_template,redirect,url_for,session
from dbservices import *

app.secret_key = "Mackaysltd"


@app.route("/")
def mackays():
    return render_template("index.html")


@app.route("/households")
def households():
    records = Households.query.all()
    households=[house for house in records]
    return render_template("households.html", households=households)

if __name__== "__main__":
    app.run(debug=True)