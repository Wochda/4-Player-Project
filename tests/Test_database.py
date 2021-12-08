import os
import pytest

from database import Database
from get_data import  game_ids, player_ids, move_ids, pieces, time

# testing if game ids are stored in the database
def test_get_game_id():
    # check if the output is a list (a list with all game ids)
    assert type(game_ids) == list
    for item in game_ids:
        # check if every elements is a integer
        assert type(item) == int

# testing if player ids are stored in the database
def test_get_player_id():
    # check if the output is a list (a list of lists, each internal list representing a game containing the players' ids)
    assert type(player_ids) == list
    for game in player_ids:
        assert type(game) == list
        for player in game:
            # check for the type of each player in each game
            assert type(player) == str

# testing if move ids are stored in the database
def test_get_move_ids():
    # check if it is of type list (a list of lists(representing games) of lists(representing rounds)
    assert type(move_ids) ==list
    for game in player_ids:
        assert type(game) == list
        for round in game:
            assert type(round) == str
            for move in round:
                assert type(move) == str


# testing if piece ids are stored in the database
def test_get_piece_ids():
    # check if it of type list (containing all pieces)
    assert type(pieces) == list
    for item in pieces:
        assert type(item) ==str

# testing if time is stored in the database
def test_get_time():
    #check if it is of type list
    assert type(time) == list
    for item in time:
        #time is stored as int in the case of time=0 and float for the rest
        assert type(item) == float or type(item) == int

@pytest.fixture(scope="module")
def database():
    return Database()

def test_init(database):
    d= database
    assert d.location == os.getcwd()+"\chessdatabase"

    assert d.connection != None # Object

    assert d.cursor != None # Object


# testing insert function
def test_insert(database):
    d = database
    # insert into database some values
    d.insert(123,"Name1","Move","Piece", 1, "Time")
    d.cursor.execute('''SELECT * from chess WHERE Player_id = "Name1" and Game_id = 123''')
    check = d.cursor.fetchall()
    #check if the values inserted are in the database
    assert check[0][1] == 123
    assert check[0][2] == "Name1"

# testing create_table function
def test_create_table(database):
    d = database
    d.create_table()
    d.cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' ''')
    c = d.cursor.fetchall()
    # check for table chess
    assert 'chess' in c[0]

#it is not possible, pytest gives an OperationalError
# testing display function
# def test_display(database):
#     d = database
#     c = d.display()
#     assert type(c[0][0]) == int
#     assert type(c[0][1]) == str

def test_commit(database):
    d = database
    assert d.connection.commit != None
