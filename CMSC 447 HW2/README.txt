Name : Nathan Wooddell
ID : TC56612
Proj : CMSC 447 Homework 2

Description : Create a CRUD application using HTML, CSS, FLASK, REACT JS.

Homepage.html
    Originally I had planned to keep all of my website code contained in this file.
    This is the part of my code which works the best, and currently serves as a homepage
    for all of the required database functions.
    These functions have been implemented as input boxes, taking the student name and
    performing an operation based on the button pressed. These are sorted into three
    neat columns.

Create_Database.py
    This file contains the code used to create my sqlite database. I used sqlite3 because
    it was included with python3.

homework2.py
    This file contains the majority of my flask functions, as well as a couple helper
    functions to help the flask functions achieve their goal.

homework2.sql
    This is the definition of my SQLite3 database, it was used in tandem with Create_Database
    to create the actual database which is called homework2.db. 

homework2.db
    This is the database file, which should be accessible by the flask code. It contains a single table
    called "gradebook" and contains three fields : StudentName, StudentID, StudentScore.