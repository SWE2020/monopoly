import pygame
from game import Game
import buttons
import GUI
import tile
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
    rolled = False
    while not rolled:
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

    print(type(current_tile))

    while not passed:
        for event in pygame.event.get():
            check_quit(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if type(current_tile) == tile.PropertyTile:
                    if current_tile._owner == current_tile:
                        pass
                        # build house
                        # build hotel
                    if current_tile._owner.getPlayerName() == "None":
                        # buy property
                        # pass
                        pass

                print(type(current_tile))
                if buttons.button_end_turn.over():
                    return passed




        board.draw_board(game)
        buttons.button_end_turn.show(display)
        #buttons.buy_button.show(display)
        #buttons.pay_rent_button.show(display)
        pygame.display.update()

    return passed


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
