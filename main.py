# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Example file showing a basic pygame "game loop"
import pygame
from circle import Circle

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

circle_pos = pygame.Vector2(screen.get_height() /2,screen.get_height() /2)


circles = [Circle(120, circle_pos, pygame.Vector2(1,1)), Circle(120, circle_pos, pygame.Vector2(6,4)),
           Circle(120, circle_pos, pygame.Vector2(4,6))]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    for circle in circles:
        circle.update(screen)
        circle.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hello!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


'''
tablice zawierajace kola
i zrobic w petli update() i draw()'''
