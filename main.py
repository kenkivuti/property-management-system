from flask import render_template, request , flash , redirect , url_for 
from dbservices import *
from flask_login import LoginManager,  login_user, current_user ,login_manager,login_required
login_manager = LoginManager(app)

with app.app_context():
    db.create_all()

app.secret_key = "Mackaysltd"


@app.route("/")
def mackays():
    return render_template("index.html")


@app.route("/households")
def houses():
    records = Houses.query.all()
    households=[house for house in records]
    return render_template("households.html", households=households)



@app.route("/register" ,methods=['POST', 'GET'])
def register():
    if request.method=='POST':
       name=request.form["name"]
       contact=request.form["contact"]
       email=request.form["email"]
       password=request.form['password']

     #    check if email exist
       user=Users.query.filter_by(email=email).first()

       if user:
         flash("email already exist")
       else:
        new_user=Users(name=name ,contact=contact, email=email , password=password)
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
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    flash(f'Welcome to the dashboard, {current_user.email}! Content: {current_user.dashboard_content}', 'info')
    return render_template('dashboard.html')


@app.route("/tenants" , methods=['POST' , 'GET'])
def tenant():
   if request.method == 'POST' :
      full_name=request.form['full_name']
      email=request.form['email']
      phone=request.form['phone']

      # add new tenants
      new_tenant=Tenants(full_name=full_name,email=email,phone=phone)
   
      # add the new tenant to the database

      db.session.add(new_tenant)

    #   commit changes to the database
      db.session.commit()
      flash("tenant added succesfully")
      
   
   records = Tenants.query.all()
   tenants = [tnt for tnt in records]
   return render_template("tenants.html", tenants=tenants)
  

  
   
   



if __name__== "__main__":
 app.run(debug=True)  
    

  