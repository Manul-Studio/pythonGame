# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Example file showing a basic pygame "game loop"
import pygame
from circle import Circle
import random
import copy
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

circle_pos = pygame.Vector2(screen.get_width(), screen.get_height())
circle_pos = circle_pos/2


circles = []

circles.append(Circle(120, copy.copy(circle_pos), pygame.Vector2(5, 5), 'pink'))
circles.append(Circle(120, copy.copy(circle_pos), pygame.Vector2(-5, 5), 'pink'))
circles.append(Circle(120, copy.copy(circle_pos), pygame.Vector2(-5, -5), 'pink'))
circles.append(Circle(120, copy.copy(circle_pos), pygame.Vector2(5, -5), 'pink'))


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



