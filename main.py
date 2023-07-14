# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Example file showing a basic pygame "game loop"
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

start_x = screen.get_width() / 2
start_y = screen.get_height() / 2
circle_radius = 120

circle_pos = pygame.Vector2( start_x, start_y)
move_y = 5
move_x = 8

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "red", circle_pos, circle_radius )

    # tutaj matma :D

    circle_pos.y += move_y
    circle_pos.x += move_x

    if circle_pos.y >= screen.get_height()-circle_radius:
        circle_pos.y = screen.get_height()-circle_radius
        move_y *= -1
    if circle_pos.y <= 0+circle_radius:
        circle_pos.y = 0+circle_radius
        move_y *= -1

    if circle_pos.x >= screen.get_width()-circle_radius:
        circle_pos.x = screen.get_width()-circle_radius
        move_x *=-1
    if circle_pos.x <= 0+circle_radius:
        circle_pos.x = 0+circle_radius
        move_x *=-1








    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print( 'hello!' )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
