import sys
sys.path.append('/Users/egeersu/Desktop/monopoly/GUI')
from Name_Selection import *
from Intro_Screen import *
#from Monopoly import *

import pygame
pygame.init()

def rescale(img, scale):
    h1, w1 = img.get_size()
    img = pygame.transform.scale(img, (int(h1*scale), int(w1*scale)))
    return img

# Music
#pygame.mixer.music.load("GUI/game_music.ogg")
#pygame.mixer.music.play(-1)

# Play the intro, save number of players
num_players = game_intro()
#num_players = 2

# Player Name Selection
Player_Names = select(num_players)
print(Player_Names)

# display
DISPLAY_SIZE = (1440,770); DISPLAY_COLOR = (110,110,110)
gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("Property Tycoon")
#background2 = pygame.image.load("GUI/background2.jpg")
board_image = pygame.image.load("GUI/Board.jpg")
prop = pygame.image.load("YFS.png")
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")

    gamedisplay.fill(DISPLAY_COLOR)
    gamedisplay.blit(board_image, (0, 0))
    gamedisplay.blit(rescale(prop, 0.20), (1130,0))
    pygame.display.update()




# Load the Game
#Players = [Player("Ege", "Car"), Player("Kaleb", "Phone"), Player("Evan", "Horse")]
#Game = Monopoly(Players)
#print(Game.get_player(0).getPlayerName())
