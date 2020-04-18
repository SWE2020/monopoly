import pygame
pygame.init()
pygame.font.init()

class GameText:
    def __init__(self, coordinates = (0,0), text = "DUMMY INPUT", color = (255,255,255), size=27):
        font = pygame.font.SysFont("sfnsdisplaycondensedblackotf", size)
        text = font.render(text, True, color)
        self.text = text
        self.textRect = text.get_rect()
        self.textRect.topleft = coordinates

    def show(self, display):
        display.blit(self.text, self.textRect)
