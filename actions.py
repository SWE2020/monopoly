# Import all other classes
from player import *
from tile import *
from Deck import *
from Bank import *
from die import *
from board import *
import time

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
                * New position is GO TO JAIL => GO TO JAIL
        """
        num_tiles = 40
        new_position = player.position + distance

        #check if the player completed a full lap around the board
        if new_position > num_tiles:
                bank1 = Bank(1000)
                GO(player, bank1)

        player.position = new_position % num_tiles

        # check GO TO JAIL
        if new_position == 30:
                go_to_jail(player)


def roll_dice(game):
        """
        Make a player roll the dice.
        Move the player.

        Conditions:
        Double for the first time => Next turn is also this player's
        Double for the second time => GO TO JAIL
        """
        # the dice should be re-initialized after we switch players
        # or simply set double_counter = 0
        player = game.get_turns().current()
        board = game.get_board()
        display = board.get_display()

        roll1, roll2 = game.get_turns().roll()

        if roll1 == roll2:
                player._double_counter += 1
        if roll1 != roll2:
                player._double_counter = 0

        if player._double_counter == 1:
                # game.setplayer
                pass

        # check if doubles for the second time => go to jail
        if player._double_counter == 2:
                go_to_jail(player)
                return "Finito"

        # move the player
        distance = roll1 + roll2
        # display rect as background to the text
        pygame.draw.rect(display, (170,170,170), (145,480,400,75))

        # display roll output on screen
        roll_string = "YOU ROLLED: " + str(roll1) + " + " + str(roll2) + " = " + str(distance)
        roll_text = GUI.GameText((168,496), roll_string, (20,20,20), 36)
        roll_text.show(display)
        pygame.display.update()

        roll_wait_time = 8000
        pygame.time.wait(roll_wait_time)

        move(player, distance)


def go_to_jail(player):
        """
        Send a player to jail.
        """
        # update player's jail field
        player.inJail = True
        # teleport the player to the jail's position
        jail_position = 15
        player.setPosition(jail_position)


def buy_property(player, tile):
        cost = tile.get_cost()
        #print("cost: ", cost, " player.getBankBalance(): ", player.getBankBalance(), " tile: ", tile._name)
        player.setBankBalance(player.getBankBalance() - cost)
        player.propertiesOwned.append(tile)
        tile._owner = player
