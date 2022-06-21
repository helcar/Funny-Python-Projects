from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun = paddle_right.move_up, key = "Up")
screen.onkey(fun = paddle_right.move_down, key = "Down")
screen.onkey(fun = paddle_left.move_up, key = "w")
screen.onkey(fun = paddle_left.move_down, key = "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with paddles
    if ball.xcor() > 320:
        if ball.distance(paddle_right) < 60:
            ball.bounce_paddle()
        else:
            ball.reset_position()  # right paddle missed the ball
            scoreboard.update_left_score()

    if ball.xcor() < -320:
        if ball.distance(paddle_left) < 60:
            ball.bounce_paddle()
        else:
            ball.reset_position()  # left paddle missed the ball
            scoreboard.update_right_score()




screen.exitonclick()
