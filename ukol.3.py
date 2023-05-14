import json

with open('body.json', 'r') as file:
    body = json.load(file)

prospech = {}

for jmena_zaku in body:
    if body[jmena_zaku] >= 60:
        prospech[jmena_zaku] = 'Pass'
    else:
        prospech[jmena_zaku] = 'Fail'

with open("prospech.json", "w") as file:
    json.dump(body, file)
