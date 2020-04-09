import pygame

# Rescales an image with a given number
def rescale(img, scale):
    h1, w1 = img.get_size()
    img = pygame.transform.scale(img, (int(h1*scale), int(w1*scale)))
    return img

# Images could be fields of the Property class
# We can simply call display_property(property.image) once the mouse is hovered over a tile.
prop0 = pygame.image.load("property1.jpg")
prop1 = pygame.image.load("property1.jpg")
prop2 = pygame.image.load("property1.jpg")
prop3 = pygame.image.load("property1.jpg")
prop4 = pygame.image.load("property1.jpg")
prop5 = pygame.image.load("property1.jpg")
prop6 = pygame.image.load("property1.jpg")
prop7 = pygame.image.load("property1.jpg")
prop8 = pygame.image.load("property1.jpg")
prop9 = pygame.image.load("property1.jpg")
prop10 = pygame.image.load("property1.jpg")
prop11 = pygame.image.load("property1.jpg")
prop12 = pygame.image.load("property1.jpg")
prop13 = pygame.image.load("property1.jpg")
prop14 = pygame.image.load("property1.jpg")
prop15 = pygame.image.load("property1.jpg")
prop16 = pygame.image.load("property1.jpg")
prop17 = pygame.image.load("property1.jpg")

properties = [prop0, prop1, prop2, prop3, prop4, prop5, prop6, prop7, prop8, prop9, prop10, prop11, prop12, prop13, prop14, prop15, prop16, prop17]

# displays the i-th property on the property
def display_image(display, i, scale):
    x = 10
    y = 10
    scale = 1
    prop = properties[i]
    prop = rescale(prop, scale)
    display.blit(prop, (x,y))
