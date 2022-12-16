from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.up()
        self.shape("square")
        self.shapesize(6, 1)
        self.color("white")
        self.goto((x_pos, y_pos))

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)