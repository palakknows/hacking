import pygame
import random
from enum import Enum
from collections import namedtuple


# initialising the pygame 
pygame .init()

font = pygame.font.Font('font.ttf',30)
#directions of action 
class Directions(Enum):
    RIGHT = 1
    LEFT = 2
    UP =3
    DOWN =4

BOX_SIZE=20
SPEED = 10 #decides how fast our game is
start_point= namedtuple('start_point', 'x,y')  
    
class pythongame:
    def __init__(self, width=684 ,height=480):
        self.width = width
        self.height = height


#creating the display screen and initialising the 
# the height 480 and width 684 of screen 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('SNAKE UHOOO!')#adds caption on screen
       
        self.clock = pygame.time.Clock()
        

        #initial state of game
        self.direction = Directions.RIGHT

        self.head = start_point(self.width/2, self.height/2)
        self.creeper = [self.head,start_point(self.head.x-BOX_SIZE, self.head.y),
        start_point(self.head.x-(2*BOX_SIZE), self.head.y)]

        self.score = 0
        self.reward =None
        self._place_reward()


    def _place_reward(self):
        #to exclude boundaries from either sides
        x= random.randint(0, (self.width-2*BOX_SIZE)//BOX_SIZE)*BOX_SIZE #//division operator
        y= random.randint(0, (self.height-2*BOX_SIZE)//BOX_SIZE)*BOX_SIZE
        self.reward = start_point(x,y)
        #to avoid placiing food on snake
        if self.reward in self.creeper:
            self._place_reward()




    def play_game(self):
        #action from outside that is input is taken
        for event in pygame.event.get(): 
          if event.type == pygame.QUIT:
            pygame.quit()#ensures game is not running
            quit()                              
            
          if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                self.direction =Directions.LEFT
            elif event.key == pygame.K_RIGHT:
                self.direction =Directions.RIGHT
            elif event.key == pygame.K_UP:
                self.direction =Directions.UP
            elif event.key == pygame.K_DOWN:
                self.direction =Directions.DOWN
        #move 
        self._move(self.direction)#move is defined
        self.creeper.insert(0,self.head)#adding head 

    

        #exit 
        game_on=True
        if self._collision():
            game_on=False
            return game_on,self.score
        

        #location upgrade for food

        if self.head==self.reward:
            self.score+=1
            self._place_reward()
        else:
            self.creeper.pop()#remove food from end

        #update of display
        self._update_display()
        self.clock.tick(SPEED)

        #score is seen and status of game
        return game_on,self.score
    
    
    def _collision(self):
        if self.head.x>self.width-BOX_SIZE or self.head.y>self.height-BOX_SIZE or self.head.x<0 or self.head.y<0 :
         return False
        
        if self.head in self.creeper[1:]:
         return False
        
        return True

    
    def _update_display(self):
        self.screen.fill((58,58,58)) #color of screen grey
        
        for start_point in self.creeper:
            pygame.draw.rect(self.screen,(0,255,0),pygame.Rect(start_point.x,start_point.y,BOX_SIZE,BOX_SIZE))#ensures snake on screen of green color and rectangles
            pygame.draw.rect(self.screen,(255,0,0),pygame.Rect(start_point.x+6,start_point.y+6,10,10))#a small rect in front of red color

            pygame.draw.rect(self.screen,(0,0,255),pygame.Rect(self.reward.x,self.reward.y,10,10))
        #concatenation of string 
            text=font.render("Score:"+str(self.score), True,(0,0,0))
            self.screen.blit(text, [0,0])#to display at corner
            pygame.display.flip()#section of screen is refreshed
    def _move(self,direction):
        x=self.head.x
        y=self.head.y
        if direction == Directions.RIGHT:
            x+=BOX_SIZE #moving one box ahead
        elif direction == Directions.LEFT:
            x-=BOX_SIZE
        elif direction == Directions.UP:
            y+=BOX_SIZE
        elif direction == Directions.DOWN:
            y-=BOX_SIZE

        self.head = start_point(x,y)

#defining main function 
if __name__ == "__main__":
    pyg=pythongame()
    
#the loop for game when it has to exit 
while True:

    game_on,score = pyg.play_game()

    if game_on ==False:
        break
    
    print('Final score',score) #mentioned as in initialising func
    
#color remains for complete game so adding it here
        
    pygame.quit()
        
    