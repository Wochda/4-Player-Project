import re
from database import *
import datetime

def get_game_id():
    # search for game_id's
    list1 = []
    for line in data:
        try:
            a = re.search("[0-9]{6,10}", line).group(0)
            list1.append(int(a))
        except:
            pass
    return list1

def get_player_id():
    # search for player_id's
    list3 = []
    for line in data:
        list2 = []
        try:
            red_1 = re.search("Red \".*?\"", line).group(0)
            red_2 = re.search("\".*?\"", red_1).group(0)
            red_3 = re.sub("\"", "", red_2)
            list2.append(red_3)

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
    list1 = []
    list2 = []
    roundlist = []
    gamelist = []

    listcomplete = []
    for line in data:
        x = str(re.findall("\}.*?\{|\][0-9]*\. .*?\{|\} [0-9]*\. .*?\{", line))
        y = re.sub("([']|\])|,|{|}|\.\.|\[", ",", x)
        z = y.split(" ")
        for item in z:
            a = re.sub(",*| ","", item)
            if a == '':
                continue
            list1.append(a)
        list2.append(list1)
        list1 = []

    for game in list2:
        game.insert(len(game), "99.")
        for move in game:
            try:
                n = re.search("[0-9]*\.", move).group(0)
                if n == move:
                    if roundlist != []:
                        if len(roundlist) == 4:
                            gamelist.append(roundlist)
                        roundlist = []
                    continue
            except:
                roundlist.append(move)

        if gamelist != []:
            listcomplete.append(gamelist)
            gamelist = []

    return listcomplete

def get_piece_ids(moves):
    list5 = []
    q = 0
    for movelistgame in moves:
        Pawns1 = {"Pawn_1": "0", "Pawn_2": "0", "Pawn_3": "0", "Pawn_4": "0", "Pawn_5": "0",
                  "Pawn_6": "0", "Pawn_7": "0", "Pawn_8": "0"}
        Pawns2 = {"Pawn_1": "0", "Pawn_2": "0", "Pawn_3": "0", "Pawn_4": "0", "Pawn_5": "0",
                  "Pawn_6": "0", "Pawn_7": "0", "Pawn_8": "0"}
        Pawns3 = {"Pawn_1": "0", "Pawn_2": "0", "Pawn_3": "0", "Pawn_4": "0", "Pawn_5": "0",
                  "Pawn_6": "0", "Pawn_7": "0", "Pawn_8": "0"}
        Pawns4 = {"Pawn_1": "0", "Pawn_2": "0", "Pawn_3": "0", "Pawn_4": "0", "Pawn_5": "0",
                  "Pawn_6": "0", "Pawn_7": "0", "Pawn_8": "0"}
        for movelistround in movelistgame:
                l = 0
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

                    try:
                        r = re.search('O-O-O|O-O|^[A-Z]', move).group(0)
                    except:
                        r = ''
                    if r == '':
                        # beginning
                        p = re.search('([a-z][0-9]-|[a-z][0-9]x)|([a-z][0-9][0-9]-|[a-z][0-9][0-9]x)', move).group(0)
                        u = re.sub("-|x", "", p)

                        # ending
                        b = re.search('(-[a-z][0-9][0-9]|x[a-z][0-9][0-9])|(-[a-z][0-9]|x[a-z][0-9])|(-[A-Z][a-z][0-9][0-9]|x[A-Z][a-z][0-9][0-9])|(-[A-Z][a-z][0-9]|x[A-Z][a-z][0-9])', move).group(0)
                        o = re.sub("-|x|[A-Z]", "", b)

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
                    if len(list5) > q:
                        list5.pop()
    return list5

def get_time(moves):
    timelist = []
    timelistout = []
    temp = []

    for line in data:
        a = re.findall("\{ .*? \}", line)
        b = re.findall("[0-9]*:[0-9]*:[0-9]*\.[0-9]*", str(a))
        if b != []:
            timelist.append(b)

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

    for item in temp:
        timelistout.insert(len(timelistout), 0)
        for i in range(0, len(item)-1):
            time1 = item[i]
            time2 = item[i+1]

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

            dateTimeA = datetime.datetime.combine(datetime.date.today(), time2)
            dateTimeB = datetime.datetime.combine(datetime.date.today(), time1)
            dateTimeDifference = dateTimeA - dateTimeB
            dateTimeDifferenceInSecs = dateTimeDifference.total_seconds()
            timelistout.append(dateTimeDifferenceInSecs)
    return timelistout


with open('ffa.txt', 'r') as data:
    game_ids = get_game_id()
    data.close()
    print(len(game_ids), "gameids")

with open('ffa.txt', 'r') as data:
    player_ids = get_player_id()
    data.close()
    print(len(player_ids), "playerids")

with open('ffa.txt', 'r') as data:
    move_ids = get_move_ids()
    data.close()
    u = 0
    for movelistgame in move_ids:
        for movelistround in movelistgame:
                for move in movelistround:
                    u += 1
    print(u, "moves")

with open('ffa.txt', 'r') as data:
    pieces = get_piece_ids(move_ids)
    data.close()
    print(len(pieces), "pieces")

with open('ffa.txt', 'r') as data:
    time = get_time(move_ids)
    data.close()
    print(len(time), "time")

db = Database()
db.create_table()

z = 0
for i in range(0, len(game_ids)):
    try:
        for o in range(0, len(move_ids[i])):
               for x in range(0, len(move_ids[i][o])):
                    db.insert(game_ids[i], player_ids[i][x], move_ids[i][o][x], pieces[z], o+1, time[z])
                    #print(game_ids[i])
                    #print(player_ids[i][x])
                    #print(move_ids[i][o][x])
                    #print(o+1)
                    #print(pieces[z])
                    #print(time[z])
                    z += 1
    except:
        break
    #except:
     #   break
   # print("Game ", i, " done...")


db.commit()
db.close()