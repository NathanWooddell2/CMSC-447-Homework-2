# Name : Nathan Wooddell
# ID : TC56612
# Project : CMSC 447 - Homework 2
# Description : This is the flask integration between my website (as defined in the Homepage.html file) and the 

# I chose to use sqlite3, and flask as sqlite3 was included in python after Python(2.5).
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

backend = Flask(__name__)


# Establishes a conncetion to the database created by the Create_Database.py file
def resolve_db():
    database = sqlite3.connect('homework2.db')
    database.row_factory = sqlite3.Row
    return database

# This displays all students in the system
@backend.route('/')
def display_all_students():
    database = resolve_db()
    gradebook = database.execute("Select * from gradbook").fetchall()
    database.close()
    return render_template('Homepage.html', gradebook=gradebook)

# A Function to display information on a student based on name
@backend.route('/get_student_from_db/', methods = ["GET", "POST"])
def get_student_from_db():
    if request.method == 'POST':
        StudentName = request.form["Ret_StudentName"]

    # Handle an empty StudentName form
    if not StudentName:
        flash("Please Enter a Student Name!")

    else:
        database = resolve_db()
        database.execute("SELECT * FROM gradebook WHERE StudentName = ?",
                        (StudentName)).fetchone()


# A function to delete a selected student based on a provided ID
@backend.route('/remove_student_from_db/', methods = ["GET", "POST"])
def remove_student_from_db():
    
    if request.method == 'POST':
        StudentName = request.form["Del_StudentName"]

    # Handle an empty StudentName form
    if not StudentName:
        flash("Please Enter a Student Name!")
    
    # Executes the delete command based on the StudentName argument
    else:
        database = resolve_db()
        database.execute("DELETE FROM gradebook WHERE StudentName=?",
                        (StudentName)).fetchone()
        database.commit()
        database.close()


# A funtion to add a student to the database, must provide all information
@backend.route('/add_student_to_db/', methods = ["GET", "POST"]) 
def add_student_to_db():
    if request.method == 'POST':
        StudentName = request.form["Add_StudentName"]
        StudentID = request.form["Add_StudentID"]
        StudentScore = request.form["Add_StudentScore"]
    
    # This is meant to handle an empty value
    if not StudentName:
        flash("Please Enter a Student Name!")
    elif not StudentID:
        flash("Please Enter a Student ID!")
    elif not StudentScore:
        flash("Please Enter a Student Score!")

    # This portion of the code is the ideal case for adding a student
    else:
        database = resolve_db()
        database.execute("INSERT INTO gradebook (StudentName, StudentID, StudentScore)",
                        (StudentName, StudentID, StudentScore))
        database.commit()
        database.close()

    return render_template('Homepage.html')