# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Example file showing a basic pygame "game loop"
import pygame
from rects import Rects

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

speed1 = [6 , 0]
rect_pos1 = pygame.Vector2(300, 300)
rect_1 = Rects(rect_pos1, 100, 100, speed1,  'red')

speed2 = [7,0]
rect_pos2 = pygame.Vector2(700, 300)
rect_2 = Rects(rect_pos2, 100, 100,speed2, 'blue')



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    rect_1.draw(screen)
    rect_2.draw(screen)


    if rect_1.collision(rect_2):
        rect_1.speed[0] = 0
    else:
        rect_1.move()
    if rect_1.speed[0]==0:
        rect_2.move()
        rect_2.update(screen)

    if rect_2.collision(rect_1) and rect_1.speed[0] ==0:
        rect_2.speed[0] = 0
        rect_1.speed[0] = -6

    if rect_2.speed[0]==0:
        rect_1.move()
        rect_1.update(screen)






    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hello!')
