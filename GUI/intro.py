import pygame
from Button import Button
from GameText import GameText

def game_intro():
    # num of players
    num_players = 0

    # set up intro display
    DISPLAY_SIZE = (800, 400)
    DISPLAY_COLOR = (15, 15, 15)
    gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption("Main Menu")
    gamedisplay.fill(DISPLAY_COLOR)
    background = pygame.image.load("GUI/background1.jpg")

    # Title
    game_title = Button((400,100), "GUI/intro_images/gametitle1.png", "GUI/intro_images/gametitle1.png", "GUI/intro_images/gametitle1.png", 0.4)

    # set up buttons
    play_button = Button((400,220), "GUI/intro_images/start1.png", "GUI/intro_images/start2.png", "GUI/intro_images/start2.png")
    button2 = Button((300,280), "GUI/intro_images/button21.png", "GUI/intro_images/button21.png", "GUI/intro_images/button22.png")
    button3 = Button((350,280), "GUI/intro_images/button31.png", "GUI/intro_images/button31.png", "GUI/intro_images/button32.png")
    button4 = Button((400,280), "GUI/intro_images/button41.png", "GUI/intro_images/button41.png", "GUI/intro_images/button42.png")
    button5 = Button((450,280), "GUI/intro_images/button51.png", "GUI/intro_images/button51.png", "GUI/intro_images/button52.png")
    button6 = Button((500,280), "GUI/intro_images/button61.png", "GUI/intro_images/button61.png", "GUI/intro_images/button62.png")

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.over():
                    if num_players == 0:
                        print("You must pick the number of players!")
                    else:
                        print("Loading Game!")
                        return num_players

                if button2.over():
                    num_players = 2
                    button2.clicked = True
                    button3.clicked = False
                    button4.clicked = False
                    button5.clicked = False
                    button6.clicked = False

                if button3.over():
                    num_players = 3
                    button2.clicked = False
                    button3.clicked = True
                    button4.clicked = False
                    button5.clicked = False
                    button6.clicked = False

                if button4.over():
                    num_players = 4
                    button2.clicked = False
                    button3.clicked = False
                    button4.clicked = True
                    button5.clicked = False
                    button6.clicked = False

                if button5.over():
                    num_players = 5
                    button2.clicked = False
                    button3.clicked = False
                    button4.clicked = False
                    button5.clicked = True
                    button6.clicked = False

                if button6.over():
                    num_players = 6
                    button2.clicked = False
                    button3.clicked = False
                    button4.clicked = False
                    button5.clicked = False
                    button6.clicked = True

        gamedisplay.blit(background, (-300, 0))
        game_title.show(gamedisplay)
        play_button.show(gamedisplay)
        button2.show(gamedisplay)
        button3.show(gamedisplay)
        button4.show(gamedisplay)
        button5.show(gamedisplay)
        button6.show(gamedisplay)
        pygame.display.update()
