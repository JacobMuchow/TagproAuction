import json


## Edit these then run the script to generate the data you need
captains = [
("AlHarrington", "Åball IFK", "ECLTP", 0, 5, ["MagicPigeon", "The Real IRS", "NewCompte", "Jim Jimson", "Player", "sweatypete", "-Jacob-", "Irish_Jesus", "SunnyMojo", "MonteCristo", "Harmony", "Fuzzy", "KBreezy" ]),
("Battosay", "Team Battosay", "ECLTP", 0, 0, ["Dyballa", "piggeh", "Nice", "katazei", "juke' em all", "Electroball", "LoweJ", "some banter", "Daffodil", "Button", "Mathi Oi"]),
("GrammarJew", "Peräsuolijoen Palloilijat", "ECLTP", 0, 0, ["MagicPigeon", "The Real IRS", "NewCompte", "Jim Jimson", "Player", "sweatypete", "-Jacob-", "Irish_Jesus", "SunnyMojo", "MonteCristo", "Harmony", "Fuzzy", "KBreezy"]),
("Sea.", "Celtag Vigo", "ECLTP", 0, 0, ["Jerry.", "Chuck_Finley", "zeeres", "n00b", "Sunny", "Huck and D", "anime addict", "J Belfort", "Squirrely", "dodsfall", "Nuts!", "Juke Dough", "phoenixx", "ParvoB19"]),
("Sensei Osy", "Ball Street", "ECLTP", 0, 0, ["Muccy", "Poukie", "Vincent Osy", "wowah", "Caro-Kann", "Wait", "ElMiracle", "Rojale", "B.Fraser", "JasonGenova.", "Bouh!", "themagpie"]),
("MrSaggyBalls", "BSC Young Balls", "ECLTP", 0, 5, ["Fat", "Nilus", "Comakip", "NZ.", "WishICared", "eggdog", "damn, son!", "ClutchHunter", "teoretyczny", "SoapyMcguire", "Ghaul", "Phreak", "Mattyicy"]),
]

managers = [
("bhayward2000", "Chasterfield FC", "ECLTP", 0, 0, ["Osy", "Heisy", "Ruud", "Sisu", "The Juker", "Koekjes", "Vjeze", "LotsO'Huggin", "ruff", "Troupee", "EASHY", "Bustaball", "Ball Grylls"], "Sherrattinho"),
("Ballkenende", "Ballmere City", "ECLTP", 0, 5, ["Green", "Strategio", "Ballkenende", "weisbrot", "Nayr", "Sam4096", "Testi", "Jolt", "alchemist", "ALCAEUS", "Gummi", "Such A Nerd", "GrabMachine", "Triple A"], "kutrebar"),
("Unplanned", "unny's Flagettis", "ECLTP", 0, 0, ["Sam-", "unvrs", "MikeC", "Bezeball", "Wu", "MoGGee", "schwenks", "Muzza", "Tagnoob", "Kodiak", "EphewSeaKay", "Nooga"], "ethce"),
("rickastley", "RickRollers", "ECLTP", 0, 5, ["Muccy", "Poukie", "Vincent Osy", "wowah", "Caro-Kann", "Wait", "ElMiracle", "Rojale", "B.Fraser", "JasonGenova.", "Bouh!", "themagpie"], "Nube"),
]

starting_money = 100
keeper_money = 5
team_size = 4

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
