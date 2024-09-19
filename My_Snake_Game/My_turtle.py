from turtle import  Screen
from my_snk import Snake
from my_fdk import Food
from my_scoreboard import ScoreBoard

import time


screen = Screen()
screen.setup(width=500 , height=500)
screen.bgcolor("black")
screen.title("My_snake_Game")
screen.tracer()

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        
        score.increase_score()


screen.exitonclick()        