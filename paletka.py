import pygame


class Paletka:

    def __init__(self, width, height, color, rect_pos, move):
        self.width = width
        self.height = height
        self.color = color
        self.rect_pos = rect_pos
        self.move = move
        self.paletka = pygame.Rect(self.rect_pos, (self.width, self.height))

    def update_right(self, screen):

        k = pygame.key.get_pressed()
        if k[pygame.K_UP]:
            self.paletka.y -=self.move[1]
        if k[pygame.K_DOWN]:
            self.paletka.y +=self.move[1]

        if self.paletka.y >= screen.get_height()-self.height:
            self.paletka.y = screen.get_height()-self.height

        if self.paletka.y <= 0:
            self.paletka.y = 0

    def update_left(self, screen):

        k = pygame.key.get_pressed()
        if k[pygame.K_w]:
            self.paletka.y -= self.move[1]
        if k[pygame.K_s]:
            self.paletka.y += self.move[1]

        if self.paletka.y >= screen.get_height()-self.height:
            self.paletka.y = screen.get_height()-self.height

        if self.paletka.y <= 0:
            self.paletka.y = 0


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.paletka)
