import pygame
def rescale(img, scale):
    h1, w1 = img.get_size()
    img = pygame.transform.scale(img, (int(h1*scale), int(w1*scale)))
    return img
