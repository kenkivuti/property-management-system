from flask import render_template, request , flash 
from dbservices import *

with app.app_context():
    db.create_all()

app.secret_key = "Mackaysltd"


@app.route("/")
def mackays():
    return render_template("index.html")


@app.route("/households")
def households():
    records = Houses.query.all()
    households=[house for house in records]
    return render_template("households.html", households=households)



@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():

  return render_template("login.html")
    

if __name__== "__main__":
    app.run(debug=True)

    # if user:
        #     flash("Email already exist")
        # else:
        #     new_user = Users(email=email, password=hashed_pass)
        #     db.session.add(new_user)
        #     db.session.commit()
        #     flash("You have succesfully registered")
        #     return redirect(url_for('login'))