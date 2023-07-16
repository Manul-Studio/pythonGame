# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Example file showing a basic pygame "game loop"
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


class Circle:

    def __init__(self):
        self.circle_radius = 120
        self.start_x = screen.get_width() / 2
        self.start_y = screen.get_width() / 2
        self.circle_pos = pygame.Vector2(self.start_x, self.start_y)
        self.move = pygame.Vector2(8,5)

    def update(self):
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

    def draw(self):
        pygame.draw.circle(screen, 'red', self.circle_pos, self.circle_radius)


circle = Circle()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    circle.draw()
    circle.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hello!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


'''A jesteś w stanie move przerobić na vector2 z pyGame
I potem spróbować stworzyć klase reprezentująca okrąg?
Musi mieć dwie metody (może więcej)
Ale potrzebował bym metody update() w której by było liczone gdzie okrąg ma być
Oraz metody draw() która narysowała by okrąg w pozycji zaktualizowanej po działaniu update()'''
