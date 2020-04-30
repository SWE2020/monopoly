# Import all other classes
import player
import tile
import board
import display_token
import display_tile
import bidder

import pygame
import GUI

def pay_rent(game):
        current_player = game.get_turns().current()
        current_position = current_player.getPosition()
        current_tile = game.get_board().get_tile_at(current_position)
        owner = current_tile._owner
        amount = current_tile.get_rent(game)
        #print(current_player.getPlayerName(), " owner: ", owner.getPlayerName(), "tile: ", current_tile._name, "tile._position: ", current_tile._position , "amount: ", amount)
        if not owner.inJail:
            transfer_money(current_player, owner, amount)

def transfer_money(player_from, player_to, amount):
        """ Transfers money from a player to another player"""
        player_from.bankBalance -= amount
        player_to.bankBalance += amount


def GO(player):
        """Call this function when a player completes a full circle"""
        GO_MONEY = 200
        player.bankBalance += GO_MONEY

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
        if new_position >= num_tiles:
                player._passed_go_once = True
                GO(player)

        new_position %= num_tiles
        player.position = new_position

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
        pygame.draw.rect(display, (170,170,170), (145,480,400,75))
        roll_string = "TIME TO GO TO JAIL!"
        roll_text = GUI.GameText((174,496), roll_string, (20,20,20), 36)
        roll_text.show(display)
        player.setPosition(jail_position)
        display_token.display_token(game)
        display_tile.display_current_tile(game)
        pygame.display.update()
        WAIT_TIME = 2000
        pygame.time.wait(WAIT_TIME)

        # update player's jail field
        player.inJail = True
        # teleport the player to the jail's position
        jail_position = 10
        player.setPosition(jail_position)
        display_token.display_token(game)
        display_tile.display_current_tile(game)

        pygame.display.update()
        ROLL_WAIT_TIME = 1200
        pygame.time.wait(ROLL_WAIT_TIME)


def buy_property(player, tile):
        """
        Player player buys the Tile tile.
        """
        cost = tile.get_cost()
        player.setBankBalance(player.getBankBalance() - cost)
        player.propertiesOwned.append(tile)
        tile._owner = player

def buy_property(game):
        """
        Current player buys the property he is on.
        """
        current_player = game.get_turns().current()
        current_position = current_player.getPosition()
        current_tile = game.get_board().get_tile_at(current_position)

        cost = current_tile.get_cost()
        current_player.setBankBalance(current_player.getBankBalance() - cost)
        current_player.propertiesOwned.append(current_tile)
        current_tile._owner = current_player

def pay_bail(game):
        """
        Player pays 50 to get out of jail.
        """
        current_player = game.get_turns().current()
        BAIL_COST = 50
        game._free_parking += BAIL_COST
        current_player.setBankBalance(current_player.getBankBalance() - BAIL_COST)

        JAIL_POSITION = 10
        current_player.setPosition(JAIL_POSITION)

        current_player.inJail = False

def free_park_collect(game):
        """
        Give all free parking money to current player.
        """
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
        WAIT_TIME = 2000
        pygame.time.wait(WAIT_TIME)

        # transaction
        current_player.bankBalance += game._free_parking
        game._free_parking = 0



def pay_tax(game):
        """
        Current player pays TAX.
        Puts that amount into free parking.
        """
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
        WAIT_TIME = 2000
        pygame.time.wait(WAIT_TIME)

def build(game, target_tile):
        """
        Builds a house on the target tile.
        If it has 4 houses, builds a hotel instead.
        """
        current_player = game.get_turns().current()
        current_position = current_player.getPosition()

        if type(target_tile) == tile.PropertyTile and target_tile.check_full_group(game):
                if target_tile.get_hotel_count() == 0:
                        if target_tile.get_house_count() != 4:
                                target_tile.add_house()
                        else:
                                target_tile.add_hotel()

                        building_cost = target_tile.get_cost()
                        current_player.removeBankBalance(building_cost)




def demolish(game, target_tile):
        """
        Removes a hotel from the target tile.
        If there is no hotel, removes a single house.
        The player gets a refund.
        """
        current_player = game.get_turns().current()
        current_position = current_player.getPosition()

        if type(target_tile) == tile.PropertyTile:
                refund = target_tile.demolish()
                print("refund: ", refund)
                current_player.addBankBalance(refund)


def end_turn(game, bought_something):
        if bought_something:
                return "end turn"
        else:
                current_player = game.get_turns().current()
                current_position = current_player.getPosition()
                current_tile = game.get_board().get_tile_at(current_position)

                prop_bidder = bidder.Bidder(game)
                max_bidder, max_bid = prop_bidder.bid_all()

                max_bidder.removeBankBalance(max_bid)
                max_bidder.addPropertyOwned(current_tile)
                current_tile._owner = max_bidder
