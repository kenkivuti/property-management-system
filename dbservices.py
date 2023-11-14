from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql://postgres:kenkivuti254@localhost:5432/mackaysdb"
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer , primary_key = True)
    name= db.Column(db.String(255), nullable = False)
    phone = db.Column(db.String)
    email=db.Column(db.String(255),nullable = False)
    role=db.Column(db.String(255),nullable=False)


class Tenants(db.Model):
    __tablename__ = 'tenants'
    id = db.Column(db.Integer , primary_key = True)
    full_name = db.Column(db.String(255))
    email=db.Column(db.String(255))
    phone = db.Column(db.String)
    tenants= db.relationship("TenantHouses" , back_populates = "tenants")


class Houses(db.Model):
    __tablename__ ='houses'
    id = db.Column(db.Integer , primary_key = True)
    house_number = db.Column(db.Integer , nullable = False)
    no_of_rooms = db.Column(db.Integer , nullable = False)
    rent = db.Column(db.String)
    houses= db.relationship("TenantHouses" , back_populates = "houses")


class TenantHouses(db.Model):
    __tablename__ = 'tenant_houses'
    id = db.Column(db.Integer , primary_key = True)
    tenant_id = db.Column(db.Integer , db.ForeignKey('tenants.id'), nullable =False)
    house_id = db.Column(db.Integer , db.ForeignKey('houses.id'))
    start_date = db.Column(DateTime )
    end_date = db.Column(db.String)
    tenant_houses = db.relationship("TenantHouseBills" , back_populates = 'tenant_houses')


class TenantHouseBills(db.Model):
    __tablename__ = 'tenant_house_bills'
    id = db.Column(db.Integer , primary_key = True)
    tenant_house_id = db.Column(db.Integer, db.ForeignKey('tenant_houses.id'), nullable =False)
    billing_date = db.Column(db.String)
    due_date=db.Column(db.String)
    amount= db.Column(db.Numeric)
    payment_status = db.Column(db.String)
    payment_date=db.column(DateTime )


class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer ,primary_key = True)
    tenant_house_bill_id = db.Column(db.Integer , db.ForeignKey('tenant_house_bills.id'), nullable =False)
    payment_method= db.Column(db.String(255))
    amount_paid = db.Column(db.Numeric)
    tenant= db.relationship("TenantHouseBills",back_populates= "payments")





    

