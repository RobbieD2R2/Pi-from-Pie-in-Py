from graphics import *
from random import *
import random
import time
import math

def main():

    radius = 200
    inCircle = 1
    outCircle = 1

    win = GraphWin("Pi From Pie", 800,600)   #title, width, height
    win.setBackground("white")

    mylabel = Text(Point(400, 40), "Pi from Pie Simulation")    # anchorpoint (centered)
    mylabel.setSize(24)
    mylabel.setStyle("bold italic")
    mylabel.setTextColor("green")
    mylabel.draw(win)

    myrect = Rectangle(Point(200,100), Point(600,500))  # upper-left, bottom-right
    myrect.draw(win)

    mycircle = Circle(Point(400,300), 200)  # centerpoint, radius
    mycircle.draw(win)

    for i in range(3000):
        x = random.choice(range(200,600))
        y = random.choice(range(100,500))
        mydart = Point(x,y)

        # If x^2 + y^2 < r^2 Then its in the circle
        # Adjust for the center pixel location: -1 0 +1 grid
        # meaning, location 400,300 is the center of the grid: location 0,0

        if (400-x)**2 + (300-y)**2 < radius**2:
            mydart.setFill("red")
            mydart.draw(win)
            inCircle += 1
        else:
            mydart.setFill("blue")
            mydart.draw(win)
            outCircle += 1

        ratio = (4 * inCircle) / (inCircle + outCircle)
        print("Ratio equals ", ratio)
        time.sleep(.01)

    win.getMouse()
    win.close()

main()