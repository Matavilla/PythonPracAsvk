from random import *
from turtle import *


def P():
    color(random(), random(), random())
    left(90)
    forward(120)
    right(90)
    forward(60)
    right(90)
    forward(120)
    left(90)

def O():
    color(random(), random(), random())
    circle(40, 360)

def L():
    color(random(), random(), random())
    left(60)
    forward(87)
    right(120)
    forward(87)
    left(60)

def I():
    left(90)
    forward(80)
    right(180)
    penup()
    forward(80)
    pendown()
    left(150)
    forward(92)
    right(150)
    forward(80)
    left(90)

def N():
    color(random(), random(), random())
    left(90)
    forward(80)
    right(180)
    forward(40)
    left(90)
    forward(60)
    left(90)
    forward(40)
    right(180)
    forward(80)
    left(90)

def A(): 
    color(random(), random(), random())
    left(60)
    forward(87)
    right(120)
    forward(87)
    left(180)
    forward(40)
    left(60)
    forward(44) 
    left(60)
    penup()
    forward(40)
    left(30)
    forward(9)
    left(90)
    pendown()
    color("RED")
    forward(80)

x = abs(pos()[0]) + 240
y = 200
speed(0)    
right(180)
penup()
forward(150)
pendown()
left(180)
shape("turtle")
pensize(5)
color("RED")
forward(20)
forward(50)


penup()
left(180)
forward(60)
right(90)
forward(9)
pendown()
right(90)

P()

penup()
right(90)
forward(9)
left(90)
pendown()

color("RED")
forward(70)

penup()
left(90)
forward(9)
pendown()
right(90)

O()

color("RED")
penup()
right(90)
forward(9)
pendown()
left(90)
forward(50)

forward(87)
right(180)
forward(87)
left(180)
penup()
left(90)
forward(9)
pendown()
right(90)

L()


penup()
right(90)
forward(9)
left(90)
pendown()

color("RED")
forward(20)

forward(60)
right(180)
forward(60)
left(180)
penup()
left(90)
forward(9)
pendown()
right(90)

I()

penup()
right(90)
forward(9)
left(90)
pendown()
color("RED")
forward(20)

forward(60)
right(180)
forward(60)
left(180)
penup()
left(90)
forward(9)
pendown()
right(90)

N()
penup()
right(90)
forward(9)
left(90)
pendown()
color("RED")
forward(20)

penup()
left(90)
forward(9)
pendown()
right(90)

A()

color("RED")
forward(20)

circle(200, 180)
forward(550)
circle(200, 180)
forward(60)
while True:
    coord = pos()
    if abs(coord[0]) >= window_width() / 2 or abs(coord[1]) >= window_height() / 2 or not -x < coord[0] < x or not -y < coord[1] < y:
         undo()
         continue
    color(random(), random(), random())
    circle(randrange(-60, 60), randrange(10, 200))
exitonclick()
