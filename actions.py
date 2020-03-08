# Import all other classes
from player import *
from Tile import *
from Deck import *
from Bank import *
from Die import *
from board import *
#from Monopoly import Monopoly, TurnManager

def transfer_money(FROM, TO, amount):
        """ Transfers money from a player to another player"""
        FROM.bankBalance -= amount
        TO.bankBalance += amount
        # check if bankrupt?


def GO(player, bank):
        """Call this function when a player completes a full circle"""
        GO_money = 200
        bank.withdraw(GO_money)
        player.bankBalance += GO_money

def move(player, distance):
        """
        Call this function to move a player around the board, given a distance.
        It checks for the following conditions:
                * A full lap around the board => invoke the GO function
                *
        """
        num_tiles = 40
        new_position = player.position + distance

        #check if the player completed a full lap around the board
        if new_position > num_tiles:
                new_position %= num_tiles
                #we will have to get bank from the Game.bank when Game.py is implemented
                bank1 = Bank(1000)
                #invoke GO
                GO(player, bank1)

        # update player's position to his new position
        player.position = new_position

def roll_dice(player):
        """
        Make a player roll the dice.
        Move the player.
        Check if the player rolled doubles.
        """
        # the dice should be re-initialized after we switch players
        # or simply set double_counter = 0

        dice = Die()
        dice_result = dice.roll()

        # move the player
        distance = sum(dice_result)
        move(player, distance)

        # check if doubles for the first time => it's player's turn again
        if dice.double_counter == 1:
                # game.setplayer
                pass
        # check if doubles for the second time => go to jail
        if dice.double_counter == 2:
                go_to_jail(player)


def go_to_jail(player):
        """
        Send a player to jail.
        """
        # update player's jail field
        player.setInJail(True)
        # teleport the player to the jail's position
        jail_position = 15
        player.setPosition(jail_position)

#transfer property?

#card actions! (another file?)
