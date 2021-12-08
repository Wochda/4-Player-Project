from database import *
import pandas as pd
import time
import random
import operator

# connect to sql database
# measure executing time
startTime = time.time()
db = Database()

#con = sqlite3.connect(DATABASELOCATION)
# Load the data into a DataFrame
# its better to load only the needed columns, this cuts execution time into half
df_raw = pd.read_sql_query("SELECT Player_id, Move_id from chess", db.connection)
df_singlegame = pd.read_sql_query("SELECT Round_id, Player_id, Move_id from chess WHERE game_id = 626634", db.connection)
# close connection
db.close()
executionTime = (time.time() - startTime)
print(f" Executiontime in seconds: {round(executionTime, 2)}")

print(f"number of rows in raw dataframe: {len(df_raw)}")

# random moves to test algorithm
print(random.sample(set(df_raw["Move_id"]),k=20))
# a single game to test algorithm
print(df_singlegame.head(20))

def Algorithm(move):
    totalmoves = 0
    # "Algorithm"
    # feeds is the set of inputmoves
    feeds = set()
    feed = ""
    # predictions is a dict which stores Player name as a key and prediction percentage as value in the end
    predictions = {}
    
    # total matching moves of df_raw
    # while loop waiting for Player enters new move and updates the predictions
    while feed != "EXIT":
        
        feed = move

        # iterate pandas df by rows (df_raw is the total list of all moves played ever linked to player_name, so there are also moves multiple times
        # depending on how often a player plays
        for entry in df_raw.itertuples():
            # entry[2] == "Move_id"
            if feed == entry[2]:
                feeds.add(feed)

                # check if player is already in dict, entry[1] == Player_id
                # if not create new key
                if entry[1] not in predictions.keys():
                    predictions[entry[1]] = 1
                else:
                    pass
                # found move -> +1
                predictions[entry[1]] = predictions.get(entry[1]) + 1
        
        # sort dict descending
        predictions2 = dict(sorted(predictions.items(), key=lambda x: x[1], reverse=True))

        
        # calculate percentage
        # create sum of all moves in totalmoves
        for key, value in predictions2.items():
            totalmoves += value
        # Dreisatz calculation and shifting floating point by 2 with *100
        for key, value in predictions2.items():
            predictions2[key] = round(((100 * value) / totalmoves) * 100, 2)
            
        # return best predictions
        return (sorted(predictions2.items(), key=operator.itemgetter(1), reverse=True)[:4])