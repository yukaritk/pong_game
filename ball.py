from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.shape("circle")
        self.color("white")
        self.x_move = 3
        self.y_move = 3
        self.move()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def limit(self):
        self.y_move *= -1

    def defend(self):
        self.x_move *= -1
        self.speed_up()

    def restart(self):
        self.goto(0, 0)
        self.defend()

    def speed_up(self):
        self.y_move *= 1.1
        self.x_move *= 1.1