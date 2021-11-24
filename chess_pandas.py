# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:22:00 2021

@author: Patrick_Waldenhofer
"""

import sqlite3

# Defines the Database object
class Database():
    location = r"C:\Users\Patrick_Waldenhofer\Desktop\CHESS\chessdatabase"
    # Initializing database connection
    def __init__(self):
        self.connection = sqlite3.connect(Database.location)
        self.cursor = self.connection.cursor()

    # function to close connection
    def close(self):
        self.connection.close()

    # function to insert the playername and playerscore into the table "players"
    def insert(self, gameid, playerid, moveid, pieceid, roundid, timeid):
        self.cursor.execute(''' INSERT INTO chess(Game_id, Player_id, Move_id, Piece_id, Round_id, Time_id) VALUES(?,?,?,?,?,?) ''', (gameid, playerid, moveid, pieceid, roundid, timeid))

    # function to create table "players" if it doesn't exist, defines player_id, playername, playerscore
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS chess (
        Chess_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Game_id INTEGER NOT NULL,
        Player_id STRING NOT NULL,
        Move_id STRING NOT NULL,
        Piece_id STRING NOT NULL,
        Round_id INTEGER NOT NULL,
        Time_id STRING NOT NULL)''')

    # function to read the data out of the database, returns list with tuples
    def display(self):
        self.cursor.execute('''SELECT * from chess WHERE game_id = "626634"''')
        return self.cursor.fetchall()

    # function used to actually do the functions above if called afterwards
    def commit(self):
        self.connection.commit()
        
a = Database()
#print(a.display()[0])
cool = a.display()
#print(type(cool))

import pandas as pd
import itertools
import csv


with open("dataset", 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a rows to the csv file
    writer.writerow(["Chess_ID","Game_ID","Player_ID","Move","Piece","Round","Time"])
    for row in cool:
        writer.writerow(row)

dfnice_raw  = pd.read_csv("dataset")

print(dfnice_raw.head())

#remove Chess ID, its not useful for prediction
del dfnice_raw["Chess_ID"]

#Shuffle dataframe
dfnice_raw = dfnice_raw.sample(frac=1)

print(dfnice_raw.head())
#Checking for null values
print(dfnice_raw.isnull().sum())

#Get numerical values for categorical data
new_raw_data = pd.get_dummies(dfnice_raw, columns = ["Game_ID","Player_ID","Move","Piece"])
print(new_raw_data.head())
print(new_raw_data.columns)
