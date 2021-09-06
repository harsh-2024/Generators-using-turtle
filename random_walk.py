import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
my_screen = Screen()
turtle.colormode(255)

def color_pricker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r,g,b)
    return my_color

direction = [0, 90, 180, 270]

for _ in range(150):
    timmy.forward(20)
    timmy.setheading(random.choice(direction))
    timmy.color(color_pricker())
    timmy.pensize(5)
    timmy.speed("fastest")

