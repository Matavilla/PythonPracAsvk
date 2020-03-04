from random import *
from turtle import *

shape("turtle")
pensize(3)
speed(9)
while True:
    coord = pos()
    if True or abs(coord[0]) >= window_width() / 2 or abs(coord[1]) >= window_height() / 2:
#undo()
        penup()
        turtlesize(randrange(1, 40))
        color(random(), random(), random())
        goto(randrange(-window_width(), window_width()), randrange(-window_height(), window_height()))
        pendown()
        continue
    circle(randrange(-60,60), randrange(10, 200))

