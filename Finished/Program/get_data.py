import re
from database import *
import datetime

def get_game_id():
    # search for game_id's
    list1 = []
    # for each line in the txt file, get the game id's with regular expression and append it to list1,
    # return list 1
    for line in data:
        # Try an except Block if no game id pattern in line is available.
        try:
            a = re.search("[0-9]{6,10}", line).group(0)
            list1.append(int(a))
        except:
            pass
    return list1

def get_player_id():
    # search for player_id's
    # for each line in the txt file, get the player names with regular expression and append it to list2,
    # than append list 2 to list 3 so every list of names represents a game.
    # Try and except Block if line doesn't contain player name patterns.
    list3 = []
    for line in data:
        list2 = []
        try:
            red_1 = re.search("Red \".*?\"", line).group(0) # Pattern to enclose names
            red_2 = re.search("\".*?\"", red_1).group(0)    # Search for names
            red_3 = re.sub("\"", "", red_2)                 # Remove unnecassary "\"
            list2.append(red_3)                             # all colors work the same way

            blue_1 = re.search("Blue \".*?\"", line).group(0)
            blue_2 = re.search("\".*?\"", blue_1).group(0)
            blue_3 = re.sub("\"", "", blue_2)
            list2.append(blue_3)

            yellow_1 = re.search("Yellow \".*?\"", line).group(0)
            yellow_2 = re.search("\".*?\"", yellow_1).group(0)
            yellow_3 = re.sub("\"", "", yellow_2)
            list2.append(yellow_3)

            green_1 = re.search("Green \".*?\"", line).group(0)
            green_2 = re.search("\".*?\"", green_1).group(0)
            green_3 = re.sub("\"", "", green_2)
            list2.append(green_3)

            list3.append(list2)
        except:
            pass

    return list3

def get_move_ids():
    # Function to get player moves
    # Create a "roundlist" containing moves, represents moveset of each round
    # Create "gamelist" containing "roundlist", every list represents a game
    # Create "listcomplete" containing "gamelist" and "roundlist"
    # list1 and list2 serve as temp
    list1 = []
    list2 = []
    roundlist = []
    gamelist = []

    listcomplete = []

    for line in data:#
        # Get every move for each line with regular expression pattern
        x = str(re.findall("\}.*?\{|\][0-9]*\. .*?\{|\} [0-9]*\. .*?\{", line))

        # Remove unneccessary symbols and append to list1.
        # Append list1 to list2, list1 represents all moves of a game, list2 all games with all moves each
        y = re.sub("([']|\])|,|{|}|\.\.|\[", ",", x)
        z = y.split(" ")
        for item in z:
            a = re.sub(",*| ","", item)
            if a == '':
                continue
            list1.append(a)
        list2.append(list1)
        list1 = []

    # Going through every gamelist and get all round where all 4 players were present
    for game in list2:
        game.insert(len(game), "99.")   # inserting "99." to represent the end of a game

        # Going through every move each game, check if 4 moves are after round number, append them to "roundlist",
        # if "roundlist" is smaller than 4, continue
        for move in game:
            try:
                n = re.search("[0-9]*\.", move).group(0)    # Pattern to search for round numbers
                if n == move:                               # If a roundnumber is found and length of "roundlist"
                    if roundlist != []:                     # is 4, append to "gamelist", if not, continue
                        if len(roundlist) == 4:
                            gamelist.append(roundlist)
                        roundlist = []
                    continue
            except:
                roundlist.append(move)                      # If no round number is found but move instead,
                                                            # append move to "roundlist"

        if gamelist != []:                                  # Check each "gamelist" if game is present,
            listcomplete.append(gamelist)                   # append game to "listcomplete"
            gamelist = []

    return listcomplete

