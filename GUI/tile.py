import pygame

def rescale(image, scale):
    h1, w1 = image.get_size()
    image = pygame.transform.scale(image, (int(h1*scale), int(w1*scale)))
    return image

class Tile:
    def __init__(self, coordinates=(0,0)):

        # Default
        #self.tile1 =

        # Mouseover
        #self.tile2 =

        # Clicked
        #self.tile3 =

        # mouse over
        self.mouse_over = False

        # save coordinates (kinda redundant since we have rect)
        self.coordinates = coordinates

        # create another rec, since image.get_rect() does not update properly
        rect = image1.get_rect()
        rect.center = coordinates
        self.rect = rect

        # clicked
        self.clicked = False

    def info(self):
        print(self.coordinates, " image: ", self.image)

    def show(self, display):
        if not self.clicked:
            if not self.over():
                # defualt
                display.blit(self.tile1, self.rect)
            else:
                # mouseover
                display.blit(self.tile2, self.rect)
        else:
            # clicked
            display.blit(self.tile3, self.rect)

    def over(self):
        x,y = pygame.mouse.get_pos()
        return self.rect.collidepoint(x,y)



# display
DISPLAY_SIZE = (1440,770); DISPLAY_COLOR = (110,110,110)
gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("Property Tycoon")
board1 = pygame.image.load("GUI/board1.png")
prop = pygame.image.load("GUI/property1.jpg")
car = pygame.image.load("GUI/car.png")

board1 = Board()

'''
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")

    gamedisplay.fill(DISPLAY_COLOR)
    gamedisplay.blit(board1, (400,15))
    gamedisplay.blit(prop, (1150,15))
    gamedisplay.blit(rescale(car, 0.07), (790,25))
    pygame.display.update()


def rescale(img, scale):
    h1, w1 = img.get_size()
    img = pygame.transform.scale(img, (int(h1*scale), int(w1*scale)))
    return img

'''
