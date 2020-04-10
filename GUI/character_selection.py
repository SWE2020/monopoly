import pygame
from input_box import *
from GameText import *

def rescale(img, scale):
    h1, w1 = img.get_size()
    img = pygame.transform.scale(img, (int(h1*scale), int(w1*scale)))
    return img

def select(num_players):

    # display
    DISPLAY_SIZE = (728, 430)
    DISPLAY_COLOR = (255, 255, 255)
    gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption("Main Menu")


    text_color = (148,0,211)
    title = GameText((250, 30), "PLAYER NAMES", text_color)

    # Texts
    text_x = 200
    text_y = 30
    text1 = GameText((text_x, text_y + 50), "PLAYER 1", text_color)
    text2 = GameText((text_x, text_y + 2*50), "PLAYER 2", text_color)
    text3 = GameText((text_x, text_y + 3*50), "PLAYER 3", text_color)
    text4 = GameText((text_x, text_y + 4*50), "PLAYER 4", text_color)
    text5 = GameText((text_x, text_y + 5*50), "PLAYER 5", text_color)
    text6 = GameText((text_x, text_y + 6*50), "PLAYER 6", text_color)

    # input box
    box_x = 370
    box_y = text_y - 10
    box1 = InputBox(box_x, box_y + 50, 200, 40)
    box2 = InputBox(box_x, box_y + 2*50, 200, 40)
    box3 = InputBox(box_x, box_y + 3*50, 200, 40)
    box4 = InputBox(box_x, box_y + 4*50, 200, 40)
    box5 = InputBox(box_x, box_y + 5*50, 200, 40)
    box6 = InputBox(box_x, box_y + 6*50, 200, 40)

    # images
    background = pygame.image.load("GUI/background_names.jpg")
    boot = pygame.image.load("GUI/character_selection/boot.png")
    phone = pygame.image.load("GUI/character_selection/phone.png")
    goblet = pygame.image.load("GUI/character_selection/goblet.png")
    hat = pygame.image.load("GUI/character_selection/hat.png")

    if num_players == 2:
        texts = [text1, text2]
        boxes = [box1, box2]
    if num_players == 3:
        texts = [text1, text2, text3]
        boxes = [box1, box2, box3]
    if num_players == 4:
        texts = [text1, text2, text3, text4]
        boxes = [box1, box2, box3, box4]
    if num_players == 5:
        texts = [text1, text2, text3, text4, text5]
        boxes = [box1, box2, box3, box4, box5]
    if num_players == 6:
        texts = [text1, text2, text3, text4, text5, text6]
        boxes = [box1, box2, box3, box4, box5, box6]


    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

            # handle input boxes
            for box in boxes:
                box.handle_event(event)

        gamedisplay.blit(background, (0, 0))

        title.show(gamedisplay)

        for box in boxes:
            box.draw(gamedisplay)

        for text in texts:
            text.show(gamedisplay)

        text1.show(gamedisplay)

        image1.show

        pygame.display.update()


select(6)
