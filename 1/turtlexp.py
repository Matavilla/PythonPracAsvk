from random import *
from turtle import *

shape("turtle")
while True:
    color(random(), random(), random())
    speed(random())
    pensize(random())
    circle(randrange(-30, 30), randrange(100))
