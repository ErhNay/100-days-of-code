###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random

t.colormode(255)


hirst = t.Turtle()


# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print("\n")
# print(rgb_colors)

color_list = [
    (202, 164, 110),
    (236, 239, 243),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]

gap = 0
X_AXIS = -250
Y_AXIS = -200


def random_color(colors):
    color = random.choice(colors)
    return hirst.color(color)


def turtle_start_position(x_axis, y_axis):
    hirst.speed("fastest")
    hirst.hideturtle()
    hirst.penup()
    hirst.goto(x_axis, y_axis)


def dot_on_x_axis(dot_size, space, colors):
    num_of_dots = 10
    for _ in range(1, num_of_dots + 1):
        hirst.dot(dot_size, random.choice(colors))
        hirst.penup()
        hirst.forward(space)


def dot_on_y_axis(x_val, y_val, gap):
    hirst.penup()
    hirst.goto(x_val, (y_val + gap))
    hirst.pendown()


turtle_start_position(X_AXIS, Y_AXIS)
turns = 0
while turns <= 10:
    dot_on_x_axis(20, 50, color_list)
    dot_on_y_axis(X_AXIS, Y_AXIS, gap)
    gap += 50
    turns += 1


screen = t.Screen()
screen.exitonclick()
