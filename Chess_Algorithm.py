# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:22:00 2021

@author: Patrick_Waldenhofer
"""

import sqlite3

DATABASELOCATION = r"C:\Users\Patrick_Waldenhofer\Desktop\CHESS\chessdatabase"

# Defines the Database object
class Database():
    
    # Initializing database connection
    def __init__(self):
        self.connection = sqlite3.connect(Database.DATABASELOCATION)
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
        self.cursor.execute('''SELECT * from chess''') #from chess WHERE game_id = "626634
        return self.cursor.fetchall()

    # function used to actually do the functions above if called afterwards
    def commit(self):
        self.connection.commit()
        


import pandas as pd
import time
import random
import operator

# connect to sql database
# measure executing time
startTime = time.time()

con = sqlite3.connect(DATABASELOCATION)
# Load the data into a DataFrame
# its better to load only the needed columns, this cuts execution time into half
df_raw = pd.read_sql_query("SELECT Player_id, Move_id from chess", con)
df_singlegame = pd.read_sql_query("SELECT Round_id, Player_id, Move_id from chess WHERE game_id = 626634", con)
# close connection
con.close()
executionTime = (time.time() - startTime)
print(f" Executiontime in seconds: {round(executionTime, 2)}")

print(f"numer of rows in raw dataframe: {len(df_raw)}")

# random moves to test algorithm
print(random.sample(set(df_raw["Move_id"]),k=20))
# a single game to test algorithm
print(df_singlegame.head(20))

# "Algorithm"

feeds = set()
feed = ""
predictions = {}

totalpoints = 0
while feed != "EXIT":
    
    feed = input("Pls enter a move: ")
    
    #iterate pandas df by rows
    for entry in df_raw.itertuples():

        if feed == entry[2]:
            feeds.add(feed)
            
            #check if player is already in dict
            if entry[1] not in predictions.keys():
                predictions[entry[1]] = 1
            else:
                pass
            # found move -> +1
            predictions[entry[1]] = predictions.get(entry[1]) + 1 
            
    # sort dict descending
    predictions2 = dict(sorted(predictions.items(),key= lambda x:x[1], reverse=True))
    
    # get total amount of points
    
    # calculate percentage 
    
    for key,value in predictions2.items():
        totalpoints += value
    
    for key,value in predictions2.items():
        predictions2[key] = round(((100*value)/totalpoints), 2)
        
        
        
    print(f"got {totalpoints} matches")
        
    
    if len(feeds) >= 5:
        #print(predictions2)
        print("first 5 entrys:")
        for k,v in sorted(predictions2.items(), key=operator.itemgetter(1), reverse=True)[:5]:
            print (k,v)
        print("Minimum:")
        print(min(predictions2.values()))
                
