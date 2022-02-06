unitList = [
    {
        "name": "dragon",
        "description": {
            "mineral": 125,
            "gas": 50,
            "hp": 100,
            "defense": 5,
            "ofense": 8
        }
    },
    {
        "name": "templer",
        "description": {
            "mineral": 50,
            "gas": 125,
            "hp": 125,
            "defense": 3,
            "ofense": 20
        }
    }
]

unitList2 = {
    "dragon": {
        "mineral": 125,
        "gas": 50,
        "hp": 100,
        "defense": 5,
        "ofense": 8
    },
    "templer": {
        "mineral": 50,
        "gas": 125,
        "hp": 125,
        "defense": 3,
        "ofense": 20
    }
}

for unit in unitList:
    print(unit['name'])
    print(unit['description'])
    
print(unitList2["dragon"]["defense"])
print(unitList2["templer"]["defense"])