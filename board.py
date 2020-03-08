import json
from Tile import Tile, PropertyTile, ActionTile

class Board:

    def __init__(self):

        self._tile_list = []

    def populate_board(self):

        with open("PropData.json", "r") as read_file:
            json_format = json.load(read_file)

        for item in json_format:
            self._tile_list.append(self.create_tile(item))

    def create_tile(self, json_tile):

        position = json_tile['Position']
        name = json_tile['Space/property']
        group = json_tile['Group']
        action = json_tile['Action']
        can_be_bought = json_tile['Can be bought?']
        cost = json_tile['Cost']
        rent = json_tile['Rent (unimproved)']
        rent1 = json_tile['1 house']
        rent2 = json_tile['2 houses']
        rent3 = json_tile['3 houses']
        rent4 = json_tile['4 houses']
        hotel = json_tile['1 hotel']

        if can_be_bought:
            tile = PropertyTile(position, name, group, action, can_be_bought, cost, rent, rent1, rent2, rent3, rent4, hotel)

        else:
            tile = ActionTile(position, name, group, action, can_be_bought, cost, rent, rent1, rent2, rent3, rent4, hotel)

        return tile

    def get_tile_list(self):
        return self._tile_list

    def get_tile_at(self, int):
        return self._tile_list[int]