def get_piece_ids(moves):
    # Function to get piece for each move a player made
    list5 = []  # list5 represents list of all pieces found for each move
    q = 0        # q to check if list 5 has the right length at the end of third "movelistround" loop
    for movelistgame in moves:

        # Dictionary to numerate all Pawns for each Player, each dictionary represents a Player
        Pawns1 = {"Pawn_1": "0", "Pawn_2": "0", "Pawn_3": "0", "Pawn_4": "0", "Pawn_5": "0",
                  "Pawn_6": "0", "Pawn_7": "0", "Pawn_8": "0"}
        Pawns2 = {"Pawn_1": "0", "Pawn_2": "0", "Pawn_3": "0", "Pawn_4": "0", "Pawn_5": "0",
                  "Pawn_6": "0", "Pawn_7": "0", "Pawn_8": "0"}
        Pawns3 = {"Pawn_1": "0", "Pawn_2": "0", "Pawn_3": "0", "Pawn_4": "0", "Pawn_5": "0",
                  "Pawn_6": "0", "Pawn_7": "0", "Pawn_8": "0"}
        Pawns4 = {"Pawn_1": "0", "Pawn_2": "0", "Pawn_3": "0", "Pawn_4": "0", "Pawn_5": "0",
                  "Pawn_6": "0", "Pawn_7": "0", "Pawn_8": "0"}
        for movelistround in movelistgame:
                l = 0   # l represents the player's turn: if Red: l = 0,  Blue: l = 1 etc.

                # Going through every move made by a player
                # R, T, S, T# represent certain events in the game that aren't pieces,
                # therefore same event gets appended, l+1 to keep track of turn
                for move in movelistround:
                    q += 1
                    if move == "R":
                        list5.append("R")
                        l += 1
                        continue
                    if move == "T":
                        list5.append("T")
                        l += 1
                        continue
                    if move == "S":
                        list5.append("S")
                        l += 1
                        continue
                    if move == "T#":
                        list5.append("T#")
                        l += 1
                        continue

                    # try and except to check if current move is a pawn(no short or long castle or big char
                    # in the beginning)
                    try:
                        r = re.search('O-O-O|O-O|^[A-Z]', move).group(0)
                    except:
                        r = ''
                    if r == '':
                        # if current move is a pawn, get starting field with regular expression (p),
                        # remove unnecessary symbols (u)
                        # beginning
                        p = re.search('([a-z][0-9]-|[a-z][0-9]x)|([a-z][0-9][0-9]-|[a-z][0-9][0-9]x)', move).group(0)
                        u = re.sub("-|x", "", p)

                        # get ending field with regular expression (b), remove unnecessary symbols (o)
                        # ending
                        b = re.search('(-[a-z][0-9][0-9]|x[a-z][0-9][0-9])|(-[a-z][0-9]|x[a-z][0-9])|(-[A-Z][a-z][0-9][0-9]|x[A-Z][a-z][0-9][0-9])|(-[A-Z][a-z][0-9]|x[A-Z][a-z][0-9])', move).group(0)
                        o = re.sub("-|x|[A-Z]", "", b)

                        # If pawn starting field is one of the original positions when the game begins,
                        # check which field and which player,
                        # append the "ending" (last) field of the pawn to the dictionary
                        # append numerated pawn to list5 and continue
                        # Check is made for every single pawn and player, l+1 to keep track of turn number
                        if u == "d2" or u == "b11" or u == "k13" or u == "m4":
                            if l == 0 and Pawns1["Pawn_1"] == "0":
                                Pawns1["Pawn_1"] = o
                                list5.append('Pawn_1')
                                l += 1
                                continue
                            if l == 1 and Pawns2["Pawn_1"] == "0":
                                Pawns2["Pawn_1"] = o
                                list5.append('Pawn_1')
                                l += 1
                                continue
                            if l == 2 and Pawns3["Pawn_1"] == "0":
                                Pawns3["Pawn_1"] = o
                                list5.append('Pawn_1')
                                l += 1
                                continue
                            if l == 3 and Pawns4["Pawn_1"] == "0":
                                Pawns4["Pawn_1"] = o
                                list5.append('Pawn_1')
                                l += 1
                                continue
                        if u == "e2" or u == "b10" or u == "j13" or u == "m5":
                            if l == 0 and Pawns1["Pawn_2"] == "0":
                                Pawns1["Pawn_2"] = o
                                list5.append('Pawn_2')
                                l += 1
                                continue
                            if l == 1 and Pawns2["Pawn_2"] == "0":
                                Pawns2["Pawn_2"] = o
                                list5.append('Pawn_2')
                                l += 1
                                continue
                            if l == 2 and Pawns3["Pawn_2"] == "0":
                                Pawns3["Pawn_2"] = o
                                list5.append('Pawn_2')
                                l += 1
                                continue
                            if l == 3 and Pawns4["Pawn_2"] == "0":
                                Pawns4["Pawn_2"] = o
                                list5.append('Pawn_2')
                                l += 1
                                continue
                        if u == "f2" or u == "b9" or u == "i13" or u == "m6":
                            if l == 0 and Pawns1["Pawn_3"] == "0":
                                Pawns1["Pawn_3"] = o
                                list5.append('Pawn_3')
                                l += 1
                                continue
                            if l == 1 and Pawns2["Pawn_3"] == "0":
                                Pawns2["Pawn_3"] = o
                                list5.append('Pawn_3')
                                l += 1
                                continue
                            if l == 2 and Pawns3["Pawn_3"] == "0":
                                Pawns3["Pawn_3"] = o
                                list5.append('Pawn_3')
                                l += 1
                                continue
                            if l == 3 and Pawns4["Pawn_3"] == "0":
                                Pawns4["Pawn_3"] = o
                                list5.append('Pawn_3')
                                l += 1
                                continue
                        if u == "g2" or u == "b8" or u == "h13" or u == "m7":
                            if l == 0 and Pawns1["Pawn_4"] == "0":
                                Pawns1["Pawn_4"] = o
                                list5.append('Pawn_4')
                                l += 1
                                continue
                            if l == 1 and Pawns2["Pawn_4"] == "0":
                                Pawns2["Pawn_4"] = o
                                list5.append('Pawn_4')
                                l += 1
                                continue
                            if l == 2 and Pawns3["Pawn_4"] == "0":
                                Pawns3["Pawn_4"] = o
                                list5.append('Pawn_4')
                                l += 1
                                continue
                            if l == 3 and Pawns4["Pawn_4"] == "0":
                                Pawns4["Pawn_4"] = o
                                list5.append('Pawn_4')
                                l += 1
                                continue
                        if u == "h2" or u == "b7" or u == "g13" or u == "m8":
                            if l == 0 and Pawns1["Pawn_5"] == "0":
                                Pawns1["Pawn_5"] = o
                                list5.append('Pawn_5')
                                l += 1
                                continue
                            if l == 1 and Pawns2["Pawn_5"] == "0":
                                Pawns2["Pawn_5"] = o
                                list5.append('Pawn_5')
                                l += 1
                                continue
                            if l == 2 and Pawns3["Pawn_5"] == "0":
                                Pawns3["Pawn_5"] = o
                                list5.append('Pawn_5')
                                l += 1
                                continue
                            if l == 3 and Pawns4["Pawn_5"] == "0":
                                Pawns4["Pawn_5"] = o
                                list5.append('Pawn_5')
                                l += 1
                                continue
                        if u == "i2" or u == "b6" or u == "f13" or u == "m9":
                            if l == 0 and Pawns1["Pawn_6"] == "0":
                                Pawns1["Pawn_6"] = o
                                list5.append('Pawn_6')
                                l += 1
                                continue
                            if l == 1 and Pawns2["Pawn_6"] == "0":
                                Pawns2["Pawn_6"] = o
                                list5.append('Pawn_6')
                                l += 1
                                continue
                            if l == 2 and Pawns3["Pawn_6"] == "0":
                                Pawns3["Pawn_6"] = o
                                list5.append('Pawn_6')
                                l += 1
                                continue
                            if l == 3 and Pawns4["Pawn_6"] == "0":
                                Pawns4["Pawn_6"] = o
                                list5.append('Pawn_6')
                                l += 1
                                continue
                        if u == "j2" or u == "b5" or u == "e13" or u == "m10":
                            if l == 0 and Pawns1["Pawn_7"] == "0":
                                Pawns1["Pawn_7"] = o
                                list5.append('Pawn_7')
                                l += 1
                                continue
                            if l == 1 and Pawns2["Pawn_7"] == "0":
                                Pawns2["Pawn_7"] = o
                                list5.append('Pawn_7')
                                l += 1
                                continue
                            if l == 2 and Pawns3["Pawn_7"] == "0":
                                Pawns3["Pawn_7"] = o
                                list5.append('Pawn_7')
                                l += 1
                                continue
                            if l == 3 and Pawns4["Pawn_7"] == "0":
                                Pawns4["Pawn_7"] = o
                                list5.append('Pawn_7')
                                l += 1
                                continue
                        if u == "k2" or u == "b4" or u == "d13" or u == "m11":
                            if l == 0 and Pawns1["Pawn_8"] == "0":
                                Pawns1["Pawn_8"] = o
                                list5.append('Pawn_8')
                                l += 1
                                continue
                            if l == 1 and Pawns2["Pawn_8"] == "0":
                                Pawns2["Pawn_8"] = o
                                list5.append('Pawn_8')
                                l += 1
                                continue
                            if l == 2 and Pawns3["Pawn_8"] == "0":
                                Pawns3["Pawn_8"] = o
                                list5.append('Pawn_8')
                                l += 1
                                continue
                            if l == 3 and Pawns4["Pawn_8"] == "0":
                                Pawns4["Pawn_8"] = o
                                list5.append('Pawn_8')
                                l += 1
                                continue

                        # If pawn was not on a original starting position, check which turn, go through all keys
                        # in dictionary, if pawn starting field is the same as value in dictionary, replace value
                        # with new ending position, append key to list5
                        if l == 0:
                            for item in Pawns1:
                                if Pawns1[item] == u and Pawns1[item] != "0":
                                    Pawns1[item] = o
                                    list5.append(item)

                        if l == 1:
                            for item in Pawns2:
                                if Pawns2[item] == u and Pawns2[item] != "0":
                                    Pawns2[item] = o
                                    list5.append(item)

                        if l == 2:
                            for item in Pawns3:
                                if Pawns3[item] == u and Pawns3[item] != "0":
                                    Pawns3[item] = o
                                    list5.append(item)

                        if l == 3:
                            for item in Pawns4:
                                if Pawns4[item] == u and Pawns4[item] != "0":
                                    Pawns4[item] = o
                                    list5.append(item)

                    # If move is not a event or a pawn, check first char of move and append corresponding piece
                    # to list5, l+1 to keep track of turn, continue
                    if r == 'B':
                        list5.append('Bishop')
                        l += 1
                        continue
                    if r == 'N':
                        list5.append('Knight')
                        l += 1
                        continue
                    if r == 'Q':
                        list5.append('Queen')
                        l += 1
                        continue
                    if r == 'K':
                        list5.append('King')
                        l += 1
                        continue
                    if r == 'R':
                        list5.append('Rook')
                        l += 1
                        continue
                    if r == 'O-O':
                        list5.append('Short_Castle')
                        l += 1
                        continue
                    if r == 'O-O-O':
                        list5.append('Long_Castle')
                        l += 1
                        continue
                    l += 1

                    # check if more than 1 move was appended to list5, since a player can also move to
                    # starting position of another players pawn, remove unnecessary appended piece
                    if len(list5) > q:
                        list5.pop()
    return list5

