import pygame
import sys
import time

import main

def run_progress_bar(banana_collected,revive_screen):
    pygame.init()

    # Set up the display
    screen_width, screen_height = 800, 200
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Progress Bar")

    # Colors
    bright_green = (0, 255, 0)
    dark_green = (0, 128, 0)

    # Bar dimensions
    bar_width, bar_height = 300, 20
    bar_x, bar_y = 200, screen_height // 2 - bar_height // 2

    # Bar state
    bar_fill = 0
    bar_speed = 2

    # Color change parameters
    color_interval = 1
    color_timer = 0
    current_color = bright_green

    # Flag for resetting
    resetting = False

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resetting = True

        keys=pygame.key.get_pressed()

        if banana_collected ==True:
            print('space')
            bar_fill=0

        # Update the bar fill
        if bar_fill < bar_width:
            bar_fill += bar_speed
        
        if bar_fill>bar_width:
            revive_screen()

        # Update the color change
        

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the empty bar
        pygame.draw.rect(screen, dark_green, (bar_x, bar_y, bar_width, bar_height))

        # Calculate the width of the filled portion of the bar from right to left
        filled_width = bar_x + bar_width - bar_fill

        # Draw the filled portion of the bar with current color
        pygame.draw.rect(screen, current_color, (filled_width, bar_y, bar_fill, bar_height))

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

