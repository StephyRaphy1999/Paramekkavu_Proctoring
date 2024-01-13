from flask import Flask, render_template, request, redirect,  flash, abort, url_for, session
from proctoring import app
from  proctoring import app
from proctoring.models import *
from flask_login import login_user, current_user, logout_user, login_required
from random import randint
import os
from PIL import Image
from datetime import datetime
from flask import jsonify
from flask import Flask, render_template, request, jsonify
import tkinter as tk
from tkinter import *
import cv2
import csv
import os
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
from datetime import datetime
import time




@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/about',methods=['GET', 'POST'])
def about():
    return render_template("about.html")

@app.route('/edittregister/<int:id>',methods=['GET', 'POST'])
def edittregister(id):
    a=Register.query.get_or_404(id)

    if request.method == 'POST':
        a.fname = request.form['fname']
        a.lname= request.form['lname']
        a.gender = request.form['gender']
        a.dob = request.form['dob']
        a.email = request.form['email']
        a.contact= request.form['contact']
        a.password = request.form['password']
        a.department = request.form['department']
        a.qualification = request.form['qualification']
        a.experience = request.form['experience']

        db.session.commit()
        return redirect('/view')

    return render_template("edittregister.html",a=a)

@app.route('/tdelete/<int:id>', methods = ['GET','POST'])
@login_required
def delete_teacher(id):
    delet = Register.query.get_or_404(id)

    try:
        db.session.delete(delet)
        db.session.commit()
        return redirect('/view')
    except:
        return 'There was a problem deleting that task'


@app.route('/view',methods=['GET', 'POST'])
def view():
    a =Register.query.filter_by(usertype="teacher").all()
    return render_template("view.html",a=a)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        email=request.form['email']
        password=request.form['password']


        admin =Register.query.filter_by(email=email, password=password,usertype= 'admin').first()
        teacher =Register.query.filter_by(email=email, password=password,usertype= 'teacher').first()
        student =Register.query.filter_by(email=email, password=password,usertype= 'student').first()
           
           
        if admin:
            login_user(admin)
            print(admin.usertype)
            session['ut']=admin.usertype
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/') 
        
        elif teacher:

            login_user(teacher)
            print(teacher.usertype)
            session['ut']=teacher.usertype
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/') 
        
        elif student:

            login_user(student)
            print(student.usertype)
            session['ut']=student.usertype
            # session['department']=student.department
            # session['sem']=student.semester
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/') 

        else:
            d="Invalid Username or Password!"
            return render_template("login")
    return render_template("login.html")

@app.route('/contact',methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

@app.route('/register',methods=['GET', 'POST'])
def add_register():

    if request.method == 'POST':


        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['gender']
        dob = request.form['dob']
        email = request.form['email']
        contact= request.form['contact']
        password = request.form['password']
        admission = request.form['admission']
        department = request.form['department']
        sem = request.form['sem']
        a = Register.query.filter_by(email=email).first()
        if a:
            return render_template("register.html",alert=True)
        else:

            my_data = Register(fname=fname,lname=lname,gender=gender,dob=dob,email=email,contact=contact,password=password,admission=admission,department=department,sem=sem,usertype="student")
            db.session.add(my_data) 
            db.session.commit()
            return redirect('/register')
    return render_template("register.html")



@app.route('/tregister',methods=['GET', 'POST'])
def add_tregister():

    if request.method == 'POST':


        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['gender']
        dob = request.form['dob']
        email = request.form['email']
        contact= request.form['contact']
        password = request.form['password']
        experience = request.form['experience']
        department = request.form['department']
        qualification = request.form['qualification']
        a = Register.query.filter_by(email=email).first()
        if a:
            return render_template("register.html",alert=True)
        else:

            my_data = Register(fname=fname,lname=lname,gender=gender,dob=dob,email=email,contact=contact,password=password,experience=experience,department=department,qualification=qualification,usertype="teacher")
            db.session.add(my_data) 
            db.session.commit()
            return redirect('/tregister')
    return render_template("tregister.html")


@app.route('/scheduleexam',methods=['GET', 'POST'])
def scheduleexam():

    if request.method == 'POST':
        subname = request.form['subname']
        time = request.form['time']
        duration = request.form['duration']
        date = request.form['date']
        dept = request.form['dept']
        sem = request.form['sem']


        my_data = Exam(subname=subname,time=time,duration=duration,date=date,dept=dept,sem=sem)
        db.session.add(my_data) 
        db.session.commit()
        return redirect('/scheduleexam')
    return render_template("scheduleexam.html")


@app.route('/examdetails',methods=['GET', 'POST'])
def examdetails():

    a =Exam.query.all()
    uid= current_user.id
    print("uid",uid)
    rid = Register.query.filter_by(id = uid).first()
    print("rid",rid.id)
    print("user_semester",rid.sem)
    print("user_department",rid.department)
    b =Exam.query.filter_by(sem=rid.sem,dept=rid.department).all()
    print (b)
    return render_template("examdetails.html",a=a,b=b)


@app.route('/editexam/<int:id>',methods=['GET', 'POST'])
def editexam(id):
    a=Exam.query.get_or_404(id)

    if request.method == 'POST':
        a.subname = request.form['subname']
        a.date = request.form['date']
        a.time = request.form['time']
        a.duration = request.form['duration']
        a.dept = request.form['dept']
        a.sem = request.form['sem']
        

        db.session.commit()
        return redirect('/examdetails')

    return render_template("editexam.html",a=a)

@app.route('/examdelete/<int:id>', methods = ['GET','POST'])
@login_required
def delete_exam(id):
    delet = Exam.query.get_or_404(id)

    try:
        db.session.delete(delet)
        db.session.commit()
        return redirect('/examdetails')
    except:
        return 'There was a problem deleting that task'












@app.route('/logout')
@login_required
def logout():
    print("Before logout code")
    print("----11----")
    try:
        print("----1----")
        logout_user()
        session.clear()  # Clear the session data
        print("Logout successful")
        return redirect('/')  # Redirect to the home page or another page after logout
        print("Before logout code")
    except Exception as e:
        print("------2--------")
        print("Logout failed with error:", str(e))
        return redirect('/')