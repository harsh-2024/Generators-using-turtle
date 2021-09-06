import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
my_screen = Screen()
turtle.colormode(255)


def color_picker():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_color = (r,g,b)
    return my_color


def draw(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.speed("fastest")
        timmy.pensize(2)
        timmy.color(color_picker())
        timmy.circle(120)
        timmy.setheading(timmy.heading()+size_of_gap)




draw(5)

my_screen.exitonclick()
