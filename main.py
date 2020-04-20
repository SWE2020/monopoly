import pygame
from game import Game
pygame.init()

def main():
    # init game
    game = Game()

    # iterate over players
    while not game.is_over():
        current_player = game.get_turns().current().getPlayerName()
        print(current_player)

        # do this while the turn is still going on
        while game.get_turns().status():

            handle_events(game)

            game.draw()

            # update display
            pygame.display.update()


        # set current player to next player; set status to True again
        game.get_turns().next()




def handle_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.get_turns().end_turn()


if __name__ == '__main__':
    main()
