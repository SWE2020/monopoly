import pygame

def rescale(image, scale):
    h1, w1 = image.get_size()
    image = pygame.transform.scale(image, (int(h1*scale), int(w1*scale)))
    return image

class Button:
    def __init__(self, coordinates=(0,0), image1=None, image2=None, image3=None, scale=1):
        # Default Image
        image1 = pygame.image.load(image1)
        image1 = rescale(image1, scale)
        self.image1 = image1

        # Mouse over image
        image2 = pygame.image.load(image2)
        image2 = rescale(image2, scale)
        self.image2 = image2

        # Clicked Image
        image3 = pygame.image.load(image3)
        image3 = rescale(image3, scale)
        self.image3 = image3

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

        #mode
        self._mode = 0

    def info(self):
        print(self.coordinates, " image: ", self.image)

    def mode_switch(self):
        if self._mode == 0:
            self._mode = 1
        else:
            self._mode = 0

    def show(self, display):
        if not self.clicked:
            if self.over():
                # mouse over image
                display.blit(self.image2, self.rect)
            else:
                # standard image
                display.blit(self.image1, self.rect)
        else:
            # clicked image
            display.blit(self.image3, self.rect)

    def show2(self, display):
        if self._mode == 0:
            display.blit(self.image1, self.rect)
        else:
            display.blit(self.image2, self.rect)

    def over(self):
        x,y = pygame.mouse.get_pos()
        return self.rect.collidepoint(x,y)

    def flip(self):
        temp = self.image1
        self.image1 = self.image3
        self.image2 = self.image3
        self.image3 = temp

    def hide(self):
        self.image1.set_alpha(0)
        self.image2.set_alpha(0)
        self.image3.set_alpha(0)

    def unhide(self):
        self.image1.set_alpha(255)
        self.image2.set_alpha(255)
        self.image3.set_alpha(255)



'''
TEST
# buttons
button1 = Button((50,50), "play1.png", 0.4)

# display
DISPLAY_SIZE = (700,400); DISPLAY_COLOR = (5,5,5)
gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('Main Menu')

# mouse
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if button1.over():
                print("yes")
            else:
                print("no")

    gamedisplay.fill(DISPLAY_COLOR)
    button1.show(gamedisplay)
    pygame.display.update()
'''
