from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def ball_move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.x_move *= -1




'''
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
ball = Ball()
ball.ball_move()
#paddle.move_up()
screen.exitonclick()
'''