@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        password = request.form['password']
        email = request.form['email']
        hashed_pass = generate_password_hash(password)
        # Email Validation
        user = Users.query.filter_by(email=email).first()
        if user:
            flash("Email is already in use")
        elif not password or not email:
            flash("Please fill all the inputs")
        else:
            new_user = Users(email=email,
                             password=hashed_pass)
            db.session.add(new_user)
            db.session.commit()
            flash("You have registered successfully!")
            return redirect(url_for("login"))

 return render_template("register.html")