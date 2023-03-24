import pygame
import random

# initialising the pygame 
pygame .init()

#creating the display screen and initialising the 
# the height and width of screen 
screen =pygame.display.set_mode ((684,480))
pygame.display.set_caption('SNAKE UHOOO!')#adds caption on screen
font = pygame.font.Font('font.ttf',32)



game_is_on = True



#the loop for game when it has to exit 
while game_is_on:
    for event in pygame.event.get(): #all events covered
        if event.type == pygame.QUIT: #for quit button use
            game_is_on  = False
        
