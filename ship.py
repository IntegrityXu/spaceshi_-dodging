import curses

class Ship:

    def __init__(self, deep, width, begin_x, begin_y):
        self.location = [begin_y + deep - 1, begin_x + width // 2]
        self.width = width
        self.begin_x = begin_x
        self.end_x = begin_x + width
        self.begin_y = begin_y

    def move(self, key): 
        #move the ship
        if key == curses.KEY_RIGHT:
            self.location[1] += 1
        elif key == curses.KEY_LEFT:
            self.location[1] -= 1

        #check if the ship out of boundary
        if self.location[1] >= self.end_x - 1:
            self.location[1] = self.end_x - 1
        if self.location[1] <= self.begin_x:
            self.location[1] = self.begin_x
            
    #check if the collision happens
    def safe(self, obstacle):
        if self.location[1] in obstacle:
            return False
        else:
            return True
    