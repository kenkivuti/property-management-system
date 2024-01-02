from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from flask_login import UserMixin , LoginManager
from enum import Enum
from wtforms import SelectField
from flask_wtf import FlaskForm


app = Flask(__name__)
# login_manager = LoginManager(app)
app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql://postgres:kenkivuti254@localhost:5432/mackaysdb"
db = SQLAlchemy(app)


class UserRole(Enum):
    USER = 'user'
    ADMIN = 'admin'



class Form(FlaskForm):
    house=SelectField('house_id',choices=[])
    tenant=SelectField('tenant_id',choices=[])
    

class Users( UserMixin , db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer , primary_key = True)
    name= db.Column(db.String(255), nullable = False)
    contact = db.Column(db.String)
    email=db.Column(db.String(255),nullable = False)
    password=db.Column(db.String(255),nullable=False)
    role=db.Column(db.String(255), nullable=False , default="tenant")
    dashboard_content = db.Column(db.String(255), default="Default Dashboard Content")



class Tenants(db.Model):
    __tablename__ = 'tenants'
    id = db.Column(db.Integer , primary_key = True)
    full_name = db.Column(db.String(255))
    email=db.Column(db.String(255))
    phone = db.Column(db.String)
    tenanthouses= db.relationship("TenantHouses" , back_populates = "tenant")


class Houses(db.Model):
    __tablename__ = 'houses'
    id = db.Column(db.Integer , primary_key = True)
    house_number = db.Column(db.Integer , nullable = False)
    no_of_rooms = db.Column(db.Integer , nullable = False)
    rent = db.Column(db.String)
    tenanthouse= db.relationship("TenantHouses" , back_populates = "house")


class TenantHouses(db.Model):
    __tablename__ = 'tenant_houses'
    id = db.Column(db.Integer , primary_key = True)
    tenant_id = db.Column(db.Integer , db.ForeignKey('tenants.id'))
    house_id = db.Column(db.Integer , db.ForeignKey('houses.id'))
    start_date = db.Column(DateTime )
    end_date = db.Column(db.String)
    tenant = db.relationship("Tenants" , back_populates = "tenanthouses")
    house=db.relationship("Houses" , back_populates ="tenanthouse")
    tenant_house=db.relationship("Tenanthousebills" , back_populates="tenant_houses")

class Tenanthousebills(db.Model):
    __tablename__ = 'tenant_house_bills'
    id = db.Column(db.Integer , primary_key = True)
    tenant_house_id = db.Column(db.Integer, db.ForeignKey('tenant_houses.id'), nullable =False)
    billing_date = db.Column(db.String)
    due_date=db.Column(db.String)
    amount= db.Column(db.Numeric)
    payment_status = db.Column(db.String)
    tenant_houses = db.relationship("TenantHouses" , back_populates = "tenant_house")
    payment_date=db.Column(DateTime )
    payments = db.relationship("Payment" , back_populates = "tenantbill")


class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer ,primary_key = True)
    tenant_house_bill_id = db.Column(db.Integer , db.ForeignKey('tenant_house_bills.id'), nullable =False)
    payment_method= db.Column(db.String(255))
    amount_paid = db.Column(db.Numeric)
    tenantbill= db.relationship("Tenanthousebills",back_populates= "payments")





    

