# Midterm Project
# Completed by Theresa Chen on October 28, 2022
import turtle

t = turtle.Turtle()


def draw_square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)


draw_square(100)
turtle.done()
