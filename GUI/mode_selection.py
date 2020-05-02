import pygame
from GUI.utils import Button, GameText, InputBox

def mode_select():
    # num of players
    num_players = 0
    print("running mode_selection")

    # set up intro display
    DISPLAY_SIZE = (700, 280)
    gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption("Pick Game Mode")
    background = pygame.image.load("GUI/images/backgrounds/background9.png")
    # title
    full_button = Button((180,140), "GUI/images/buttons/button_full_game_2.png", "GUI/images/buttons/button_full_game_1.png", "GUI/images/buttons/button_full_game_1.png")
    abridged_button = Button((520,140), "GUI/images/buttons/button_abridged_game_2.png", "GUI/images/buttons/button_abridged_game_1.png", "GUI/images/buttons/button_abridged_game_1.png")

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if full_button.over():
                        return "Full"
                if abridged_button.over():
                        return "Abridged"

        gamedisplay.blit(background, (-920, -680))
        full_button.show(gamedisplay)
        abridged_button.show(gamedisplay)
        pygame.display.update()
