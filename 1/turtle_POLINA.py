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
    forward(100)
    left(90)
    pendown()
    color("RED")
    forward(80)

speed(4)    
right(180)
penup()
forward(300)
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
forward(100)
pendown()
right(90)

P()

penup()
right(90)
forward(100)
left(90)
pendown()

color("RED")
forward(70)

penup()
left(90)
forward(100)
pendown()
right(90)

O()

color("RED")
penup()
right(90)
forward(100)
pendown()
left(90)
forward(50)

forward(87)
right(180)
forward(87)
left(180)
penup()
left(90)
forward(100)
pendown()
right(90)

L()


penup()
right(90)
forward(100)
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
forward(100)
pendown()
right(90)

I()

penup()
right(90)
forward(100)
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
forward(100)
pendown()
right(90)

N()
penup()
right(90)
forward(100)
left(90)
pendown()
color("RED")
forward(20)

penup()
left(90)
forward(100)
pendown()
right(90)

A()

color("RED")
forward(20)

circle(200, 180)
forward(550)
circle(200, 180)
forward(60)
penup()
goto(170, 260)
pendown()
color('red', 'yellow')
begin_fill()
for i in range(0, 300):
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
penup()
while True:
    turtlesize(randrange(1, 40))
    color(random(), random(), random())
    goto(randrange(-window_width(), window_width()), randrange(-window_height(), window_height()))
exitonclick()
