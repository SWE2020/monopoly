# Import all other classes
from player import *
from tile import *
from Deck import *
from Bank import *
from die import *
from board import *
import display_token
import display_tile
import time

def pay_rent(game):
        current_player = game.get_turns().current()
        current_position = current_player.getPosition()
        current_tile = game.get_board().get_tile_at(current_position)
        owner = current_tile._owner
        amount = current_tile.get_rent(game)
        #print(current_player.getPlayerName(), " owner: ", owner.getPlayerName(), "tile: ", current_tile._name, "tile._position: ", current_tile._position , "amount: ", amount)
        if not owner.inJail:
            transfer_money(current_player, owner, amount)

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

def move(player, distance, game):
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
        GO_TO_JAIL = 30
        if new_position == GO_TO_JAIL:
                go_to_jail(game)


        # check FREE PARK
        FREE_PARK = 20
        if new_position == FREE_PARK:
                free_park_collect(game)


        # check TAX
        TAX1 = 4
        TAX2 = 38
        if new_position == TAX1 or new_position == TAX2:
                pay_tax(game)




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

        # move the player
        distance = roll1 + roll2
        game._last_roll = distance
        # display rect as background to the text
        pygame.draw.rect(display, (170,170,170), (145,480,400,75))

        # display roll output on screen
        roll_string = "YOU ROLLED: " + str(roll1) + " + " + str(roll2) + " = " + str(distance)
        roll_text = GUI.GameText((168,496), roll_string, (20,20,20), 36)
        roll_text.show(display)
        pygame.display.update()

        roll_wait_time = 500
        pygame.time.wait(roll_wait_time)

        # check if doubles for the second time => go to jail
        # change this to 3
        if player._double_counter == 2:
                go_to_jail(game)
                return "Finito"

        # next player will also be the current player
        if player._double_counter == 1:
                game.get_turns()._go_again = True
        move(player, distance, game)




def go_to_jail(game):
        """
        Send the current player to jail.
        """
        player = game.get_turns().current()
        display = game.get_board().get_display()

        # go to "go to jail tile" first
        jail_position = 30
        player.setPosition(jail_position)
        display_token.display_token(game)
        display_tile.display_current_tile(game)
        pygame.display.update()
        ROLL_WAIT_TIME = 5000
        pygame.time.wait(ROLL_WAIT_TIME)

        # update player's jail field
        player.inJail = True
        # teleport the player to the jail's position
        jail_position = 10
        player.setPosition(jail_position)
        pygame.draw.rect(display, (170,170,170), (145,480,400,75))

        # display roll output on screen
        roll_string = "TIME TO GO TO JAIL!"
        roll_text = GUI.GameText((174,496), roll_string, (20,20,20), 36)
        roll_text.show(display)
        display_token.display_token(game)
        display_tile.display_current_tile(game)

        pygame.display.update()
        ROLL_WAIT_TIME = 5000
        pygame.time.wait(ROLL_WAIT_TIME)


def buy_property(player, tile):
        cost = tile.get_cost()
        #print("cost: ", cost, " player.getBankBalance(): ", player.getBankBalance(), " tile: ", tile._name)
        player.setBankBalance(player.getBankBalance() - cost)
        player.propertiesOwned.append(tile)
        tile._owner = player

def buy_property(game):
        current_player = game.get_turns().current()
        current_position = current_player.getPosition()
        current_tile = game.get_board().get_tile_at(current_position)

        cost = current_tile.get_cost()
        current_player.setBankBalance(current_player.getBankBalance() - cost)
        current_player.propertiesOwned.append(current_tile)
        current_tile._owner = current_player

def pay_bail(game):
        current_player = game.get_turns().current()
        BAIL_COST = 50
        game._free_parking += BAIL_COST
        current_player.setBankBalance(current_player.getBankBalance() - BAIL_COST)

        JAIL_POSITION = 10
        current_player.setPosition(JAIL_POSITION)

        current_player.inJail = False

def free_park_collect(game):
        current_player = game.get_turns().current()
        display = game.get_board().get_display()

        # warning
        pygame.draw.rect(display, (170,170,170), (145,480,400,75))
        out_string = "YOU COLLECT " + str(game._free_parking) + "£ !"
        out_text = GUI.GameText((187,496), out_string, (20,20,20), 36)
        out_text.show(display)
        display_token.display_token(game)
        display_tile.display_current_tile(game)
        pygame.display.update()
        WAIT_TIME = 7000
        pygame.time.wait(WAIT_TIME)

        # transaction
        current_player.bankBalance += game._free_parking
        game._free_parking = 0



def pay_tax(game):
        current_player = game.get_turns().current()
        display = game.get_board().get_display()

        TAX = 100
        current_player.bankBalance -= TAX
        game._free_parking += TAX

        pygame.draw.rect(display, (170,170,170), (145,480,400,75))
        out_string = "PAYING TAX: 100£ !"
        out_text = GUI.GameText((179,496), out_string, (20,20,20), 36)
        out_text.show(display)
        display_token.display_token(game)
        display_tile.display_current_tile(game)
        pygame.display.update()
        WAIT_TIME = 7000
        pygame.time.wait(WAIT_TIME)
