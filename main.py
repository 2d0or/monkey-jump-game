import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((636, 800))
pygame.display.set_caption("Monkey Game")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)




def play():
    while True:
        #PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        import pygame
        import sys 
        import random   

        #define fixed variables

        screen_height = 800
        screen_width = 636

        player_width = 50   
        player_height = 50

        player_y = 200
        player_x = 250


        base_y = 600
        base_x = 150

        base_y_1 = 150
        base_x_1 = 150

        base_y_2 = 300
        base_x_2 = 150


        base_width = 300
        base_height = 20

    ##define gravity value 
        gravity = 4
        zero = 0
        gravity_base = 3


        size = (screen_width, screen_height)
        screen = pygame.display.set_mode(size)


    #name of the window
        pygame.display.set_caption('Monkey Game')



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
            def __init__(self,x,y,base_x, base_y, speed):
                super().__init__()
                self.image = pygame.Surface((base_width,base_height))
                self.image.fill('#ffe135')
                self.rect = self.image.get_rect()
                self.rect.x = base_x
                self.rect.y = base_y
                self.speed = gravity_base

            def update(self):
                self.rect.move_ip(0,int(gravity_base))

        
                

        player = Monkey(player_x, player_y, gravity)
        base = Base(base_height, base_width, base_x, base_y, gravity_base)
        base1=Base(base_width,base_height,base_x_2,base_y_1,gravity_base)
        base2=Base(base_width,base_height, base_x_2, base_y_2, gravity_base)


        all_sprites = pygame.sprite.Group()

        #initialize pygame
        pygame.init()

        #colco
        clock = pygame.time.Clock()

        #background
        background_image = pygame.image.load("sky1.png")
        background_y = 0
        keys = pygame.key.get_pressed()
        #game conditions 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
            clock.tick(60)


            #### falling off the map --> break
            if player.rect.y+player_height>screen_height:
                main_menu()
            
            if player.rect.y<0:
                print('sky')
                main_menu()

            if keys[pygame.K_ESCAPE]:
                print('Space')
                main_menu()
                

            #--------
            # introduce player collision with base & gravits
            # collision base bottom
            if player.rect.y+player_height==base.rect.y:
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
            # if player.rect.y+player_height==base1.rect.y:

                    # Scroll the background
                    print('jump')
                    background_y += 5

                    if background_y >= screen_height:
                        background_y = 0
                    player.rect.y -=8
            
         

            if base.rect.y+base_height==screen_height:
                base.rect.y =0
            
            if base1.rect.y+base_height ==screen_height:
                base1.rect.y=0

            if base2.rect.y+base_height ==screen_height:
                base2.rect.y = 0

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


            pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(15).render("Nothing here yet.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(350, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(300, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    SCREEN.fill('White')
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        keys = pygame.key.get_pressed()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(60).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(300, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(320, 400), 
                            text_input="OPTIONS", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(300, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        

          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                print('mouse_button_down')
            if keys[pygame.K_SPACE]:
                print('Space')
                play()
            
            if keys[pygame.K_ESCAPE]:
                sys.exit()
        pygame.display.update()


main_menu()

