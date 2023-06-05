import pygame, sys
from button import Button
pygame.init()

SCREEN = pygame.display.set_mode((636, 800))
pygame.display.set_caption("Monkey Game")

BG = pygame.image.load("assets/Background.png")



def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font1.ttf", size)



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


        base_y = 576
        base_x = 150

        base_y_1 = 192
        base_x_1 = 150

        base_y_2 = 384
        base_x_2 = 150

        base_width = 200
        base_height = 20

        banana_width = 30
        banana_height=30
        banana_x=200
        banana_y=100
        gravity_banana=3
        ##define gravity value 1
        gravity = 4
        zero = 0
        gravity_base = 3
        green = (225,225,225)
        
      
                            
        size = (screen_width, screen_height)
        screen = pygame.display.set_mode(size)


        #name of the window
        pygame.display.set_caption('Monkey Game')

        class Base(pygame.sprite.Sprite):
            def __init__(self, width, height, speed):
                super().__init__()
                self.image = pygame.Surface((base_width,base_height))
                self.image.fill('#ffe135')
                self.rect = self.image.get_rect()
                self.rect.x = base_x
                self.rect.y = base_y
                self.speed = gravity_base
                

            
            def update(self):
                self.rect.move_ip(0, gravity_base)
                if self.rect.y >= screen_height:
                    self.rect.y = -self.rect.height
                    self.rect.x = random.randint(50, 500)
                
            

        class Base1(pygame.sprite.Sprite):
            def __init__(self, width, height, speed):
                super().__init__()
                self.image = pygame.Surface((base_width,base_height))
                self.image.fill('#ffe135')
                self.rect = self.image.get_rect()
                self.rect.x = base_x_1
                self.rect.y = base_y_1
                self.speed = gravity_base

            


            def update(self):
                self.rect.move_ip(0, gravity_base)
                if self.rect.y >= screen_height:
                    self.rect.y = -self.rect.height
                    self.rect.x = random.randint(50, 500)
                    

        class Base2(pygame.sprite.Sprite):
            def __init__(self, width, height,speed):
                super().__init__()
                self.image = pygame.Surface((base_width,base_height))
                self.image.fill('#ffe135')
                self.rect = self.image.get_rect()   
                self.rect.x = base_x_2
                self.rect.y = base_y_2
                self.speed = gravity_base
        
            def update(self):
                self.rect.move_ip(0, gravity_base)
                if self.rect.y +base_height> screen_height:
                    self.rect.y = -self.rect.height
                    self.rect.x = random.randint(50, 500)
                



        class Monkey(pygame.sprite.Sprite):
            def __init__(self, x, y, speed):
                super().__init__()

                self.images = [pygame.image.load('monkey.png'), pygame.image.load('monkey1.png')]
                self.index = 0
                self.image = self.images[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = player_x
                self.rect.y = player_y
                self.speed = speed
                self.space_pressed = False  # Flag to track space bar state

            def update(self):
                if self.space_pressed:
                    self.index = 1
                else:
                    self.index = 0

                self.image = self.images[self.index]
                self.rect.move_ip(0, self.speed)

            def set_space_pressed(self, pressed):
                self.space_pressed = pressed


            
        banana_collected = 0
        class banana(pygame.sprite.Sprite):
            def __init__(self,x,y,width,height,speed):
                super().__init__()
                self.image = pygame.Surface((banana_width, banana_height))
                self.image.fill('#FFFF00')
                self.rect = self.image.get_rect()
                self.rect.x = banana_x
                self.rect.y = banana_y
                self.speed=gravity_banana
                
                           

            def update(self):
                self.rect.move_ip(0,gravity_banana)
                if player.rect.colliderect(banana.rect):
                    print('banana_collected')
                    banana.rect.y = -100
                    banana.rect.x = random.randint(50,500)
                    screen.blit(banana_text, banana_text_rect)

                    
                    
                        
    
        player = Monkey(player_x, player_y, gravity)
        base = Base(base_width,base_height, gravity_base)
        base1=Base1(base_width,base_height,gravity_base)
        base2=Base2(base_width,base_height, gravity_base)
        banana=banana(banana_width,banana_height,banana_x,banana_y,gravity_banana)
        all_sprites = pygame.sprite.Group(player, base, base1, base2, banana)  # Add banana to all_sprites group
        all_sprites = pygame.sprite.Group()

        #initialize pygame
        pygame.init()
       
            
        image1 = pygame.image.load("monkey.png")
        image2 = pygame.image.load("monkey1.png")
        character_images = [image1, image2]
        current_image_index = 0
        current_image = character_images[current_image_index]

        #clock
        clock = pygame.time.Clock()
        
        #background
        background_image = pygame.image.load("sky1.png")
        background_y = 0
        keys = pygame.key.get_pressed()
        #game conditions 
        banana_font = pygame.font.Font("assets/font1.ttf", 30)
        banana_text = banana_font.render("Bananas Collected", True, green)
        banana_text_rect = banana_text.get_rect(center=(250, 300))
        while True:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.set_space_pressed(True)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        player.set_space_pressed(False)
                

               
                
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

            #--------
            #gravity_banana
            if banana.rect.y+banana_height>screen_height:
                print('banana_border')
                banana.rect.y=-100
                banana.rect.x=random.randint(50,500)
           
            #---------------
            # player movement A&D

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                player.rect.x -=3
                #print('player_move_-x')



            if keys[pygame.K_d]:
                player.rect.x +=3
               # print('player_move_x')   



            ## introduce jump mechanics
            if keys[pygame.K_SPACE]:
            # if player.rect.y+player_height==base1.rect.y:
                    # Scroll the background
                
                    #print('jump')
                    background_y += 5

                    if background_y >= screen_height:
                        background_y = 0
                    player.rect.y -=8
            
            
         

            if base.rect.y+base_height >screen_height:
                base.rect.y =0
                base.rect.x = random.randint(50,500)
            
            if base1.rect.y+base_height >screen_height:
                base1.rect.y=0
                base1.rect.x=random.randint(50,500)

            if base2.rect.y+base_height >screen_height:
                base2.rect.y = 0
                base2.rect.x = random.randint(50,500)

            #screen.blit(background_image, (0, background_y))
            #screen.blit(background_image, (0, background_y - screen_height))

            screen.fill((255,255,255))

            screen.blit(player.image,player.rect)
            screen.blit(base.image, base.rect)
            screen.blit(base1.image, base1.rect)
            screen.blit(base2.image, base2.rect)
            screen.blit(banana.image, banana.rect)
            player.update()
            base.update()
            base1.update()
            base2.update()
            banana.update()
            all_sprites.update()
            all_sprites.draw(screen)

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
    global banana_collected  
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

