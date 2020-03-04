from random import *
from turtle import *

shape("turtle")
pensize(5)
while True:
    color(random(), random(), random())
    speed(random())
    pensize(random())
    circle(randrange(-1000, 1000), randrange(100))
