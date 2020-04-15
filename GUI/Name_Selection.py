import pygame
from input_box import *
from GameText import *
from Button import *

def rescale(img, scale):
    h1, w1 = img.get_size()
    img = pygame.transform.scale(img, (int(h1*scale), int(w1*scale)))
    return img

def select(num_players):
    # display
    DISPLAY_SIZE = (1200, 700)
    DISPLAY_COLOR = (255, 255, 255)
    gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption("Main Menu")

    text_color = (30,30,30)
    title = GameText((500, 12), "PLAYER NAMES", text_color, 32)

    # Button
    next_button = Button((1090,640), "GUI/character_selection/button_next1.png", "GUI/character_selection/button_next2.png", "GUI/character_selection/button_next2.png", 1)


    # Texts
    text_x = 380
    text_y = 15
    text1 = GameText((text_x, text_y + 74), "PLAYER 1", text_color, 37)
    text2 = GameText((text_x, text_y + 2*74), "PLAYER 2", text_color, 37)
    text3 = GameText((text_x, text_y + 3*74), "PLAYER 3", text_color, 37)
    text4 = GameText((text_x, text_y + 4*74), "PLAYER 4", text_color, 37)
    text5 = GameText((text_x, text_y + 5*74), "PLAYER 5", text_color, 37)
    text6 = GameText((text_x, text_y + 6*74), "PLAYER 6", text_color, 37)

    # input box
    box_x = 600
    box_y = 15
    box1 = InputBox(box_x, box_y + 74, 270, 40)
    box2 = InputBox(box_x, box_y + 2*74, 270, 40)
    box3 = InputBox(box_x, box_y + 3*74, 270, 40)
    box4 = InputBox(box_x, box_y + 4*74, 270, 40)
    box5 = InputBox(box_x, box_y + 5*74, 270, 40)
    box6 = InputBox(box_x, box_y + 6*74, 270, 40)

    # Background
    #background = pygame.image.load("GUI/background_names.jpg")
    background = pygame.image.load("GUI/character_selection/background9.png")

    # Tokens
    boot = pygame.image.load("GUI/character_selection/boot.png")
    phone = pygame.image.load("GUI/character_selection/phone.png")
    hat = pygame.image.load("GUI/character_selection/hat.png")
    goblet = pygame.image.load("GUI/character_selection/goblet.png")
    cat = pygame.image.load("GUI/character_selection/cat.png")
    spoon = pygame.image.load("GUI/character_selection/spoon.png")

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

    names = []

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.over():
                    all_done = True
                    for box in boxes:
                        if box.text == "":
                            all_done = False
                            print("Please enter a name for each player!")
                        names.append(box.text)
                    if all_done:
                        return names
                    else:
                        names = []

            # handle input boxes
            for box in boxes:
                box.handle_event(event)

        gamedisplay.blit(background, (-700, -250))

        title.show(gamedisplay)

        for box in boxes:
            box.draw(gamedisplay)

        for text in texts:
            text.show(gamedisplay)

        text1.show(gamedisplay)

        if num_players >= 2:
            gamedisplay.blit(rescale(boot, 0.14), (270, 75))
            gamedisplay.blit(rescale(phone, 0.14), (270, 155))
        if num_players >= 3:
            gamedisplay.blit(rescale(hat, 0.06), (255, 240))
        if num_players >= 4:
            gamedisplay.blit(rescale(cat, 0.11), (265, 297))
        if num_players >= 5:
            gamedisplay.blit(rescale(goblet, 0.14), (247, 366))
        if num_players >= 6:
            gamedisplay.blit(rescale(spoon, 0.11), (265, 446))

        next_button.show(gamedisplay)

        pygame.display.update()
