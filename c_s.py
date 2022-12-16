import pygame
import random
import exp
# initialize
pygame.init()
# set the game window
win = pygame.display.set_mode((800, 600))
# fps setting
clock = pygame.time.Clock()
# Projectile
bullet = pygame.image.load("Bullet_1.png")
# load welcome screen
wel=pygame.image.load("welcome.png")
# score numbers
d={0: pygame.image.load("NUMS/0.png"), 1: pygame.image.load("NUMS/1.png"), 2: pygame.image.load("NUMS/2.png"), 3: pygame.image.load("NUMS/3.png"), 4: pygame.image.load("NUMS/4.png"), 5: pygame.image.load("NUMS/5.png"), 6: pygame.image.load("NUMS/6.png"), 7: pygame.image.load("NUMS/7.png"), 8: pygame.image.load("NUMS/8.png"), 9: pygame.image.load("NUMS/9.png")}
# game over
g_o = pygame.image.load("PAUSE/game_over.png")
# Player object properties
class Player(object):
    def __init__(self, x, y, player_yc):
        self.x = x
        self.y = y
        self.player_yc=player_yc
        self.level_up=0
        self.game_over=False
        # the player animating array!
        self.player_animation=[pygame.image.load("Player_1.png"),pygame.image.load("Player_2.png"),pygame.image.load("Player_3.png"),pygame.image.load("Player_4.png"),pygame.image.load("Player_5.png"),pygame.image.load("Player_6.png"),pygame.image.load("Player_7.png")]
        self.hitbox = (self.x, self.y, 28, 18)
        #pygame.draw.rect(win,(255,200,0),self.hitbox,2)
    def draw(self,i):
        #self.game_over=not self.game_over
        win.blit(self.player_animation[i], (self.x, self.y))
        self.hitbox = (self.x+6, self.y+9, 60, 40)
        #pygame.draw.rect(win, (255, 200, 0), self.hitbox, 2)
#bullet object
class Bullets(object):
    def __init__(self,x,y,level_up):
        self.x=x
        self.y=y
        self.vel=5+level_up
        self.if_collided=False
        self.y_change=0
        self.hitbox=(self.x,self.y,28,18)
    def draw(self):
        win.blit(bullet, (self.x, self.y))
        self.hitbox = (self.x, self.y, 20, 18)
        #pygame.draw.rect(win,(255,200,0),self.hitbox,2)


# comet object
class Comet(object):
    def __init__(self,x,y,level_up):
        self.x=x
        self.y=y
        self.level_up=1
        self.x_change=4+level_up
        self.comet_animation=[pygame.image.load("COMETS!!/Comet_1.png"),pygame.image.load("COMETS!!/Comet_2.png"),pygame.image.load("COMETS!!/Comet_3.png"),pygame.image.load("COMETS!!/Comet_4.png"),pygame.image.load("COMETS!!/Comet_5.png"),pygame.image.load("COMETS!!/Comet_6.png"),pygame.image.load("COMETS!!/Comet_7.png")]
        self.hitbox = (self.x, self.y+9, 28, 40)
    def draw_comet(self,i):
        win.blit(self.comet_animation[i], (self.x, self.y))
        self.hitbox = (self.x, self.y+9, 28, 40)
       # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


# score board
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
        new_node = Node(x, y, data)
        #new_node=Node(5,-9,data)
        new_node.next=self.head
        self.head=new_node
        pointer=self.head
        while pointer:
            pointer.x+=35
            pointer=pointer.next
    # this method is not used
    def display1(self):
        displayer=self.head
        while displayer:
            win.blit(displayer.data,(displayer.x,displayer.y))
            displayer=displayer.next
    # this method is not used
    def delete(self):
        curr=self.head
        while curr:
            prev=curr.next
            curr.data=None
            curr.next=None
            curr.x=0
            curr.y=0
            curr=prev
        self.head=curr

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

# for collision detection
def if_collision(comet,bullet,bool):
    y=random.randint(45, 550)
    comet_array.pop(comet_array.index(comet))
    if not bool:
        comet_array.append(Comet(880,y+20,P.level_up))
    bullet_list.pop(bullet_list.index(bullet))

def respawn_comets(level):
    x_of_comet=0
    for pi in range(4):
        y_of_comet = random.randint(45, 550)
        comet_array.append(Comet(800 + x_of_comet, y_of_comet, level))
        x_of_comet += 100

