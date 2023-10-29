from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, String, Numeric
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql://postgres:kenkivuti254@localhost:5432/mackaysdb"
db = SQLAlchemy(app)

class Households(db.Model):
    __tablename__ = 'households'
    id = Column(Integer , primary_key = True)
    house_number = Column(Integer , nullable = False)
    no_of_rooms = Column(Integer, nullable = False)
    rent = Column(String)
    tenant = relationship("Tenant", back_populates="households")



class Tenant(db.Model):
    __tablename__ = 'tenant'
    id = Column(Integer, primary_key = True)
    house_id = Column(Integer , ForeignKey('households.id'))
    first_name= Column(String(255))
    last_name= Column(String(255))
    email_address = Column(String(255))
    contact= Column(String)
    payments = relationship("Payments" , back_populates="tenant")
    Households = relationship("Households" , back_populates= "tenant")



class Payments(db.Model):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key= True)
    tenant_id =Column(Integer , ForeignKey('tenant.id'), nullable= False)
    payment_method =Column(Integer)
    amount_paid = Column(Integer)



class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer , primary_key= True)
    email = Column(String(255))
    password = Column(String(255))


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:kenkivuti254@localhost:5432/mackaysdb"
# db = SQLAlchemy(app)

# class Households(db.Model):
#     __tablename__ = 'households'
#     id = db.Column(db.Integer, primary_key=True)
#     house_number = db.Column(db.Integer, nullable=False)
#     no_of_rooms = db.Column(db.Integer, nullable=False)
#     rent = db.Column(db.String)
#     tenants = db.relationship("Tenant", back_populates="household")

# class Tenant(db.Model):
#     __tablename__ = 'tenant'
#     id = db.Column(db.Integer, primary_key=True)
#     house_id = db.Column(db.Integer, db.ForeignKey('households.id'))
#     first_name = db.Column(db.String(255))
#     last_name = db.Column(db.String(255))
#     email_address = db.Column(db.String(255))
#     contact = db.Column(db.String)
#     payments = db.relationship("Payment", back_populates="tenant")
#     household = db.relationship("Households", back_populates="tenants")

# class Payment(db.Model):
#     __tablename__ = 'payments'
#     id = db.Column(db.Integer, primary_key=True)
#     tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=False)
#     payment_method = db.Column(db.String(255))  # Change to String
#     amount_paid = db.Column(db.Numeric)
#     Tenant = db.relationship("Tenant", back_populates="payments")

# class Users(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(255))
#     password = db.Column(db.String(255))