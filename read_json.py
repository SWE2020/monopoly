import json

"""
Reads the JSON file named "CardData.json"
There are 32 Cards, each one is represented by a Python dictionary
Returns a list of dictionaries where each dictionary has keys:
    'Description'
    'Action'
    'Card Type'
"""
def read_CardData(path_file="CardData.json"):
    with open(path_file, "r") as read_file:
        data = json.load(read_file)
    return data

"""
Reads the JSON file named "PropData.json"
There are 51 Properties, each one is represented by a Python dictionary
Returns a list of dictionaries where each dictionary has keys:
    'Position'
    'Type'
    'Group'
    'Action'
    'CanBuy'
    'Rent'
    '1 house'
    '2 house'
    '3 house'
    '4 house'
    '1 hotel'
"""

def read_PropData(path_file="PropData.json"):
    with open(path_file, "r") as read_file:
        data = json.load(read_file)
    return data