# welcome screen
def welcome():
    run_w=True
    while run_w:
        clock.tick(30)
        win.fill((0, 0, 0))
        win.blit(wel, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    with open("high_score_base", "w") as f:
                        f.write(str(0))
                if event.key==pygame.K_SPACE or event.key==pygame.K_p:
                    return True
        pygame.display.update()
y22 = random.randrange(0, 200, 5)
# pause menu
def pause(high_score,i_p):
    # ik its spelled menu
    pause_animator=[pygame.image.load("PAUSE/pause_menue3.png"),pygame.image.load("PAUSE/pause_menue3.png"),pygame.image.load("PAUSE/pause_menue3.png"),pygame.image.load("PAUSE/pause_menue2.png"),pygame.image.load("PAUSE/pause_menue2.png"),pygame.image.load("PAUSE/pause_menue2.png"),pygame.image.load("PAUSE/pause_menue1.png"),pygame.image.load("PAUSE/pause_menue1.png"),pygame.image.load("PAUSE/pause_menue1.png"),pygame.image.load("PAUSE/pause_menue.png"),pygame.image.load("PAUSE/pause_menue.png"),pygame.image.load("PAUSE/pause_menue.png")]
    win.blit(pause_animator[i_p], (200, 150))
    # high score display
    temp = high_score
    if high_score == 0:
        win.blit(d[0], (230, 340))
    while temp > 0:
        LL.insert(d[temp % 10], 190,340)
        temp = temp // 10
    LL.display()
# to save high score
def high_score():
    with open("high_score_base","r") as f:
        return f.read()
# kong is sleeping
e1 = exp.Bullets(850, 100)
# to spawn the first 6 comets
comet_array=[]
x_of_comet=0
#y_gap=0
for pi in range(4):
    y_of_comet=random.randint(45,550)
    comet_array.append(Comet(800+x_of_comet,y_of_comet,0))
    x_of_comet+=100
# initialise linklist
LL=Linklist()
# running the game
run=welcome()
# player animation array pointer
i=0
# bullet list to display multiple bullets
bullet_list =[]
# player class variable
P=Player(10,50,0)
# to pause
paused=False
i_p=0
# initilizing the bullet sprite coordinates
x,y=65,31
#init the score
score=0
aux_score=0
# to display kong
disp_kong=False
# temp
#font=pygame.font.SysFont("",30,True)
# main game loop
while run:
    # fps setter
    clock.tick(30)
    if aux_score==300:
        aux_score=0
        e1 = exp.Bullets(850, 100)
        disp_kong=True
    # filling the window
    win.fill((34, 177, 76))
    # to loop through the player animation game sprite animation
    if i>=7:
        i=0
    try:
        highestscore=int(high_score())
    except:
        highestscore=0
    # loop to get the key events from pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not paused and not P.game_over:
                P.player_yc = -(5+P.level_up)
            if event.key == pygame.K_DOWN and not paused and not P.game_over:
                P.player_yc = 5+P.level_up
            if event.key== pygame.K_SPACE:
                if not paused:
                    y = P.y + 22
                    bullet_list.append(Bullets(x,y,P.level_up))
                else:
                    paused=not paused
                if P.game_over:
                    if disp_kong:
                        disp_kong=not disp_kong
                        #e1.x = 850
                        #e1.y=100
                        #e1.game_over=False
                    P.x = 10
                    P.y = 50
                    score = 0
                    aux_score=0
                    P.level_up=0
                    # comet_array.clear()
                    # bullet_list.clear()
                    comet_array=[]
                    bullet_list=[]
                    x_of_comet = 0
                    # y_gap=0
                    respawn_comets(0)
                    P.game_over=not P.game_over
            # for pause menu
            if event.key==pygame.K_p and not P.game_over:
                P.player_yc = 0
                paused=not paused
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                P.player_yc = 0
    # the movement of the player on y axis
    P.y += P.player_yc
    # bullets
    for bull in bullet_list:
        if bull.x < 790 and bull.x >= 65 and bull.if_collided==False:
            bull.draw()
            if not paused and not P.game_over:
                bull.x+=bull.vel
        else:
            bullet_list.pop(bullet_list.index(bull))
           #del bull

    # movement limit for the player sprite
    if P.y <= 50:
        P.y = 50
    elif P.y >= 550:
        P.y = 550
    # to blit the player sprite
    #win.blit(P.player_animation[i], (P.x, P.y))
    P.draw(i)
    # to display the comets in the comet array
    for ccc in comet_array:
        y_of_comet = random.randint(45, 550)
        if ccc.x>-10 and ccc.hitbox[1]+ccc.hitbox[3]<600:
            ccc.draw_comet(i)
            if not paused and not P.game_over:
                ccc.x-=ccc.x_change
        else:
            comet_array.pop(comet_array.index(ccc))
            if not disp_kong:
                comet_array.append(Comet(830,y_of_comet,P.level_up))
    # for collision of player bullet and comet
    for co in comet_array:
        for bb in bullet_list:
            if bb.hitbox[1]<co.hitbox[1]+co.hitbox[3] and bb.hitbox[1]+bb.hitbox[3]>co.hitbox[1]:
                if bb.hitbox[0]+bb.hitbox[2]>co.hitbox[0]:
                    if_collision(co, bb,disp_kong)
                    score+=1
                    if aux_score<=300:
                        aux_score+=1
    # collision of player with comet
    for co1 in comet_array:
        if P.hitbox[1] < co1.hitbox[1] + co1.hitbox[3] and P.hitbox[1] + P.hitbox[3] > co1.hitbox[1]:
            if P.hitbox[0] + P.hitbox[2] > co1.hitbox[0]:
                P.game_over=True
                #print(life)
    if disp_kong and len(comet_array)==0:
        e1.draw_sprite()
        # auto bullet fire for kong
        if ((e1.x == 400 and e1.y == y22) or (e1.x == 400 and e1.y == y22+100)) and not P.game_over and len(e1.kongs_bullets)<=3 and e1.kong_lives>0:
            P0 = exp.Pallets(e1.x, e1.y + 125)
            P0.upper_diagonal = True
            e1.kongs_bullets.append(P0)
            P1 = exp.Pallets(e1.x, e1.y + 125)
            P1.lower_diagonal = True
            e1.kongs_bullets.append(P1)
            P2 = exp.Pallets(e1.x, e1.y + 125)
            e1.kongs_bullets.append(P2)
            y22=random.randrange(0, 200, 5)
            e1.fire_kong()
        for bull in e1.kongs_bullets:
            if (bull.x < 490 and bull.x >= 5) and (bull.y < 600 and bull.y >= 50):
                bull.draw(paused,P.game_over)
            else:
                e1.kongs_bullets.pop(e1.kongs_bullets.index(bull))
        # kongs bullets colliding with player
        for k_b in e1.kongs_bullets:
            if P.hitbox[1] < k_b.hitbox[1] + k_b.hitbox[3] and P.hitbox[1] + P.hitbox[3] > k_b.hitbox[1]:
                if P.hitbox[0] + P.hitbox[2] > k_b.hitbox[0]:
                    P.game_over = True
                    e1.game_over=True
                    e1.kongs_bullets.clear()
        # detect collision of player bullet and kongs bullets
        for co1 in bullet_list:
            for bb1 in e1.kongs_bullets:
                if bb1.hitbox[1] < co1.hitbox[1] + co1.hitbox[3] and bb1.hitbox[1] + bb1.hitbox[3] > co1.hitbox[1]:
                    if bb1.hitbox[0] + bb1.hitbox[2] > co1.hitbox[0] and bb1.hitbox[0] < co1.hitbox[0] + co1.hitbox[2]:
                        bb1.if_collided = True
                        co1.if_collided = True
        # to detect collided bullets on kong
        for h_k in bullet_list:
            if e1.hitbox[1] < h_k.hitbox[1] + h_k.hitbox[3] and e1.hitbox[1] + e1.hitbox[3] > h_k.hitbox[1]:
                if e1.hitbox[0] + e1.hitbox[2] > h_k.hitbox[0] and e1.hitbox[0] < h_k.hitbox[0] + h_k.hitbox[2]:
                    if e1.x<=400:
                        # reduce kongs life
                        e1.kong_lives -= 1
                    # set collided bullets as true
                    h_k.if_collided=True
        # remove collided bullets
        #for i_i in bullet_list:
         #   if i_i.if_collided == True:
          #      bullet_list.pop(bullet_list.index(i_i))
        # remove collided bullets
        for j_j in e1.kongs_bullets:
            if j_j.if_collided==True:
                e1.kongs_bullets.pop(e1.kongs_bullets.index(j_j))
        if e1.proceed:
            disp_kong=False
            #aux_score=0
            P.level_up+=2
            score+=100
            e1.proceed=not e1.proceed
            respawn_comets(P.level_up)


        if paused:
            e1.pause=True
        else:
            e1.pause=False
    #text=font.render("SCORE "+str(score),True,(0,0,0))
    #win.blit(text,(70,70))
    # to display kong or to wake sleeping kong

    # score board counter
    # to make a copy of the score for processing
    temp = score
    if score == 0:
        win.blit(d[0], (35, -9))
    while temp > 0:
        LL.insert(d[temp % 10],5,-9)
        temp = temp // 10
    # display the score digits
    LL.display()
    # refresh aka deleting thy link list
    #LL.delete()
    if highestscore<score:
        highestscore=score
    with open("high_score_base","w") as f:
        f.write(str(highestscore))
    #text = font.render("SCORE " + str(highestscore), True, (0, 0, 0))
    #win.blit(text, (600, 60))
    # incrementing the player sprite array pointer
    if paused:
        if i_p>11:
            i_p=0
        pause(highestscore,i_p)
        i_p+=1
    if not paused and not P.game_over:
        i +=1
    # update the window!!
    if P.game_over:
        win.blit(g_o, (200, 150))
        P.player_yc = 0
    pygame.display.update()
