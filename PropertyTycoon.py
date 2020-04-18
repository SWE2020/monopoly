#from Name_Selection import *
#from Monopoly import *
import pygame
import GUI
pygame.init()

# Music
#pygame.mixer.music.load("soundtrack.mp3")
#pygame.mixer.music.play(-1)

# Play the intro, save number of players
num_players = GUI.game_intro()
#num_players = 3

# Player Name Selection
Player_Names = GUI.select(num_players)
#Player_Names = ["Ege", "Deniz", "Elif"]

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
