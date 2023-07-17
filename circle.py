import pygame


class Circle:

    def __init__(self, screen):
        self.circle_radius = 120
        self.circle_pos = pygame.Vector2(screen.get_width() / 2, screen.get_width() / 2)
        self.move = pygame.Vector2(8,5)

    def update(self, screen):
        self.circle_pos.y += self.move[1]
        self.circle_pos.x += self.move[0]

        if self.circle_pos.y >= screen.get_height() - self.circle_radius:
            self.circle_pos.y = screen.get_height() - self.circle_radius

            self.move[1] *= -1
        if self.circle_pos.y <= 0 + self.circle_radius:
            self.circle_pos.y = 0 + self.circle_radius

            self.move[1] *= -1

        if self.circle_pos.x >= screen.get_width() - self.circle_radius:
            self.circle_pos.x = screen.get_width() - self.circle_radius

            self.move[0] *= -1
        if self.circle_pos.x <= 0 + self.circle_radius:
            self.circle_pos.x = 0 + self.circle_radius

            self.move[0] *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, 'red', self.circle_pos, self.circle_radius)
