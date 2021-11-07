import pygame
import random
pygame.init()
win = pygame.display.set_mode((800, 600))
clock=pygame.time.Clock()
pallet=pygame.image.load("Bullet_1.png")
king_kong_reload=pygame.image.load("king_kong/king_kong_1.png")
king_kong_fire=pygame.image.load("king_kong/king_kong_fire.png")
king_kong_dead=[pygame.image.load("king_kong/king_kong_dead_1.png"),pygame.image.load("king_kong/king_kong_dead_1.png"),pygame.image.load("king_kong/king_kong_dead_1.png"),pygame.image.load("king_kong/king_kong_dead_2.png"),pygame.image.load("king_kong/king_kong_dead_2.png"),pygame.image.load("king_kong/king_kong_dead_2.png"),pygame.image.load("king_kong/king_kong_dead_3.png"),pygame.image.load("king_kong/king_kong_dead_3.png"),pygame.image.load("king_kong/king_kong_dead_3.png"),pygame.image.load("king_kong/king_kong_dead_3.png")]
king_kong=[pygame.image.load("king_kong/king_kong_walk_1.png"),pygame.image.load("king_kong/king_kong_walk_1.png"),pygame.image.load("king_kong/king_kong_walk_1.png"),pygame.image.load("king_kong/king_kong_walk_1.png"),pygame.image.load("king_kong/king_kong_walk_1.png"),pygame.image.load("king_kong/king_kong_walk_2.png"),pygame.image.load("king_kong/king_kong_walk_2.png"),pygame.image.load("king_kong/king_kong_walk_2.png"),pygame.image.load("king_kong/king_kong_walk_2.png"),pygame.image.load("king_kong/king_kong_walk_2.png")]
data=pygame.image.load("COMETS!!/Comet_1.png")
d={0:pygame.image.load("NUMS/0.png"),1:pygame.image.load("NUMS/1.png"),2:pygame.image.load("NUMS/2.png"),3:pygame.image.load("NUMS/3.png"),4:pygame.image.load("NUMS/4.png"),5:pygame.image.load("NUMS/5.png"),6:pygame.image.load("NUMS/6.png"),7:pygame.image.load("NUMS/7.png"),8:pygame.image.load("NUMS/8.png"),9:pygame.image.load("NUMS/9.png")}
#win.blit(self.comet_animation[i], (self.x, self.y))
class Node(object):
    def __init__(self,x,y,data):
        self.x=x
        self.y=y
        self.data=data
        self.next=None
class Linklist(object):
    def __init__(self):
        self.head=None
        self.pointer=None
    def insert(self,data,x,y):
        new_node=Node(x,y,data)
        new_node.next=self.head
        self.head=new_node
        pointer=self.head
        while pointer:
            pointer.x+=35
            pointer=pointer.next
    def display(self):
        displayer = self.head
        while displayer:
            win.blit(displayer.data, (displayer.x, displayer.y))
            prev = displayer.next
            displayer.data=None
            displayer.next=None
            displayer.x=0
            displayer.y=0
            displayer=prev
        self.head=displayer


class Pallets(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vel=4
        self.y_change=0
        self.hitbox=(self.x,self.y,28,18)
        self.upper_diagonal=False
        self.lower_diagonal=False
        self.if_collided=False
    def draw(self,pause,game_over):
        win.blit(pallet, (self.x, self.y))
        self.hitbox = (self.x, self.y, 20, 18)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        if not pause and not game_over:
            if self.upper_diagonal:
                self.y-=2
                self.x -= self.vel
            elif self.lower_diagonal:
                self.y+=2
                self.x -= self.vel
            else:
                self.x -= self.vel



# if x== some coordinate
# stop the x coordinate count and change the y coordinate
# if y coordinate> some value decrease
# elif y coor <some val increase
class Bullets(object):
    def __init__(self,x,y):
        self.x=x
        self.x_change=5
        self.y=y
        self.go_up=True
        self.go_down=False
        self.fire=False
        self.reload=False
        self.king_fire=king_kong_fire
        self.projectile=king_kong
        self.k_reload=king_kong_reload
        self.kongs_bullets=[]
        self.pause=False
        self.game_over=False
        self.kong_fall=False
        self.proceed=False
        self.vel_fall=0
        self.kong_lives=100
        self.i=0
        self.hitbox = (self.x, self.y, 28, 40)

        #pygame.image.load("Bullet_1.png")
    # this method is to draw kong and not bullets, running out of names here:(
    def draw_bullet(self,x,y,i):
        win.blit(self.projectile[i], (x,y))
    # method to display kong is firing
    def fire_kong(self):
        win.blit(self.king_fire,(self.x,self.y))

    # method to display reloading kong sprite
    def reload_kong(self,x,y):
        win.blit(self.k_reload, (x, y))
    def pause_kong(self):
        if self.i>9:
            self.i=0
        if not self.fire and not self.reload:
            win.blit(self.projectile[self.i], (self.x, self.y))
        if self.fire and not self.reload:
            self.fire_kong()
        if self.reload and not self.fire:
            self.reload_kong(self.x,self.y)
    def draw_sprite(self):
        if self.i>9:
            self.i=0
        if self.game_over==True:
            win.blit(self.projectile[self.i], (self.x, self.y))
        # set game over false
        if self.x>400:
            win.blit(self.projectile[self.i], (self.x, self.y))
            if not self.pause:
                self.x-=self.x_change
        elif self.x<=400:
            if self.y>=350:
                self.go_up=True
                self.go_down=False
            if self.y<=0:
                self.go_down=True
                self.go_up=False
            if self.go_down and not self.fire and not self.reload and not self.pause and not self.game_over and self.kong_lives>0 :
                self.y+=self.x_change
            if self.go_up and not self.fire and not self.reload and not self.pause and not self.game_over and self.kong_lives>0:
                self.y-=self.x_change
            if self.fire and not self.reload and self.kong_lives>0:
                self.fire_kong()
            elif not self.reload and self.kong_lives>0:
                self.draw_bullet(self.x,self.y,self.i)
            elif self.reload and not self.game_over and self.kong_lives>0:
                self.reload_kong(self.x,self.y)
            self.hitbox = (self.x, self.y, 250, 250)
            #pygame.draw.rect(win, (100, 70, 0), self.hitbox, 2)
            if self.kong_lives<=0:
                #self.kongs_bullets.clear()
                if not self.kong_fall:
                    if self.y<2:
                        self.kong_fall=True
                    self.y-=5
                if self.kong_fall:
                    self.y+=self.vel_fall
                    self.vel_fall+=1
                if self.y<610:
                    win.blit(king_kong_dead[self.i], (self.x, self.y))
                elif self.y>=600:
                    self.proceed=True
        if not self.pause and not self.game_over:
            self.i+=1

    def fire_bullets(self,x):
        P=Pallets(self.x, self.y + 125)
        x_b=random.randint(10,100)
        if x==x_b:
            self.kongs_bullets.append(P)






