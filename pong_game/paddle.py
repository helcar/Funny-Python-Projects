from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, init_xcor, init_ycor):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(init_xcor, init_ycor)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)


'''
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
paddle = Paddle()
screen.listen()
screen.onkey(fun = paddle.move_up, key = "Up")
screen.onkey(fun = paddle.move_down, key = "Down")
#paddle.move_up()
screen.exitonclick()
'''
