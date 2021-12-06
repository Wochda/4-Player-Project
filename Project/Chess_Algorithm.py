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

print(f"numer of rows in raw dataframe: {len(df_raw)}")

# random moves to test algorithm
print(random.sample(set(df_raw["Move_id"]),k=20))
# a single game to test algorithm
print(df_singlegame.head(20))

def Algorithm(move):

    # "Algorithm"
    feeds = set()
    feed = ""
    predictions = {}

    totalpoints = 0
    while feed != "EXIT":
        #self.reply = ""
        feed = move

        # iterate pandas df by rows
        for entry in df_raw.itertuples():

            if feed == entry[2]:
                feeds.add(feed)

                # check if player is already in dict
                if entry[1] not in predictions.keys():
                    predictions[entry[1]] = 1
                else:
                    pass
                # found move -> +1
                predictions[entry[1]] = predictions.get(entry[1]) + 1
                # sort dict descending
        predictions2 = dict(sorted(predictions.items(), key=lambda x: x[1], reverse=True))

        # get total amount of points
        # calculate percentage
        for key, value in predictions2.items():
            totalpoints += value

        for key, value in predictions2.items():
            predictions2[key] = round(((100 * value) / totalpoints) * 100, 2)

        return (sorted(predictions2.items(), key=operator.itemgetter(1), reverse=True)[:5])