import pygame
import sys 
import random

#define fixed variables

screen_height = 800
screen_width = 636

player_width = 50   
player_height = 50

player_y = 500
player_x = 250


base_y = 600
base_x = 200

base_y_1 = 200
base_x_1 = 200

base_y_2 = 400
base_x_2 = 200


base_width = 300
base_height = 20

##define gravity value 
gravity = 1
zero = 0


size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)


#name of the window
pygame.display.set_caption('my monkey game')



#define player  = monkey
class Monkey(pygame.sprite.Sprite):
    def __init__(self,x,y, speed):
        super().__init__()
        self.image = pygame.image.load('monkey.png')
        self.rect = self.image.get_rect()
       
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = gravity

    def update(self):
        self.rect.move_ip(0,int(gravity))

class Base(pygame.sprite.Sprite):
    def __init__(self,x,y,base_x, base_y):
        super().__init__()
        self.image = pygame.Surface((base_width,base_height))
        self.image.fill('#ffe135')
        self.rect = self.image.get_rect()
        self.rect.x = base_x
        self.rect.y = base_y

   
        

player = Monkey(player_x, player_y, gravity)
base=Base(base_width,base_height,base_x,base_y)
base1=Base(base_width,base_height,base_x_2,base_y_1)
base2=Base(base_width,base_height, base_x_2, base_y_2)


all_sprites = pygame.sprite.Group()

#initialize pygame
pygame.init()

#colco
clock = pygame.time.Clock()

#background
background_image = pygame.image.load("sky.jpg")
background_y = 0


#game conditions 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)



    

    #--------
    # introduce player collision with base & gravits
    # collision base bottom
    if player.rect.y+player_height>base.rect.y:
        player.rect.y-= 1
        print('collision_base')
        collision_base_2 = 1
    else: 
        collision_base_2= False
    #--------------
    #palyer collision left right 
    if player.rect.x+player_width<base.rect.x:
        player.rect.y +=4

    if player.rect.x>base.rect.x+base_width:
        player.rect.y +=4
    

    #-----------
    #collision base 2

    if player.rect.y+player_height== base2.rect.y:
        print('collision_base_2')
        collision_base_2=True
    else:
        collision_base_2==False

    if collision_base_2==True:
        player.rect.y -=1

    #---------------
    #collision base 1 
    if player.rect.y+player_height==base1.rect.y:
        collision_base_1=1
        collision_base_1=True
        print('collision_base_1')
    else:
        collision_base_1=False

    if collision_base_1==True:
        player.rect.y -=1

    
    #---------------
    # player movement A&D

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.rect.x -=3
        print('player_move_-x')



    if keys[pygame.K_d]:
        player.rect.x +=3
        print('player_move_x')   



    ## introduce jump mechanics
    if keys[pygame.K_SPACE]:
        # Scroll the background
        background_y += 5

        if background_y >= screen_height:
            background_y = 0

    # Draw background
       
        player.rect.y -=8



    screen.blit(background_image, (0, background_y))
    screen.blit(background_image, (0, background_y - screen_height))

    #screen.fill((255,255,255))

    screen.blit(player.image,player.rect)
    screen.blit(base.image, base.rect)
    screen.blit(base1.image, base1.rect)
    screen.blit(base2.image, base2.rect)
    player.update()
    base.update()
    base1.update()
    base2.update()

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
