import pygame
from GUI.utils import Button, GameText, InputBox, rescale

def select(num_players):
    # display
    DISPLAY_SIZE = (1200, 700)
    DISPLAY_COLOR = (255, 255, 255)
    gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption("Main Menu")

    text_color = (30,30,30)
    title = GameText((500, 12), "PLAYER NAMES", text_color, 32)

    # Button
    next_button = Button((1090,640), "GUI/images/name_selection_images/button_next1.png", "GUI/images/name_selection_images/button_next2.png", "GUI/images/name_selection_images/button_next2.png", 1)


    # Texts
    text_x = 385
    text_y = 15
    text1 = GameText((text_x, text_y + 74), "PLAYER 1", text_color, 37)
    text2 = GameText((text_x, text_y + 2*74), "PLAYER 2", text_color, 37)
    text3 = GameText((text_x, text_y + 3*74), "PLAYER 3", text_color, 37)
    text4 = GameText((text_x, text_y + 4*74), "PLAYER 4", text_color, 37)
    text5 = GameText((text_x, text_y + 5*74), "PLAYER 5", text_color, 37)
    text6 = GameText((text_x, text_y + 6*74), "PLAYER 6", text_color, 37)

    # input box
    box_x = 590
    box_y = 15
    box1 = InputBox(box_x, box_y + 74, 270, 40)
    box2 = InputBox(box_x, box_y + 2*74, 270, 40)
    box3 = InputBox(box_x, box_y + 3*74, 270, 40)
    box4 = InputBox(box_x, box_y + 4*74, 270, 40)
    box5 = InputBox(box_x, box_y + 5*74, 270, 40)
    box6 = InputBox(box_x, box_y + 6*74, 270, 40)

    # ai buttons
    ai_x = 910
    ai_y = 33
    ai1 = Button((ai_x, ai_y + 74), "GUI/images/name_selection_images/human.png", "GUI/images/name_selection_images/robot.png", "GUI/images/name_selection_images/robot.png")
    ai2 = Button((ai_x, ai_y + 2*74), "GUI/images/name_selection_images/human.png", "GUI/images/name_selection_images/robot.png", "GUI/images/name_selection_images/robot.png")
    ai3 = Button((ai_x, ai_y + 3*74), "GUI/images/name_selection_images/human.png", "GUI/images/name_selection_images/robot.png", "GUI/images/name_selection_images/robot.png")
    ai4 = Button((ai_x, ai_y + 4*74), "GUI/images/name_selection_images/human.png", "GUI/images/name_selection_images/robot.png", "GUI/images/name_selection_images/robot.png")
    ai5 = Button((ai_x, ai_y + 5*74), "GUI/images/name_selection_images/human.png", "GUI/images/name_selection_images/robot.png", "GUI/images/name_selection_images/robot.png")
    ai6 = Button((ai_x, ai_y + 6*74), "GUI/images/name_selection_images/human.png", "GUI/images/name_selection_images/robot.png", "GUI/images/name_selection_images/robot.png")

    ai1._mode = 0
    ai2._mode = 1
    ai3._mode = 1
    ai4._mode = 1
    ai5._mode = 1
    ai6._mode = 1


    # Background
    background = pygame.image.load("GUI/images/backgrounds/background9.png")

    # Tokens
    boot = pygame.image.load("GUI/images/name_selection_images/boot.png")
    phone = pygame.image.load("GUI/images/name_selection_images/phone.png")
    hat = pygame.image.load("GUI/images/name_selection_images/hat.png")
    goblet = pygame.image.load("GUI/images/name_selection_images/goblet.png")
    cat = pygame.image.load("GUI/images/name_selection_images/cat.png")
    spoon = pygame.image.load("GUI/images/name_selection_images/spoon.png")

    # AI vs Human


    if num_players == 2:
        texts = [text1, text2]
        boxes = [box1, box2]
        ai_buttons = [ai1, ai2]
    if num_players == 3:
        texts = [text1, text2, text3]
        boxes = [box1, box2, box3]
        ai_buttons = [ai1, ai2, ai3]
    if num_players == 4:
        texts = [text1, text2, text3, text4]
        boxes = [box1, box2, box3, box4]
        ai_buttons = [ai1, ai2, ai3, ai4]

    if num_players == 5:
        texts = [text1, text2, text3, text4, text5]
        boxes = [box1, box2, box3, box4, box5]
        ai_buttons = [ai1, ai2, ai3, ai4, ai5]

    if num_players == 6:
        texts = [text1, text2, text3, text4, text5, text6]
        boxes = [box1, box2, box3, box4, box5, box6]
        ai_buttons = [ai1, ai2, ai3, ai4, ai5, ai6]

    ai_info = []
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
                    for (i, box) in enumerate(boxes):
                        if box.text == "":
                            all_done = False
                        names.append(box.text)
                        ai_info.append(ai_buttons[i]._mode)
                    if all_done:
                        return names, ai_info
                    else:
                        names = []
                for ai_button in ai_buttons:
                    if ai_button.over():
                        ai_button.mode_switch()

            # handle input boxes
            for box in boxes:
                box.handle_event(event)

        gamedisplay.blit(background, (-700, -250))

        title.show(gamedisplay)

        for box in boxes:
            box.draw(gamedisplay)

        for ai_button in ai_buttons:
            ai_button.show2(gamedisplay)

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
