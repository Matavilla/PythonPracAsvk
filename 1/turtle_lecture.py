from random import *
from turtle import *

shape("turtle")
pensize(4)
i = 1
while True:
    coord = pos()
    if abs(coord[0]) >= window_width() / 2 or abs(coord[1]) >= window_height() / 2:
        undo()
        continue
    color(random(), random(), random())
    pensize(i)
    turtlesize(i)
    i += 5
    circle(randrange(-60,60), randrange(10, 200))

