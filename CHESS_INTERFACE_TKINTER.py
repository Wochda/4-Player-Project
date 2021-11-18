# ## Stand alone apps interface with tkinter based on Romans Prototype :)

####################################################################################################
# CHESS INTERFACE USING PYQT5                                                                      
####################################################################################################

import tkinter as tk
from tkinter.simpledialog import askstring
import sqlite3

root = tk.Tk()
a = ("Comic Sans MS", 15, "bold")
b = ("Comic Sans MS", 20, "bold")
root.geometry("600x400")
root.resizable(False, False)
root.iconbitmap("chess_piece_knight.ico")





class FirstPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Widgets()
        self.CREATETABLEFUNC()

    def Widgets(self):
        # pop up box asking for player usernames
        self.player_name = askstring('Name', 'Please enter your player name:')
        print(self.player_name)

        if self.player_name:  # if user clicks ok its saved to database, else, its not
            self.SAVETOTABLE()


    def CREATETABLEFUNC(self):
        self.Name = self.player_name

        # Connect to database;
        conn = sqlite3.connect('UserHistory.db')
        cursor = conn.cursor()

        # Create a table to store the user's player name;
        cursor.execute("CREATE TABLE IF NOT EXISTS History_table (player NULL)")


        # Close connection;
        conn.commit()
        conn.close()

    def SAVETOTABLE(self):

        # Connect to database;
        conn = sqlite3.connect('UserHistory.db')
        cursor = conn.cursor()

        # save user's player name entry to table;

        cursor.execute("INSERT INTO History_table(player) VALUES (:player_name)", {'player_name': self.player_name})

        # Close connection;
        conn.commit()
        conn.close()




FirstPage(root)



root.mainloop()
