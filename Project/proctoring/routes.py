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

@app.route('/gg',methods=['GET', 'POST'])
def gg():
    return render_template("gg.html")