import curses
import argparse
from obstacle import Obstacle
from ship import Ship

def main(stdscr, args):

    curses.curs_set(0)
    stdscr.nodelay(1)

    mh, mw = stdscr.getmaxyx()
    begin_x = 0 
    begin_y = 0

    if args.canvas_height > mh - begin_y or args.canvas_width > mw - begin_x:
        raise RuntimeError("The game can't initialize, please adjust your screen size or change canvas size.")


    sh = args.canvas_height
    #leave space for score
    sw = args.canvas_width - 10
   
    difference = [70000,50000,20000]
    #the speed of generating obsttacles, according to different level
    speed = difference[args.diff_level - 1]

    obstacle = Obstacle(sw, sh)
    ship = Ship(sh, sw, begin_x, begin_y)

    stdscr.addstr(ship.location[0], ship.location[1], "*")
    moveList = [curses.KEY_LEFT, curses.KEY_RIGHT]

    cob = 0
    score = 0

    while 1: 
        cob += 1
        if cob == speed:
            score += 1
            cob = 0
            #add new obstacles
            stdscr.clear()
            obstacle.createObstacle()
            for row in range(len(obstacle.obstacles)):
                for col in obstacle.obstacles[row]:
                    stdscr.addstr(row, col, "-")


        #move the ship
        key = stdscr.getch()
        if key in moveList:
            stdscr.addstr(ship.location[0], ship.location[1], " ")
            ship.move(key)
        elif key == 27:
            return 

        #check if collision happens
        #beacuse the ship and obstacle could meet at the bottom, so just check if collision when the obstacle arrived the bottom
        if len(obstacle.obstacles) == sh:
            if not ship.safe( obstacle.obstacles[len(obstacle.obstacles) - 1]) :
                #draw the result
                stdscr.addstr(ship.location[0], ship.location[1], "x")
                stdscr.addstr(sh - 1, sw + 3, "score: " + str(score - sh))
                stdscr.addstr( sh // 2, sw // 2 - 13, "press any key to continue")
                stdscr.refresh()
                stdscr.nodelay(0)
                stdscr.getch()
                break    

        stdscr.addstr(ship.location[0], ship.location[1], "*")
        stdscr.refresh()
        
    
#argument setting
parse = argparse.ArgumentParser()

parse.add_argument("--canvas_height", type = int, default = 20, 
                    help="the height of game area")
parse.add_argument("--canvas_width", type = int, default = 50, 
                    help="the width of game arrea")
parse.add_argument("--diff_level", type = int, default = 1, choices=[1, 2, 3],
                    help="")

args = parse.parse_args()

try:
    curses.wrapper(lambda x: main(x, args))
except RuntimeError as e:
    print(e)