import pygame
from game import Game
import buttons
pygame.init()

def main():
    # init game
    game = Game()

    # iterate over players
    while not game.is_over():
        current_player = game.get_turns().current().getPlayerName()
        print(game.get_players()[0].getTokenName())

        # do this while the turn is still going on
        while game.get_turns().status():
            rolling_phase(game)
            #handle_events(game)
            # update display
            game.get_turns().end_turn()
        # set curret player to next player; set status to True again
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
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            buttons.roll_button.show(display)
            if event.type == pygame.MOUSEBUTTONDOWN and buttons.roll_button.over():
                buttons.roll_button_function(game)
                return "End Rolling Phase"

        board.draw_board(game)
        buttons.roll_button.show(display)
        pygame.display.update()


if __name__ == '__main__':
    main()
