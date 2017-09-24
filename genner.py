# -*- coding: utf-8 -*-

import json


## Edit these then run the script to generate the data you need
captains = [
("Ballkenende", "Ballmere City", "ELTP", 10, 0, ["Berlin Ball",  "mP",   "4am",  "zeeres",   "lume", "Ballkenende",  "Evuelf",   "teoretyczny",  "NZ.",  "dodsfall"]),
("Jerry.", "Celtag Vigo", "ELTP", 15, 0, ["kutrebar",    "ethce",    "gofio",    "Jim Jimson",   "Jerry.",   "Umor", "Sam4096",  "Heisy",    "Vjeze",    "ClutchHunter"]),
("ethce", "FC Capoli", "ELTP", 0, 0, ["kutrebar",   "ethce",    "gofio",    "Jim Jimson",   "Jerry.",   "Umor", "Sam4096",  "Heisy",    "Vjeze",    "ClutchHunter"]),
("Chuck_Finley", "Stand-On-Re de Liège", "ELTP", 10, 5, ["Sea.",    "Nilus",    "okthen",   "piggeh",   "GrammarJew",   "Chuck_Finley", "Dor",  "Huck and D",   "Nice", "TheBob18"]),
]

managers = [
("Raylan", "Blocka Juniors", "ELTP", 0, 5, ["Nube", "Green",    "Sensei Osy",   "Battosay", "Poukie",   "Sanitence",    "Rob Flagetti", "NoctiZ",   "Vincent Osy",  "Raylan"], "Green"),
("bhayward2000", "Chaseterfield FC", "ELTP", 0, 0, ["Osy",  "SIGSEGV",  "anom", "EASHY",    "WishICared",   "Nayr", "The Juker",    "Young Savage", "anime.addict", "DEAD NAN"], "DEAD NAN"),
("damn, son!", "Momentum", "ELTP", 10, 0, ["Hyponome",   "nub",  "Strategio",    "unvrs",    "failed",   "MrSaggyBalls", "Bezeball", "damn, son!",   "Voodoo",   "Schwenks"], "AlHarrington"),
("rickastley", "The Rickrollers", "ELTP", 0, 0, ["Mpuddi",  "Booya Ball",   "dets", "DaEvil1",  "Fred_",    "Ronding",  "edvard41298",  "rickastley",   "Unplanned",    "wowah"], "Dyballa"),
]

starting_money = 100
keeper_money = 5
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
