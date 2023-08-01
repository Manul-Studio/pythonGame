
import pygame
from rects import Rects

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

speed1 = [6 , 0]
rect_pos1 = pygame.Vector2(500, 300)
rect_1 = Rects(rect_pos1, 200, 200, speed1,  'blue')

speed2 = [-6,0]
rect_pos2 = pygame.Vector2(900, 300)
rect_2 = Rects(rect_pos2, 200, 200,speed2, 'green')


test_font = pygame.font.SysFont('Arial',50)


count = 0
def collision_rects():
    global count
    if rect_2.collision(rect_1):
        rect_2.speed[0] = 0
    else:
        rect_2.move()

    if rect_2.speed[0] == 0:
        rect_1.move()
        rect_1.update(screen)

    if rect_1.collision(rect_2) and rect_2.speed[0] == 0:
        rect_1.speed[0] = 0
        rect_2.speed[0] = 6
        rect_2.move()
        count+=1

    if rect_2.collision(rect_1) and rect_1.speed[0] == 0:
        rect_2.speed[0] = 0
        rect_1.speed[0] = -6
        rect_1.move()
def collision_count():
    counter_text = test_font.render("Collisions:" +str(count), True, (0, 0, 0))
    screen.blit(counter_text, (10, 10))

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
    collision_rects()
    collision_count()


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hello!')
