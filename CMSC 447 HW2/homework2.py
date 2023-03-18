# Name : Nathan Wooddell
# ID : TC56612
# Project : CMSC 447 - Homework 2
# Description : This is the flask integration between my website (as defined in the Homepage.html file) and the 

# I chose to use sqlite3, and flask as sqlite3 was included in python after Python(2.5).
from flask import Flask, render_template 
import sqlite3

backend = Flask(__name__)

# Establishes a conncetion to the database created by the Create_Database.py file
def resolve_db():
    database = sqlite3.connect('homework2.db')
    database.row_factory = sqlite3.Row
    return database

# A Function to display information on a student based on name
@backend.route('/')
def get_student_from_db():
    database = resolve_db()
    # currently this just returns everything from the gradebook -> needs work
    gradebook = database.execute('SELECT * FROM gradebook').fetchall() # GIVE THIS A BETTER NAME
    database.close()
    return render_template('homepage.html', gradebook=gradebook)

# A function to delete a selected student based on a provided ID
@backend.route('/')
def remove_student_from_db():
    print("Placeholder")

# A funtion to add a student to the database, must provide all information
@backend.route('/')
def add_student_to_db():
    print("Placeholder")