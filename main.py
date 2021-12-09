from turtle import Turtle, Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

WIDTH = 800
HEIGHT = 600
REFRESH_RATE = 1/100


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("Green")
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle(-380)
paddle_r = Paddle(370)
ball = Ball()
score_board = ScoreBoard()


screen.listen()
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")

game_on = True

while game_on:

    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= - 280:
        ball.bounce_y()
    if ball.xcor() < -360 and ball.distance(paddle_l) < 50:
        ball.bounce_x()
    elif ball.xcor() > 350 and ball.distance(paddle_r) < 50:
        ball.bounce_x()
    if ball.xcor() > 400:
        score_board.l_point()
        score_board.update_scoreboard()
        ball.reset_position()
    if ball.xcor() < -400:
        score_board.r_point()
        score_board.update_scoreboard()
        ball.reset_position()

    screen.update()
    sleep(REFRESH_RATE)


screen.exitonclick()
