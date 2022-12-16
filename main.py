import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from field import Field

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()
score = Scoreboard()
field = Field()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.limit()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 280 or (ball.distance(l_paddle) < 50 and ball.xcor() < - 280):
        ball.defend()

    if ball.xcor() > 350:
        ball.restart()
        score.r_point()

    if ball.xcor() < -350:
        ball.restart()
        score.l_point()

screen.exitonclick()
