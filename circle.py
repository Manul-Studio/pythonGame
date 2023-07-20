import pygame


class Circle:

    def __init__(self, circle_pos, width, height, move, color):
        self.circle_pos = circle_pos
        self.move = move
        self.color = color
        self.width = width
        self.height = height
        self.ball = pygame.Rect(circle_pos, (self.width, self.height))
        self.score_l = 0
        self.score_r = 0

    def score_update(self,screen):
        if self.ball.x >= screen.get_width() - self.width:
            self.score_l +=1

        if self.ball.x <=0:
            self.score_r += 1

    def score_show(self, circle, test_font, screen):
        score_left = str(circle.score_l)
        score_left = test_font.render('Player 1:' + score_left, True, 'Black')
        screen.blit(score_left, (300, 0))

        score_right = str(circle.score_r)
        score_right = test_font.render('Player 2:' + score_right, True, 'Black')
        screen.blit(score_right, (750, 0))

    def update(self, screen):
        self.ball.y += self.move[1]
        self.ball.x += self.move[0]


        if self.ball.y >= screen.get_height() - self.height:
            self.ball.y = screen.get_height() - self.height

            self.move[1] *= -1
        if self.ball.y <= 0:
            self.ball.y = 0

            self.move[1] *= -1

        if self.ball.x >= screen.get_width() - self.width:
            self.ball.x = screen.get_width() - self.width

            self.move[0] *= -1

        if self.ball.x <= 0:
            self.ball.x = 0

            self.move[0] *= -1

    def collision(self, paletka_right, paletka_left):

        if self.ball.colliderect(paletka_right.paletka) or self.ball.colliderect(paletka_left.paletka):
            self.move[0] *= -1



    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.ball)