from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)

    def inilization(self):
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", move = False, align = "center", font = ("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align="center", font=("Arial", 18, "bold"))


#screen = Screen()
#screen.bgcolor("black")
#text = Scoreboard()
#text.inilization()
#screen.exitonclick()