from turtle import Turtle

class Wall(Turtle):

    def __init__(self, wall_type):
        super().__init__()
        self.wall = Turtle("square")
        self.wall.color("white")
        self.wall.penup()
        if wall_type == "vertical":
            self.wall.shapesize(stretch_wid=26.5, stretch_len=0.5)
        elif wall_type == "horizontal":
            self.wall.shapesize(stretch_wid=0.5, stretch_len=20)