# Function to get time for each move and calculate how long a move took.
def get_time(moves):
    timelist = []
    timelistout = []
    temp = []

    # Get time for each move with regular expression pattern, if nothing found continue
    for line in data:
        a = re.findall("\{ .*? \}", line)
        b = re.findall("[0-9]*:[0-9]*:[0-9]*\.[0-9]*", str(a))
        if b != []:
            timelist.append(b)

    # Get time for each move in the movelist from function: get_move_id
    # by checking and comparing length of both lists, times found get appended to temp2, temp2 append to temp
    # each list of temp represents a game
    # v for tacking each item, i for iteration in moves
    i = 0
    for item in timelist:
        temp2 = []
        v = 0
        for move in moves[i]:
            v += len(move)
        for timeitem in item:
            if len(temp2) >= v:
                break
            temp2.append(timeitem)
        i += 1
        temp.append(temp2)

    # Calculating how much time each move was needed using library datetime
    # Going through each game, insert 0 for each first move since no beginning
    # of the game time is given in txt file
    for item in temp:
        timelistout.insert(len(timelistout), 0)
        for i in range(0, len(item)-1):
            time1 = item[i]
            time2 = item[i+1]

            # transform times into a format that is usable with datetime using regular expression
            hours1 = int(re.findall("[0-9]*", time1)[0])
            minutes1 = int(re.findall("[0-9]*", time1)[2])
            seconds1 = int(re.findall("[0-9]*", time1)[4])
            milliseconds1 = int(re.findall("[0-9]*", time1)[6])
            hours2 = int(re.findall("[0-9]*", time2)[0])
            minutes2 = int(re.findall("[0-9]*", time2)[2])
            seconds2 = int(re.findall("[0-9]*", time2)[4])
            milliseconds2 = int(re.findall("[0-9]*", time2)[6])
            time1 = datetime.time(hours1, minutes1, seconds1, milliseconds1)
            time2 = datetime.time(hours2, minutes2, seconds2, milliseconds2)

            # Calculating time by substracting time from move before with the current move time
            # Append all time to a list (same length like moves)
            dateTimeA = datetime.datetime.combine(datetime.date.today(), time2)
            dateTimeB = datetime.datetime.combine(datetime.date.today(), time1)
            dateTimeDifference = dateTimeA - dateTimeB
            dateTimeDifferenceInSecs = dateTimeDifference.total_seconds()
            timelistout.append(dateTimeDifferenceInSecs)
    return timelistout

