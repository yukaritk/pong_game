from turtle import Turtle
FONT = ("Courier", 80, "normal")
ALIGN = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.board()

    def board(self):
        self.clear()
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALIGN, font=FONT)
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=ALIGN, font=FONT)

    def l_point(self):
        self.r_score += 1
        self.board()

    def r_point(self):
        self.l_score += 1
        self.board()