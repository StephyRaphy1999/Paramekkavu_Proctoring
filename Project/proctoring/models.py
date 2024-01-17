from  proctoring import app
from proctoring import db,app
from proctoring import db,app,login_manager
from flask_login import UserMixin

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship 
# from flask_table import Table, Col, LinkCol
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(id):
    return Register.query.get(int(id))



class Register(db.Model, UserMixin):
    
    id=db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    dob = db.Column(db.String(80))
    email = db.Column(db.String(80))
    contact = db.Column(db.String(80))
    password = db.Column(db.String(80))
    admission = db.Column(db.String(80))
    department = db.Column(db.String(80))
    sem = db.Column(db.String(80))
    usertype = db.Column(db.String(80))
    qualification = db.Column(db.String(80))
    experience = db.Column(db.String(80))
    status = db.Column(db.String(80),default='NULL')




class Exam(db.Model, UserMixin):
    
    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('register.id'))
    user = relationship('Register', foreign_keys=[user_id])
    subname = db.Column(db.String(80))
    date = db.Column(db.String(80))
    time = db.Column(db.String(80))
    duration = db.Column(db.String(80))
    sem = db.Column(db.String(80))
    dept = db.Column(db.String(80))
  
    



class Examregister(db.Model, UserMixin):
    
    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('register.id'))
    Exam_id = db.Column(db.Integer, ForeignKey('exam.id'))