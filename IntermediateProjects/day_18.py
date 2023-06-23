from turtle import Turtle, Screen
from random import choice, randint

import turtle as t

t.colormode(255)
# t.mode("logo")

tim = t.Turtle()


# The Square Project

# def square():
#     for _ in range(4):
#         tim.forward(100)
#         tim.right(90)


# Drawing Dashes Challenge

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Drawing different shapes all at once
colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "burlywood",
    "medium spring green",
    "wheat",
    "chocolate",
    "slate blue",
    "IndianRed",
    "dark slate gray",
    "LightSeaGreen",
]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.right(angle)
#         tim.forward(100)


# for shape_size in range(3, 11):
#     tim.color(choice(colors))
#     draw_shape(shape_size)


# Random Walk Challenge


def random_colors():
    r = randint(0, 255)

    g = randint(0, 255)

    b = randint(0, 255)
    # tuple creation
    color = (r, b, g)

    return color


# def random_walk(angle_list):
#     rand_angle = choice(angle_list)

#     tim.forward(30)

#     tim.setheading(rand_angle)


# tim.pensize(10)

# tim.speed("fastest")

# start_walk = True

# angles = [0, 90, 180, 270]

# for _ in range(200):
#     color = random_colors()
#     print(color)

#     tim.color(color)

#     random_walk(angle_list=angles)


# Spirograph
tim.speed("fastest")


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


# draw_spirograph(5)
draw_spirograph(50)

screen = Screen()

screen.exitonclick()
