import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Greedy Snake")

# set it to 0 means the screen won't update until calling screen.update()
# otherwise, each segment will update immediately, which make the screen flash
screen.tracer(0)

# create a snake object
snake = Snake()
food = Food()
score = Scoreboard()
score.inilization()

screen.listen()
screen.onkey(fun = snake.up, key = "Up")
screen.onkey(fun = snake.down, key = "Down")
screen.onkey(fun = snake.left, key = "Left")
screen.onkey(fun = snake.right, key = "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with its own tail
    # if head collide with any segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
