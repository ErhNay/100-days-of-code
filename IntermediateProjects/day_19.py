from turtle import Turtle, Screen
import random

# # tim = Turtle()
# etch_a_sketch = Turtle()

is_race_on = False

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make a bet", prompt="Which turtle will win the race? Enter a color: "
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_offset = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")

    new_turtle.color(colors[turtle_index])

    new_turtle.penup()

    new_turtle.goto(x=-230, y=y_offset[turtle_index])

    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False

            # get the winning color
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")

            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)

        turtle.forward(random_distance)


screen.exitonclick()


# # def move():
# #     for _ in range(6):
# #         tim.fd(100)
# #         tim.lt(60)


# # screen.onkey(fun=move, key="space")


# # Etch A Sketch Challenge


# # move forward
# def move_forward():
#     etch_a_sketch.fd(10)


# def move_backward():
#     etch_a_sketch.back(10)


# def counter_clockwise():
#     etch_a_sketch.left(10)


# def clockwise():
#     etch_a_sketch.right(10)


# def clear_screen():
#     etch_a_sketch.reset()


# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear_screen)
# screen.exitonclick()


#
