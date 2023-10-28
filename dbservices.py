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
    tenant = relationship("tenant", back_populates="households")



class Tenant(db.Model):
    __tablename__ = 'tenant'
    id = Column(Integer, primary_key = True)
    house_id = Column(Integer , ForeignKey('household.id'))
    first_name= Column(String(255))
    last_name= Column(String(255))
    email_address = Column(String(255))
    contact= Column(String)
    payments = relationship("payments" , back_populates="tenant")



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