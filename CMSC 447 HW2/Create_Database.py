# Name : Nathan Wooddell
# ID : TC56612
# Project : CMSC 447 - Homework 2
# Description : This file is a short script used to create the SQL database defined in the
#   homework2.sql file. Running it again will likely drop the current database.

import sqlite3

database = sqlite3.connect("homework2.db")

with open('homework2.sql') as file:
    database.executescript(file.read())

    cursor = database.cursor()

    cursor.execute()