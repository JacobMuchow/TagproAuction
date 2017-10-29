# -*- coding: utf-8 -*-


import json


## Edit these then run the script to generate the data you need
captains = [
    ("intercest", "Boostin Dynamo", "Northeast", 0, 0, ["Stann", "Gasol", "waterwheel", "Wavey", "ZenWhisper"]),
    ("protag", "Ghostboosters", "Northeast", 0, 0, []),
    ("Gem", "Someballian Pirates", "Northeast", 5, 0, []),
    # Lowej manager

    ("C Bivvey", "Whitecaps", "East", 0, 0, []),
    ("MEX", "A Blockwork Orange", "East", 5, 0, []),
    # Tantrew manager
    ("aardvark", "21 Juke Street", "East", 0, 0, []),

    # Ron Hextball manager
    ("eee", "The RePublicans", "Southeast", 15, 0, []),
    # JDoeMonopoly manager
    ("dodsfall", "A Developmental Lad", "Southeast", 0, 0, []),

    ("Bamboozler", "877CAPSNOW", "West", 5, 0, []),
    ("Warriors", "Centra of Attention", "West", 0, 0, []),
    ("yank", "Tears", "West", 0, 0, ["BigBird", "Belle", "Curry", "glide", "Hawaii", "WhatNotToDo"]),
    # fender manager
]

managers = [
    ("Lowej", "London WASDs", "Northeast", 0, 0, [], "Arbybear"),
    ("Tantrew", "Red Hot Chili Poppers", "East", 0, 0, ["Eashy", "Frozen", "danisk"], "Destar"),
    ("Ron Hextball", "TC Jukes", "Southeast", 15, 0, [], "Ty"),
    ("JDoeMonopoly", "Pequeños Pandas", "Southeast", 15, 0, [], "Veezy"),
    ("fender", "Rollin' Golden Boulders", "West", 0, 0, [], "Iblis")
]

starting_money = 100
keeper_money = 10
team_size = 5

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
