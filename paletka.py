import pygame

class Paletka:

    def __init__(self, width, height, color, rect_pos, move):
        self.width = width
        self.height = height
        self.color = color
        self.rect_pos = rect_pos
        self.move = move
        self.paletka = pygame.Rect(self.rect_pos, (self.width, self.height))

    def update(self,screen):
        self.paletka.y += self.move

        if self.paletka.y >= screen.get_height()-self.height:
            self.paletka.y = screen.get_height()-self.height

            self.move*= -1

        if self.paletka.y <= 0:
            self.paletka.y = 0

            self.move*= -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.paletka)

