from random import random, randint
from turn_manager import TurnManager
import GUI
from actions import *

class Game:

    def __init__(self):

        self._players = []
        self._tokens = ["boot", "phone", "hat", "cat", "goblet", "spoon"]
        self.play_intro()


        self._turns = TurnManager(self._players)

        self._board = Board()
        self._board.populate_board()
        self._board.setup_board()

        self._is_over = False
        self._winner = None

    def play_intro(self):
        #pygame.mixer.music.load("soundtrack.mp3")
        #pygame.mixer.music.play(-1)

        num_players = GUI.game_intro()
        #num_players = 4

        player_names = GUI.select(num_players)
        #player_names = ["Ege", "Kaleb", "Evan", "Sydney"]

        for i in range(num_players):
            new_player = Player(player_names[i], self._tokens[i])
            self._players.append(new_player)


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

    def draw(self):
        self._board.draw_board(self)

"""
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
"""