# open txt file, loop to switch between both files
for j in range(2):
    file = 'solo.txt'
    if j == 1:
        file = 'ffa.txt'

    # get data using the function defined above, print length of lists
    # after each function, move pointer to the beginning of txt file
    with open(file, 'r') as data:
        game_ids = get_game_id()
        print(len(game_ids), "gameids")
        data.seek(0)
        player_ids = get_player_id()
        print(len(player_ids), "playerids")
        data.seek(0)
        move_ids = get_move_ids()
        u = 0
        for movelistgame in move_ids:
            for movelistround in movelistgame:
                    for move in movelistround:
                        u += 1
        print(u, "moves")
        data.seek(0)
        pieces = get_piece_ids(move_ids)
        print(len(pieces), "pieces")
        data.seek(0)
        time = get_time(move_ids)
        data.close()
        print(len(time), "time")

    # Create database object and table in it only if not already created
    db = Database()
    db.create_table()

    # go through all lists and insert them into database
    z = 0
    for i in range(0, len(game_ids)):
        for o in range(0, len(move_ids[i])):
                for x in range(0, len(move_ids[i][o])):
                    db.insert(game_ids[i], player_ids[i][x], move_ids[i][o][x], pieces[z], o+1, time[z])
                    z += 1

    # commit to database and close connection
    db.commit()
    db.close()