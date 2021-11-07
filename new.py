import pygame
import time
# init pygame
pygame.init()
# draw window
win = pygame.display.set_mode((800,600))
# setting the fps or init the fps.
clock = pygame.time.Clock()
# load image
bullet=pygame.image.load("Bullet_1.png")
# funct to update the game window

class Bullets(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vel=5
        self.y_change=0
    def draw(self):
        win.blit(bullet, (self.x, self.y))

#speed=ds/dt
run = True
bullet_list =[]
x=0
y=40
a=1
go_up=False
go_down=True
no_of_frames=0
while run:
    clock.tick(30)
    win.fill((34, 177, 76))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y+=10
            if event.key== pygame.K_SPACE:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN  :
                y_c = 0
    #print(bullet_list)
    pygame.draw.circle(win, (0, 0, 0), (100, y), 20)
    hitbox = (200, 150, 400, 300)
    pygame.draw.rect(win, (0, 0, 0), hitbox)
    if y>=580:
        go_up=not go_up
        go_down=not go_down

        no_of_frames=0
    if y<=20:
        go_up = not go_up
        go_down = not go_down
        no_of_frames=0
    if not go_down and go_up:
        y-=a
    if go_down and not go_up:
        y+=a
    no_of_frames+=1
    pygame.display.update()
pygame.quit()

