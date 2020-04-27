import pygame
import GUI
import tile

def display_target_tile(game):
    """displays the tile that is targeted by the player's cursor and highlights that tile on the board"""
    board = game.get_board()
    display = board.get_display()
    tile_rects = board._tile_rects

    background = pygame.image.load("GUI/images/wall.png")
    x,y = pygame.mouse.get_pos()

    # if the mouse is currently on a tile
    for (target_index, rect) in enumerate(tile_rects):

        if rect.collidepoint(x,y):

            # background
            display.blit(background, (890,425))

            #highlight the tile
            highlight = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
            highlight.fill((0,0,0,128))
            display.blit(highlight, (rect[0], rect[1]))

            # get the corrensponding tile
            target_tile = board.get_tile_at(target_index)

            # display the target card
            target_tile.get_image().set_alpha(255)
            display.blit(target_tile.get_image(), (685, 408))
            print(target_tile.get_image())

            # display owner of the tile
            owner_string = "Owned by: " + target_tile._owner.getPlayerName()
            owner_text = GUI.GameText((952, 458), owner_string, (40,40,40), 33)
            owner_text.show(display)

            # number of houses and hotels
            if type(target_tile) == tile.PropertyTile:
                num_houses = "Number of houses: " + str(target_tile.get_house_count())
                num_hotels = "Number of Hotels: " + str(target_tile.get_hotel_count())
                house_text = GUI.GameText((952, 520), num_houses, (40,40,40), 25)
                hotel_text = GUI.GameText((952, 555), num_hotels, (40,40,40), 25)
                house_text.show(display)
                hotel_text.show(display)

                info1 = "Click on a tile to build a house on it."
                info2 = "If you already have 4 houses, it will build a hotel."
                info3 = "Shift-Click on a tile to mortgage that property."
                info1_text = GUI.GameText((952, 680), info1, (40,40,40), 17)
                info2_text = GUI.GameText((952, 700), info2, (40,40,40), 17)
                info3_text = GUI.GameText((952, 720), info3, (40,40,40), 17)

                info1_text.show(display)
                info2_text.show(display)
                info3_text.show(display)


        # if a flag is false
        #print("display current tile in this same format, put the above code in a func?")

def display_current_tile(game):
    """displays the tile on which the current player stands"""
    # diplay current tile's property card on screen
    x,y = pygame.mouse.get_pos()
    display = game.get_board().get_display()
    current_position = game.get_turns().current().getPosition()
    current_tile = game.get_board().get_tile_at(current_position)
    current_image = current_tile.get_image()
    current_image.set_alpha(255)
    display.blit(current_image, (230, 105))
    # highlight current tile on the board
    current_location = game.get_turns().current().getPosition()
    rect = tile_boxes[current_location]
    highlight = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
    highlight.fill((255,0,0,175))
    display.blit(highlight, (rect[0], rect[1]))

# coordinates for the tiles
tile_boxes = {
    0:(588,587,90,90),
    1:(535,589,47,90),
    2:(481,589,47,90),
    3:(427,589,47,90),
    4:(372,588,47,90),
    5:(319,588,47,90),
    6:(265,588,47,90),
    7:(211,586,47,90),
    8:(156,587,47,90),
    9:(102,587,47,90),
    10:(5,587,90,90),
    11:(1,534,94,47),
    12:(1,481,94,47),
    13:(1,427,94,47),
    14:(2,371,94,47),
    15:(2,315,94,47),
    16:(2,260,94,47),
    17:(2,207,94,47),
    18:(1,152,94,47),
    19:(1,99,94,47),
    20:(3,1,92,90),
    21:(102,1,48,92),
    22:(156,1,48,92),
    23:(210,1,48,92),
    24:(264,0,48,92),
    25:(318,0,48,92),
    26:(372,1,48,92),
    27:(426,0,48,92),
    28:(480,1,48,92),
    29:(534,1,48,92),
    30:(588,1,90,90),
    31:(587, 98,94,47),
    32:(587,153,94,47),
    33:(587,207,94,47),
    34:(587,261,94,47),
    35:(587,316,94,47),
    36:(587,370,94,47),
    37:(587,426,94,47),
    38:(587,480,94,47),
    39:(587,534,94,47)
}

def create_tile_rects():
    """creates a pygame.Rect object correspoding to each tile"""
    rects = []
    for i in range(40):
        x,y,w,h = tile_boxes[i]
        rects.append(pygame.Rect(x,y,w,h))
    return rects
