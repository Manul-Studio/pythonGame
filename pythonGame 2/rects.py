import pygame

class Rects:

    def __init__(self, rect_pos, rect_width, rect_height, speed, color):
        self.rect_pos = rect_pos
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.speed= speed
        self.color = color

        self.rect = pygame.Rect(self.rect_pos, (self.rect_width, self.rect_height))

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def update(self, screen):
        if self.rect.x <= 0:
            self.speed[0] *= -1

        if self.rect.x >= screen.get_width()- self.rect_width:
            self.speed[0] *=-1


    def collision(self, other):
        return self.rect.colliderect(other.rect)




    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)