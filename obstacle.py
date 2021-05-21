import random
from collections import deque
import random

class Obstacle:

    def __init__(self, width, height, div):
        self.width = width
        self.height = height
        self.obstacles = deque()
        self.div = div
    
    #add a new obstacle line
    def createObstacle(self): 

        #if the obstacles fill the screen, remove one line
        if len(self.obstacles) == self.height: 
            self.obstacles.pop()
        
        #number of obstacles in one line
        lineNum = random.randrange(3, self.width // self.div)
        #the location of obstacles
        index = random.sample(range(0, self.width ) , lineNum)
        self.obstacles.appendleft(index)
                
