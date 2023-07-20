# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Example file showing a basic pygame "game loop"
import pygame
from circle import Circle
from paletka import Paletka
import copy

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

circle_pos = pygame.Vector2(screen.get_width(), screen.get_height())
circle_pos = circle_pos/2
width = 40
height = 40
circle = Circle(circle_pos, width, height, pygame.Vector2(15, 15), 'pink')

rect_pos_left = pygame.Vector2(0, screen.get_height()/2)
paletka_left = Paletka(30, 200, 'red', rect_pos_left, pygame.Vector2(0, 15))

rect_pos_right = pygame.Vector2(screen.get_width()-30, screen.get_height() /2)
paletka_right = Paletka(30, 200, 'blue', rect_pos_right, pygame.Vector2(0, 15))


test_font = pygame.font.SysFont('Arial',50)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    circle.update(screen)
    circle.collision(paletka_right, paletka_left)
    circle.draw(screen)
    circle.score_update(screen)

    circle.score_show(circle, test_font, screen)
    paletka_left.draw(screen)
    paletka_right.draw(screen)
    paletka_left.update_left(screen)
    paletka_right.update_right(screen)



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hello!')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


