import pygame
import os
import random
import numpy as np
import pygame.freetype
from enum import Enum
from sys import exit
from pygame.locals import *
from collections import namedtuple


# initialising the pygame 
pygame.init()
pygame.font.init()

font = pygame.freetype.SysFont('font.ttf',30)
#directions of action 
class Directions(Enum):
    RIGHT = 1
    LEFT = 2
    UP =3
    DOWN =4

    BLACK=(0,0,0)

BOX_SIZE=20
SPEED = 20 #decides how fast our game is
start_point= namedtuple('start_point', 'x,y')  
    
class pythongameAI:
    def __init__(self, width=684 ,height=480):
        self.width = width
        self.height = height


#creating the display screen and initialising the 
# the height 480 and width 684 of screen 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('SNAKE UHOOO!')#adds caption on screen
       
        self.clock = pygame.time.Clock()
        
        self.refresh()
       


    def refresh(self):
         #initial state of game
        self.direction = Directions.RIGHT

        self.head = start_point(self.width/2, self.height/2)
        self.creeper = [self.head,start_point(self.head.x-BOX_SIZE, self.head.y),
        start_point(self.head.x-(2*BOX_SIZE), self.head.y)]

        self.score = 0
        self.reward =None
        self._place_reward()
        self.frame_iteration=0


    def _place_reward(self):
        #to exclude boundaries from either sides
        x= random.randint(0, (self.width-2*BOX_SIZE)//BOX_SIZE)*BOX_SIZE #//division operator
        y= random.randint(0, (self.height-2*BOX_SIZE)//BOX_SIZE)*BOX_SIZE
        self.reward = start_point(x,y)
        #to avoid placiing food on snake
        if self.reward in self.creeper:
            self._place_reward()




    def play_game(self, action):
        self.frame_iteration+=1
        #action from outside that is input is taken
    
        for event in pygame.event.get(): 
          if event.type == pygame.QUIT:
            pygame.quit()#ensures game is not running
            quit()                              
            
    
        #movement guide
        self._move(action)#move is defined
        self.creeper.insert(0,self.head)#adding head 

    

        #exit 
        prize =0
        game_over=False
        if self._collision() or self.frame_iteration> 120*len(self.creeper):
            game_over=True
            prize=-10

            return prize,game_over,self.score
        

        #location upgrade for food

        if self.head==self.reward:
            self.score +=1
            prize= 10
            self._place_reward()
        else:
            self.creeper.pop()#remove food from end

        #update of display
        self._update_display()
        self.clock.tick(SPEED)

        #score is seen and status of game
        return prize,game_over,self.score
    
    
    def _collision(self,pt=None):
        if pt is None:
            pt = self.head
        if pt.x>self.width - BOX_SIZE or pt.y>self.height-BOX_SIZE or pt.x<0 or pt.y<0 :
         return True
        
        if pt in self.creeper[1:]:
         return True
        
        return False

    
    def _update_display(self):
        self.screen.fill((58,58,58)) #color of screen grey
        
        for pt in self.creeper:
            pygame.draw.rect(self.screen,(0,255,0),pygame.Rect(pt.x,pt.y,BOX_SIZE,BOX_SIZE))#ensures snake on screen of green color and rectangles
            pygame.draw.rect(self.screen,(255,0,0),pygame.Rect(pt.x+6,pt.y+6,10,10))#a small rect in front of red color

            pygame.draw.rect(self.screen,(0,0,255),pygame.Rect(self.reward.x,self.reward.y,10,10))
        #concatenation of string 
            text=font.render('Score:' + str(self.score), True,(0,0,0))
            self.screen.blit(text,[0,0])
            pygame.display.flip()#section of screen is refreshed
    def _move(self,action):
         
        motion=[Directions.RIGHT, Directions.DOWN,Directions.LEFT,Directions.UP]
        idx= motion.index(self.direction)
        
        if np.array_equal(action,[1,0,0]):
            new_dir = motion[idx]
        elif np.array_equal(action,[0,1,0]):
            next_idx =(idx+1)%4
            new_dir = motion[next_idx]
        else:
            next_idx =(idx-1)%4
            next_dir=motion[next_idx]
        
        self.direction =new_dir

        x=self.head.x
        y=self.head.y
        if self.direction == Directions.RIGHT:
            x+=BOX_SIZE #moving one box ahead
        elif self.direction == Directions.LEFT:
            x-=BOX_SIZE
        elif self.direction == Directions.UP:
            y+=BOX_SIZE
        elif self.direction == Directions.DOWN:
            y-=BOX_SIZE

        self.head = start_point(x,y)

#defining main function 
