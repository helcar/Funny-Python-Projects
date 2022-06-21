import random
from turtle import Turtle, Screen

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        #original is 20 x 20, times 0.5 becomes 10 x 10
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280),random.randint(-280,280))


#screen = Screen()
#food = Food()
#screen.exitonclick()
