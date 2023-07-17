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


circle = Circle(screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    circle.draw(screen)
    circle.update(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hello!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


'''jedyne co to start_x/y bym w ogole nie przechowywal
a jak juz chcial to tak samo jak pozycje czyli vector2
no i fajnie by było jak by Circle bylo w osobnym pliku
no i jak to sie ogarnie to
kolejna czesc zadania
to zrobic
tablice zawierajace kola
i zrobic w petli update() i draw()'''
