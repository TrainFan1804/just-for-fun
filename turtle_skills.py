import turtle
from random import randint


def quadrat(länge):
    for i in range(4):
        turtle.forward(länge)
        turtle.right(90)


def dreieck(länge):
    for i in range(3):
        turtle.forward(länge)
        turtle.right(120)


def vieleck(ecken, längen):
    winkel = 360 / ecken
    for i in range(ecken):
        turtle.forward(längen)
        turtle.right(winkel)

turtle.speed(100000)
turtle.hideturtle()
turtle.pensize(3)

for i in range(100):
    turtle.heading()
    turtle.goto(randint(-100, 200), randint(200, 500))
    länge = randint(10, 100)
    ecken = randint(3, 7)
    vieleck(länge, ecken)