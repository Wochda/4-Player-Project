import sqlite3
import os

# Defines the Database object
class Database():
    location = os.getcwd()+"\chessdatabase"
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
        self.cursor.execute('''SELECT * from chess''')
        return self.cursor.fetchall()

    # function used to actually do the functions above if called afterwards
    def commit(self):
        self.connection.commit()