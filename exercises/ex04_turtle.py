"""Going to attempt to draw a house with windows. My "Try something fun!" is assigning random colors to the flags by using the randint function on line 94."""

__author__ = "730510654"

from turtle import Turtle, colormode, done
from random import randint

colormode(255)


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw a rectangle of the given width and length whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i = 0
    while i < 2:
        a_turtle.forward(length)
        a_turtle.right(90)
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1


def draw_triangle(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a triangle of the given width whose left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(270)
    a_turtle.pendown()
    i = 0
    while i < 3:
        a_turtle.forward(width)
        a_turtle.left(120)
        i += 1


def draw_line(a_turtle: Turtle, x: float, y: float, length: float, direction: float) -> None:
    """Draw a line of the given length towards the given direction, starting at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(direction)
    a_turtle.pendown()
    a_turtle.forward(length)


def main() -> None:
    """The entrypoint of my scene."""
    window_width = 100
    door_length = 100
    door_width = 200
    house_length = 600
    house_width = 300
    flag_width = 50
    line_length = 100 
    cool_guy: Turtle = Turtle()
    cool_guy.speed(50)
    cool_guy.hideturtle()

    cool_guy.fillcolor(32, 137, 8)
    cool_guy.begin_fill()
    draw_rectangle(cool_guy, -500, -300, 200, 1000)
    cool_guy.end_fill()

    cool_guy.fillcolor(43, 189, 201)
    cool_guy.begin_fill()
    draw_rectangle(cool_guy, -500, 500, 800, 1000)
    cool_guy.end_fill()

    cool_guy.fillcolor(190, 15, 15)
    cool_guy.begin_fill()
    draw_rectangle(cool_guy, -300, 0, house_width, house_length)
    cool_guy.end_fill()

    i = 0
    x = -300
    while i < 6:
        draw_line(cool_guy, x, 0, line_length, 90)
        cool_guy.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
        cool_guy.begin_fill()
        draw_triangle(cool_guy, x, 100, flag_width)
        cool_guy.end_fill()
        i += 1
        x += 120

    cool_guy.fillcolor(136, 98, 5)
    cool_guy.begin_fill()
    draw_rectangle(cool_guy, -50, -100, door_width, door_length)
    cool_guy.end_fill()

    i = 0
    x = -200
    while i < 2:
        cool_guy.fillcolor(255, 255, 255)
        cool_guy.begin_fill()
        draw_square(cool_guy, x, -100, window_width)
        cool_guy.end_fill()
        i += 1
        x += 300
    
    i = 0
    x = -200
    while i < 4:
        cool_guy.pencolor(131, 43, 201)
        if i < 2:
            draw_line(cool_guy, x, -150, line_length, 0)
        elif i == 2:
            x = -150
            draw_line(cool_guy, x, -100, line_length, 270)
        else:
            x = 150
            draw_line(cool_guy, x, -100, line_length, 270)
        x += 300
        i += 1

    done()


if __name__ == "__main__":
    main()
