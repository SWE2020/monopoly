import sys
sys.path.append('/Users/egeersu/Desktop/monopoly/GUI')

import pygame
from intro import *
from Monopoly import *


# Music
pygame.init()
pygame.mixer.music.load("GUI/game_music.ogg")
pygame.mixer.music.play(-1)

# Play the intro, save number of players
num_players = game_intro()
#num_players = 2
#print(num_players)

# display
DISPLAY_SIZE = (1440,770); DISPLAY_COLOR = (110,110,110)
gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("Property Tycoon")
#board1 = pygame.image.load("GUI/board1.png")
#prop = pygame.image.load("GUI/property1.jpg")
#car = pygame.image.load("GUI/car.png")


# Load the Game
Players = [Player("Ege", "Car"), Player("Kaleb", "Phone"), Player("Evan", "Horse")]
Game = Monopoly(Players)
print(Game.get_player(0).getPlayerName())
