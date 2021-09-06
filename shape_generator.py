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

def draw_shape(sides):
    angle = 360/sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)


for sides in range(3, 11):
    timmy.color(color_picker())
    timmy.pensize(5)
    draw_shape(sides)











