from flask import render_template, request, flash, redirect, url_for, session
from dbservices import *
from flask_login import LoginManager,  login_user, current_user, login_manager, login_required

login_manager = LoginManager(app)
login_manager.login_view = 'login'

with app.app_context():
    db.create_all()

app.secret_key = "Ma@ck#ays%ltd"


@app.route("/")
def mackays():
    return render_template("index.html")


@app.route("/households")
def houses():
    records = Houses.query.all()
    households = [house for house in records]
    return render_template("households.html", households=households)


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form["name"]
        contact = request.form["contact"]
        email = request.form["email"]
        password = request.form['password']
        role = request.form['role']

      #    check if email exist
        user = Users.query.filter_by(email=email).first()

        if user:
            flash("email already exist")
        else:
            new_user = Users(name=name, contact=contact,
                             email=email, password=password, role=role)
            db.session.add(new_user)
            db.session.commit()
            flash("Registered successfully")
            return redirect(url_for('login'))
    return render_template("register.html")


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Users.query.filter_by(email=email, password=password).first()

        if user:
            # store email in session
            session['email'] = user.email
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')


# @app.route('/admin_page')
# @login_required
# def admin_page():
#     if current_user.role != 'admin':
#         flash('Access denied. You do not have permission to view this page.', 'error')
#         return redirect(url_for('login'))
#     return render_template('index.html')


@app.route('/dashboard')
@login_required
def dashboard():
    print(current_user)
    flash(
        f'Welcome to your dashboard, {current_user.email}! Content: {current_user.dashboard_content}', 'info')
    return render_template('dashboard.html')


@app.route("/tenants", methods=['POST', 'GET'])
def tenants():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone']

        # add new tenants
        new_tenant = Tenants(full_name=full_name, email=email, phone=phone)

        # add the new tenant to the database

        db.session.add(new_tenant)

    #   commit changes to the database
        db.session.commit()
        flash("tenant added succesfully")

#    limit other users from accessing the page
#    if  Users.role != 'admin':
#         flash("Access denied  you do not have permission to view this page")
#         return redirect(url_for('login'))

    records = Tenants.query.all()
    tenants = [tnt for tnt in records]
    return render_template("tenants.html", tenants=tenants)


@app.route("/tenantshouses")
def tenantshouses():
    if request.method == 'POST':
        tenant_id = request.form['tenant_id']
        house_id = request.form['house_id']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        new_tenanthouse = TenantHouses(
            tenant_id=tenant_id, house_id=house_id, start_date=start_date, end_date=end_date)

        db.session.add(new_tenanthouse)

        db.session.commit()
        flash("success")

    records = TenantHouses.query.all()
    tenant_house = [th for th in records]

    return render_template("tenanthouse.html", tenant_house=tenant_house)


@app.route("/add-tenant")
def addtenant():
    form = Form()
    return redirect("/tenantshouses", form=form)


@app.route("/users", methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']

        # add new user
        new_user = Users(name=name, contact=contact, email=email)

        # add the new user to the database

        db.session.add(new_user)

    #   commit changes to the database
        db.session.commit()
        flash("user added succesfully")



    records = Users.query.all()
    users = [user for user in records]
    return render_template("user.html", users=users)


@app.route("/logout")
def logout():
    session.pop('email', None)
    flash('logout successfully')
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
