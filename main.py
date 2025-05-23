from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

######################Screen Behavior##############################
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

####################Initialize Snake and Food Behavior################################
snake = Snake()
food = Food()
score = Scoreboard()

####################Snake Behavior################################
screen.onkey(snake.up, "Up")
screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

####################Game Logic################################
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    ########################### Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    ############ Detectin collision 
    if snake.head.xcor() > 280 or snake.head.xcor()< -280  or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False 
        scoreboard.game_over()

        for segment in snake.segments[1:]:
        elif snake.head.distance(segment) < 10:
            game_is_on = False 
            scoreboard.game_over()

###################How To CLose The Game#################################
screen.exitonclick()
