import pygame

BLACK= (0,0,0)
WHITE = (255, 255, 255)
GRAY=(128,128,128)
RED= (255,0,0)
Cell_size=60

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.x = col * Cell_size
        self.y = row * Cell_size
        self.original = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):

        #Font for regular value
        if self.value != 0:
            font = pygame.font.Font(None, 40)
            text = font.render(str(self.value), 0, BLACK)
            self.screen.blit(text, (self.x + 20, self.y + 15))
        #Sketched Value
        elif self.sketched_value != 0:
            font = pygame.font.Font(None, 20)
            text = font.render(str(self.sketched_value), 0, GRAY)
            self.screen.blit(text, (self.x + 5, self.y + 5))

        #Cell selected, draw a red boarder around it
        if self.selected:
            pygame.draw.rect(self.screen, RED, (self.x, self.y, Cell_size, Cell_size), 3)

