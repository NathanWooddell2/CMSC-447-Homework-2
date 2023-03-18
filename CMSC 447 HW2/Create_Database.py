# Name : Nathan Wooddell
# ID : TC56612
# Project : CMSC 447 - Homework 2
# Description : This file is a short script used to create the SQL database defined in the
#   homework2.sql file. Running it again will likely drop the current database.

import sqlite3

# Defines our database object, and creates it if it doesn't already exist
database = sqlite3.connect("homework2.db")

# Read from the SQL file, and execute the script present within
with open('homework2.sql') as file:
    database.executescript(file.read())

# defines a cursor for the .sql file
cursor = database.cursor()

# All of the predefined people who need to be added to the database
cursor.execute("INSERT INTO gradebook (StudentName, StudentID, StudentScore) VALUES ('Steve Smith', 211, 80)")

cursor.execute("INSERT INTO gradebook (StudentName, StudentID, StudentScore) VALUES ('Jian Wong', 122, 92)")

cursor.execute("INSERT INTO gradebook (StudentName, StudentID, StudentScore) VALUES ('Chris Peterson', 213, 91)")

cursor.execute("INSERT INTO gradebook (StudentName, StudentID, StudentScore) VALUES ('Sai Patel', 524, 94)")

cursor.execute("INSERT INTO gradebook (StudentName, StudentID, StudentScore) VALUES ('Andrew Whitehead', 425, 99)")

cursor.execute("INSERT INTO gradebook (StudentName, StudentID, StudentScore) VALUES ('Lynn Roberts', 626, 90)")

cursor.execute("INSERT INTO gradebook (StudentName, StudentID, StudentScore) VALUES ('Robert Sanders', 287, 75)")

# Makes an initial commit 
database.commit()
database.close()