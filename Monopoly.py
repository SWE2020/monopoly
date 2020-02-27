from player import Player
from board import Board


class Monopoly:

    def __init__(self, player_count, player_tokens):

        self._player_count = player_count
        self._player_token = ['!', '@', '#', '$', '%', '^']
        self._players = {}
        self._board = Board()
        self._board.populate_board()
        for i in self._board.get_tile_list():
            print(i.get_name())



        for i in range(0, player_count):
            player = Player()
            self._players[i] = player

        print(self._players)

    def get_players(self):
        return self._players

    def get_player(self, key):

if __name__ == "__main__":
    game = Monopoly(6)