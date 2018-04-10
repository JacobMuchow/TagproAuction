# -*- coding: utf-8 -*-


import json


## Edit these then run the script to generate the data you need
captains = [
    ("Tim Hortons", "Club Pinguin", "Red", 0, 0, []),
    ("TheBob18", "Knights of Cap-a-Lot", "Red", 0, 0, []),
    ("BallAnka", "Pi-Curious", "Red", 0, 0, []),
    ("Bubblez", "Trailer Park Balls", "Red", 0, 0, []),
    ("Ajax", "Ball or Nothing", "Blue", 0, 0, []),
    ("Catalyst", "Degrees of Freedom", "Blue", 0, 0, []),
    ("yiss", "St. Ball Saints", "Blue", 0, 0, []),
    ("#SelfySentax", "Stranger Pings", "Blue", 0, 0, []),
    ("PK SMURFBALL", "Weed the People", "Blue", 0, 0, []),
    ("Mufro", "TBD", "Blue", 0, 0, [])
]

managers = [
    ("NameLEss", "Master Boaters", "Red", 0, 0, [], "waterwheel"),
    ("protag", "qakboosters", "Red", 0, 0, [], "TagProfessor"),
    ("BALLDON'TLIE", "SMALL CAPS", "Red", 0, 0, [], "veezy"),
    ("GOOBR", "Jungle Jukes", "Red", 0, 0, [], "YUNG ZEFF"),
    ("MEX", "Big Gay Balls", "Blue", 0, 0, [], "RuBall"),
    ("Bright", "Bubble Balls", "Blue", 0, 0, [], "El Sacko")
]

starting_money = 100
keeper_money = 0
team_size = 6

nominations = [{"name" : "nextInOrder", "nextorder" : 0}]
team_names = []
keepers = []
teams = []
for index, data in enumerate(captains):
    captain, team_name, division, additional_money, additional_keeper_money, team_keepers = data
    nominations.append({"name" : captain, "rosterfull" : False, "order" : -1})
    team_names.append({"teamname":team_name, "division" : division, "money" : starting_money + additional_money, "keepermoney": keeper_money + additional_keeper_money, "captain":captain, "numrosterspots":team_size, "count":1, "order":(len(team_names) + 1)})
    teams.append({"name" : captain, "captain":True, "order" : 1, "cost" : 0, "division" : division, "teamname" : team_name })
    for x in range(2, team_size+1):
        teams.append({"name":"", "order" : x, "cost" : 0, "division" : division, "teamname" : team_name })
    keepers.append({"captain" : captain, "keepers":team_keepers})
 
for index, data in enumerate(managers):
    captain, team_name, division, additional_money, additional_keeper_money, team_keepers, first_player = data
    count = 0
    nominations.append({"name" : captain, "rosterfull" : False, "order" : -1})
    if first_player:
        teams.append({"name" : first_player, "cocaptain":True, "order" : 1, "cost" : 0, "division" : division, "teamname" : team_name })
        count = count + 1
    team_names.append({"teamname":team_name, "division" : division, "money" : starting_money + additional_money, "keepermoney": keeper_money + additional_keeper_money, "captain":captain, "numrosterspots":team_size, "count":count, "order":(len(team_names) + 1)})
    for x in range(count+1, team_size+1):
        teams.append({"name":"", "order" : x, "cost" : 0, "division" : division, "teamname" : team_name })
    keepers.append({"captain" : captain, "keepers":team_keepers})
 
division_names = set(c[2] for c in captains) | set(m[2] for m in managers)
divisions = []
for index, division in enumerate(division_names):
    divisions.append({"division": division, "order":index})
 
team_names.sort(key = lambda a: a["teamname"])
for index, division in enumerate(team_names):
    division["order"] = index
 
with open("./private/nominations.json", "wb") as f:
    f.write(json.dumps(nominations))
with open("./private/teamnames.json", "wb") as f:
    f.write(json.dumps(team_names))
with open("./private/divisions.json", "wb") as f:
    f.write(json.dumps(divisions))
with open("./private/teams.json", "wb") as f:
    f.write(json.dumps(teams))
with open("./private/keepers.json", "wb") as f:
    f.write(json.dumps(keepers))
