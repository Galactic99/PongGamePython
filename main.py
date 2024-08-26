from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.wall_bounce()

    if ball.distance(r_paddle) < 70 and ball.xcor() == 330:
        ball.paddle_bounce()

    if ball.distance(l_paddle) < 70 and ball.xcor() == -330:
        ball.paddle_bounce()

    if ball.xcor() > 390:
        ball.out_of_bounds()
        scoreboard.l_point()
        time.sleep(1)

    if ball.xcor() < -390:
        ball.out_of_bounds()
        scoreboard.r_point()
        time.sleep(1)



screen.exitonclick()
