from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_speed = 4
        self.y_speed = 4

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(x=new_x, y=new_y)

    def bounce_x(self):
        self.x_speed *= -1

    def bounce_y(self):
        self.y_speed *= -1
