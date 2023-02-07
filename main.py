from turtle import Screen
import time
from python import Python
from food import Food
from scooreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Python()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        score.total_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        score.game_over()
        game_on = False

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_on = False


screen.exitonclick()