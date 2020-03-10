import json
from Tile import *
from Card import *

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
    'Name'
    'Action'
    'CanBuy'
    'Cost'
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

def create_tiles(array):
    empty = []
    for i in array:
        empty.append(parse_dictionary(i))

    return empty

def create_cards(array):
    empty = []
    for i in array:
        empty.append(parse_dictionary_1(i))

def parse_dictionary(dictionary):

    position = dictionary['Position']
    name = dictionary['Space/property']
    group = dictionary['Group']
    action = dictionary['Action']
    can_be_bought = dictionary['Can be bought?']
    cost = dictionary['Cost']
    rent = dictionary['Rent (unimproved)']
    rent1 = dictionary['1 house']
    rent2 = dictionary['2 houses']
    rent3 = dictionary['3 houses']
    rent4 = dictionary['4 houses']
    hotel = dictionary['1 hotel']

    if dictionary['Can be bought?'] == True:
        print("PropertyTile")
        #ropertyTile()
        p = PropertyTile(position, name, group, action, can_be_bought, cost, rent, rent1, rent2, rent3, rent4, hotel)
        return p
    else:
        print("ActionTile")
        p = ActionTile(position, name, group, action, can_be_bought, cost, rent, rent1, rent2, rent3, rent4, hotel)
        return p


def parse_dictionary_1(dictionary):
    class_id = dictionary["Card_ID"]
    subclass = dictionary["SubClassType"]
    description = dictionary["Description"]
    action_data = dictionary["ActionData"]
    # action_description = dictionary["CanBuy"]
    card_type = dictionary["Card Type"]

    if subclass == "Payment":
        PaymentCard()
    elif subclass == "Movement":
        pass
    elif subclass == "JailFree":
        pass








if __name__ == "__main__":
    x = read_CardData()
    for i in x:
        if i['SubClassType'] == "Payment":
            print("pay")
            PaymentCard()
        elif i['SubClassType'] == "Movement":
            print("move")
        elif i['SubClassType'] == "JailFree":
            print("Jaily")


