import pygame
pygame.init()
pygame.font.init()

class GameText:
    def __init__(self, coordinates = (0,0), text = "DUMMY INPUT", font = pygame.font.SysFont("Arial", 50), color = (255,0,0)):
        text = font.render(text, True, color)
        self.text = text
        self.textRect = text.get_rect()
        self.textRect.center = coordinates

    def show(self, display):
        display.blit(self.text, self.textRect)


'''
def test_GameText():
    # Display
    DISPLAY_SIZE = (600, 400)
    DISPLAY_COLOR = (20, 20, 20)
    gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)

    # Texts
    start_text = GameText((200,100), "START GAME")
    options_text = GameText((200,150), "OPTIONS")
    exit_text = GameText((200,200), "EXIT GAME")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplay.fill(DISPLAY_COLOR)
        start_text.show(gamedisplay)
        options_text.show(gamedisplay)
        exit_text.show(gamedisplay)
        pygame.display.update()


test_GameText()
'''
