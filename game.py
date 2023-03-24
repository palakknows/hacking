import pygame
import random
from enum import Enum
from collections import namedtuple


# initialising the pygame 
pygame .init()

#directions of action 
class Directions(Enum):
    RIGHT = 1
    LEFT = 2
    UP =3
    DOWN =4

BOX_SIZE=20

start_point= namedtuple('start_point', 'x,y')  
    
class pythongame:
    def __init__(self, width=684 ,height=480):
        self.width = width
        self.height = height


#creating the display screen and initialising the 
# the height 480 and width 684 of screen 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('SNAKE UHOOO!')#adds caption on screen
        font = pygame.font.Font('font.ttf',32)
        self.clock = pygame.time.Clock()
        self.screen.fill((58,58,58))

        #initial state of game
        self.direction = Directions.RIGHT

        self.head = start_point(self.w/2, self.h/2)

        self.creeper = [self.head,start_point(self.head.x-BOX_SIZE, self.head.y),
        start_point(self.head.x-(2*BOX_SIZE), self.head.y)]

        self.score = 0
        self.reward =None
        self._place_reward()


    def _place_reward(self):
        #to exclude boundaries from either sides
        x= random.randint((0, (self.width-(2*BOX_SIZE)))//BOX_SIZE)*BOX_SIZE
        y= random.randint((0, (self.height-(2*BOX_SIZE)))//BOX_SIZE)*BOX_SIZE
        self.reward = start_point(x,y)
        #to avoid placiing food on snake
        if self.reward in self.creeper:
            self._place_reward()



    def play_game(self):
        #action from outside that is input is taken





     game_is_on = True
     return self.score



#the loop for game when it has to exit 
while game_is_on:
    for event in pygame.event.get(): #all events covered
        if event.type == pygame.QUIT: #for quit button use
            game_is_on  = False
        
#color remains for complete game so adding it here
        

        
    pygame.display.update()