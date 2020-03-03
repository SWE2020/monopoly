from random import random, randint

from player import Player
from board import Board


class TurnManager:
    """
    A class to manage the order of turns amongst game players.
    """

    def __init__(self, players):
        """
        Construct a new turn manager based on game players.

        Parameters:
            players (List<T>): An ordered list of players to store.
        """
        self._players = players
        # Start in correct direction
        self._direction = True
        self._location = 0
        self._max = len(players)

    def current(self):
        return self._players[self._location]

    def next(self):
        return self.skip(count=0)

    def get_player(self, position):
        return self._players[position]

    def skip(self, count=0):
        count += 1
        self._location += count
        self._location %= self._max
        return self._players[self._location]


class Monopoly:

    def __init__(self, players):
        self._players = players
        self._turns = TurnManager(players)
        self._board = Board()
        self._board.populate_board()

        # Decks of Cards

        self._is_over = False
        self._winner = None

        self._action = None

    def get_players(self):
        return self._players

    def get_board(self):
        return self._board

    def get_player(self, key):
        return self._players[key]

    def current_player(self):
        return self._turns.current()

    def get_next_player(self):
        return self._turns.next()

    def get_turns(self):
        return self._turns

    def is_over(self):
        return self._is_over

    ## Is over for player in players, if playe has won: self.winner = player, self.isover = true
    #       return self._is over


if __name__ == "__main__":
    token_list = ['!', '@', '#', '$', '%', '^']
    # How many players do we want
    player_count = input("How many players are playing?  ")

    # Check that player count is not greater than 6
    while int(player_count) < 2 or int(player_count) > 6:
        print("This game is for between 2 and 6 players. ")
        player_count = input("How many players are playing?  ")

    player_list = []

    # Input the tokens for the players
    i = 0
    while i < int(player_count):
        token = None
        print("Player %d, you are up!" % int(i + 1))
        print("Please choose a token: [" + "][".join(token_list) + "]")
        token = input("Which token do you choose? ")
        while token not in token_list:
            print("Please choose a token: [" + "][".join(token_list) + "]")
            token = input("Which token do you choose? ")

        print("Player %d, your token is %s" % (i + 1, token))
        name = input("Please enter your name: ")
        token_list.remove(token)
        player_dummy = Player(name, token)
        player_dummy.setBankBalance(1500)
        player_list.append(player_dummy)
        i += 1

    # Create instance of Monopoly game
    game = Monopoly(player_list)
    #print(game.get_players())

    while not game.is_over():
        # Print the name and current location of the player
        name = game.current_player().getPlayerName()
        current_position = game.current_player().getPosition()
        print("Current player: " + str(name) +
              "   Location: " + str(game.get_board().get_tile_at(current_position).get_name()))
        input("Press any key to roll the dice ")
        dice_roll = randint(1,6) + randint(1,6)
        print("Dice roll value: " + str(dice_roll))
        print("%s moves %s spaces" % (name, dice_roll))
        # Current positon
        current_position = game.current_player().getPosition()
        game.current_player().setPosition((current_position + dice_roll))
        current_position = game.current_player().getPosition()
        print("%s has landed on %s" % (name, game.get_board().get_tile_at(current_position).get_name()))
        decision = input("Current actions are %s " % (", ".join(["Buy", "Skip"])))
        if decision == "buy":
            # Add property to the players hand
            game.current_player().propertiesOwned.append(game.get_board().get_tile_at(current_position))
            # Deduct that amount from the
            game.current_player().bankBalance -= game.get_board().get_tile_at(current_position).get_cost()
        print("%s, it is the end of your turn")
        print("| Account Balance: %s | Properties Owned: %s | Location: %s)" % (game.current_player().getBankBalance(),
                                                                                game.current_player().getPropertiesOwned(),
                                                                                game.get_board().get_tile_at(current_position).get_name()))
        input("Press any key to continue to the next player.")
        game.get_turns().next()