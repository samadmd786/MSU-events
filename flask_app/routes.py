# Author: Prof. MM Ghassemi <ghassem3@msu.edu>
from flask import current_app as app
from flask import render_template, redirect, request
from .utils.database.database  import database
from werkzeug.datastructures import ImmutableMultiDict
from pprint import pprint
import json
import random
db = database()

@app.route('/')
def root():
	return redirect('/home')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/home.html')
def home1():
	return render_template('home.html')



@app.route('/clubs.html')
def club():
	club_data = db.getData("clubs")
	print(type(club_data))
	return render_template('clubs.html',data=club_data)

@app.route('/professional.html')
def professional():
	pro_data = db.getData("professional")
	return render_template('professional.html', data= pro_data)

@app.route('/community.html')
def community():
	com_data = db.getData("community")
	return render_template('community.html',data= com_data)

@app.route('/entertainment.html')
def entertainment():
	enter_data =db.getData("entertainment")
	return render_template('entertainment.html',data = enter_data)


