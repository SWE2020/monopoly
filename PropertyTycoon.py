import sys
sys.path.append('/Users/egeersu/Desktop/monopoly/GUI')
print(sys.path)

from intro import *
from Board import *
from Monopoly import *

# Play the intro, save number of players
pygame.init()
#num_players = game_intro()
num_players = 2
print(num_players)


# Token Screen

# Load the Game
Players = [Player("Ege", "Car"), Player("Kaleb", "Phone"), Player("Evan", "Horse")]
Game = Monopoly(Players)
