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
            #action_phase(game)
            #end_phase(game)
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

def action_phase(game):
    board = game.get_board()
    display = board.get_display()
    passed = False

    while not passed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and buttons.buy_button.over():
                print("bought")
            if event.type == pygame.MOUSEBUTTONDOWN and buttons.pay_rent_button.over():
                print("paid rent")

        board.draw_board(game)
        buttons.buy_button.show(display)
        buttons.pay_rent_button.show(display)
        pygame.display.update()

# if the player passes on a property, time for auction
def auction_phase(game):
    pass

def end_phase(game):
    pass


if __name__ == '__main__':
    main()
