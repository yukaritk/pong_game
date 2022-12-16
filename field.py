from turtle import Turtle


class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(100, 0.2)
        self.color("white")