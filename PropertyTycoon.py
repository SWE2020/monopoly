import sys
sys.path.append('/Users/egeersu/Desktop/monopoly/GUI')
from intro import *
from Monopoly import *

import pygame
pygame.init()

# Music
#pygame.mixer.music.load("GUI/game_music.ogg")
#pygame.mixer.music.play(-1)

# Play the intro, save number of players
#num_players = game_intro()
num_players = 2
#print(num_players)

# display
# display
DISPLAY_SIZE = (1440,770); DISPLAY_COLOR = (110,110,110)
gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("Property Tycoon")
background2 = pygame.image.load("GUI/background2.jpg")
board1 = pygame.image.load("GUI/board1.png")
prop = pygame.image.load("GUI/property1.jpg")
car = pygame.image.load("GUI/car.png")
marker = pygame.image.load("GUI/marker1.png")


def rescale(img, scale):
    h1, w1 = img.get_size()
    img = pygame.transform.scale(img, (int(h1*scale), int(w1*scale)))
    return img

x1 = 395
x2 = 97
run = True
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")

    x1,y1 = pygame.mouse.get_pos()
    gamedisplay.fill(DISPLAY_COLOR)
    gamedisplay.blit(background2, (0,-150))
    gamedisplay.blit(board1, (0,0))
    print(board1)
    gamedisplay.blit(prop, (1150,15))
    gamedisplay.blit(rescale(car, 0.07), (790,25))
    gamedisplay.blit(rescale(marker, 0.02), (x1,y1))
    pygame.display.update()




# Load the Game
Players = [Player("Ege", "Car"), Player("Kaleb", "Phone"), Player("Evan", "Horse")]
Game = Monopoly(Players)
print(Game.get_player(0).getPlayerName())
