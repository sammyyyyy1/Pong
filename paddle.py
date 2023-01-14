from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.pad = Turtle("square")
        self.pad.shapesize(stretch_wid=0.5, stretch_len=4)
        self.pad.color("white")
        self.pad.penup()
        self.pad.setheading(0)

    def reset(self, y_pos):
        self.pad.goto(x=-150, y=y_pos)

    def move_right(self):
        self.pad.forward(10)

    def move_left(self):
        self.pad.backward(10)

