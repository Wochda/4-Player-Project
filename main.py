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
    list3 = []

    for line in data:
        x = str(re.findall("\}.*?\{|\][0-9]*\. .*?\{|\} [0-9]*\. .*?\{", line))
        y = re.sub("([']|\])|,|{|}|\.\.|\[", ",", x)
        z = y.split(" ")
        for item in z:
            a = re.sub(",*| ","", item)
            if a == '':
                continue
            list1.append(a)
        list3.append(list1)
        list1 = []

    list2 = []
    list4 = []
    list5 = []

    for itemlist in list3:
        for i in range(0, len(itemlist)):
            try:
                re.findall("[0-9]*\.", itemlist[i])[0]
                continue
            except:
                list2.append(itemlist[i])
                try:
                    re.findall("[0-9]*\.", itemlist[i+1])[0]
                    list4.append(list2)
                    list2 = []
                except:
                    try:
                        itemlist[i+1]
                    except:
                        list4.append(list2)
        if list4 != []:
            list5.append(list4)
        list4 = []
    return list5

def get_piece_ids(moves):
    list5 = []
    for movelistgame in moves:
        for movelistround in movelistgame:
            for move in movelistround:
                if move == "R":
                    list5.append("R")
                    continue
                if move == "T":
                    list5.append("T")
                    continue
                if move == "S":
                    list5.append("S")
                    continue

                try:
                    r = re.search('O-O-O|O-O|^[A-Z]', move).group(0)
                except:
                    r = ''
                if r == '':
                    list5.append('Pawn')
                if r == 'B':
                    list5.append('Bishop')
                if r == 'N':
                    list5.append('Knight')
                if r == 'Q':
                    list5.append('Queen')
                if r == 'K':
                    list5.append('King')
                if r == 'R':
                    list5.append('Rook')
                if r == 'O-O':
                    list5.append('Short_Castle')
                if r == 'O-O-O':
                    list5.append('Long_Castle')
    return list5

def get_time():
    timelist = []
    timelistout = []
    f = 0
    for line in data:
        a = re.findall("\{ .*? \}", line)
        b = re.findall("[0-9]*:[0-9]*:[0-9]*\.[0-9]*", str(a))
        if b != []:
            timelist.append(b)

    for item in timelist:
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
        timelistout.insert(0, 0)
    return timelistout


with open('solo.txt', 'r') as data:
    game_ids = get_game_id()
    data.close()

with open('solo.txt', 'r') as data:
    player_ids = get_player_id()
    data.close()

with open('solo.txt', 'r') as data:
    move_ids = get_move_ids()
    data.close()

with open('solo.txt', 'r') as data:
    pieces = get_piece_ids(move_ids)
    data.close()

with open('solo.txt', 'r') as data:
    time = get_time()
    data.close()

db = Database()
db.create_table()
z = 0
for i in range(0, len(game_ids)):
    p = 0
    for o in range(0, len(move_ids[i])):
        g = 0
        while g < len(move_ids[i][o]):
            if len(move_ids[i][o]) < 4:
                p += 1
                z += 1
                g += 1
                continue
            if len(move_ids[i][o]) > 4:
                move_ids[i][o].remove(move_ids[i][o][0])
                if g > 0:
                    g -= 1
                continue
            if p > 3:
                p = 0
            db.insert(game_ids[i], player_ids[i][p], move_ids[i][o][g], pieces[z], o+1, time[z])
            db.commit()
            #print(game_ids[i], player_ids[i][p], move_ids[i][o][g], pieces[z], o+1, time[z])
            #print(game_ids[i])
            #print(player_ids[i][p])
            #print(move_ids[i][o][g])
            #print(pieces[z])
            #print(o+1)
            #print(time[z])
            #print(pieces[r])
            #print(o + 1)
            #print(time[g])
            p += 1
            z += 1
            g += 1