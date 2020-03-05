from random import *
from turtle import *
from math import *

shape("turtle")
pensize(3)
speed(9999)
i = 0
while True:
    coord = pos()
    if abs(coord[0]) >= window_width() / 2 or abs(coord[1]) >= window_height() / 2:
#undo()
        turtlesize(i + randrange(1, 40),i + randrange(1, 40),i + randrange(1, 40))
        color(random(), random(), random())
        d = atan(coord[1] / coord[0]) * 180 / pi
        right(180 * (1 + (coord[0] < 0)) - d + heading())
        circle(randrange(10, 60), 90)
        circle(-randrange(10, 60), 90)
        circle(-randrange(10, 60), 90)
        circle(randrange(10, 60), 90)
#goto(randrange(-window_width(), window_width()), randrange(-window_height(), window_height()))
        continue
    color(random(), random(), random())
    circle(randrange(-60,60), randrange(10, 200))

