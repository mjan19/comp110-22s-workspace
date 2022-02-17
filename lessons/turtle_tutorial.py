from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

side_length = 300

colormode(255)

leo.color(99, 204, 250)
leo.fillcolor(32, 67, 93)
leo.hideturtle()
leo.speed(50)

leo.up()
leo.goto(-200, -100)
leo.down()

leo.begin_fill()

i = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i += 1

leo.end_fill()

bob: Turtle = Turtle()

bob.color(0, 0, 0)
bob.speed(100)

bob.up()
bob.goto(-200, -100)
bob.down()

while (i < 90):
    bob.forward(side_length)
    bob.left(122)
    side_length *= .97
    i += 1

done()
