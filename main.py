import pygame
from game import Game
import buttons
import GUI
import tile
import time
pygame.init()

def main():
    # init game
    game = Game()

    # iterate over players
    while not game.is_over():

        # do this while the turn is still going on
        while game.get_turns().status():
            rolling_phase(game)
            action_phase(game)
            game.get_turns().end_turn()

        # set current player to next player; set status to True again
        game.get_turns().next()


def handle_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttons.handle_button_events(game)

def rolling_phase(game):
    board = game.get_board()
    display = board.get_display()
    while True:
        for event in pygame.event.get():
            check_quit(event)
            if event.type == pygame.MOUSEBUTTONDOWN and buttons.button_roll.over():
                buttons.button_roll_function(game)
                return "End Rolling Phase"

        board.draw_board(game)
        buttons.button_roll.show(display)
        pygame.display.update()

def action_phase(game):
    board = game.get_board()
    display = board.get_display()
    passed = False

    current_player = game.get_turns().current()
    current_position = current_player.getPosition()
    current_tile = game.get_board().get_tile_at(current_position)
    paid_rent = False

    while not passed:

        board.draw_board(game)
        mode = 0

        if type(current_tile) == tile.PropertyTile:
            # player owns the current tile
            if current_tile._owner == current_player:
                mode = 0
                # build house
                # build hotel
                buttons.button_end_turn.show(display)
            # No one owns the current tile
            elif current_tile._owner.getPlayerName() == "None":
                mode = 1
                buttons.button_buy.show(display)
                buttons.button_end_turn.show(display)
            else:
                mode = 2
                if not paid_rent:
                    buttons.button_pay_rent.show(display)

                buttons.button_end_turn.show(display)

        if type(current_tile) == tile.ActionTile:
                mode = 3
                buttons.button_end_turn.show(display)

            # if oppknocks

            # if potluck
            # if jail
            # if free parking

        # current tile is an Action Tile
        if type(current_tile) == tile.ActionTile:
            pass

        for event in pygame.event.get():
            check_quit(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 0:
                    if buttons.button_end_turn.over():
                        return buttons.button_end_turn_function(game)
                if mode == 1:
                    if buttons.button_buy.over():
                        buttons.button_buy_function(game)
                    if buttons.button_end_turn.over():
                        return buttons.button_end_turn_function(game)
                if mode == 2:
                    if buttons.button_pay_rent.over():
                        if paid_rent == False:
                            buttons.button_pay_rent_function(game)
                            paid_rent = True
                    if buttons.button_end_turn.over():
                        if paid_rent:
                            return buttons.button_end_turn_function(game)
                if mode == 3:
                    if buttons.button_end_turn.over():
                        return buttons.button_end_turn_function(game)


        pygame.display.update()



def builder_phase(game):
    pass

# if the player passes on a property, time for auction
def auction_phase(game):
    pass

def end_phase(game):
    pass

def check_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

if __name__ == '__main__':
    main()
