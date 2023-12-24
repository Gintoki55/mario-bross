#set up the screen

import turtle

wn = turtle.Screen()
wn.setup(width=800,height=600)
wn.bgcolor("red")

head = turtle.Turtle()
head.penup()
head.color("blue")
head.shape("square")
head.goto(0,-250)
head.pendown()
head.goto(100,200)

while True:
    wn.update()