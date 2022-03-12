from turtle import Turtle, Screen 
import time 

from food import Food
from culebrita import Snake
from scoreboard import ScoreBoard

screen = Screen() 
screen.setup(width=600, height=600) 
screen.bgcolor("black") 
screen.title("Programate snake game") 
screen.tracer(1)

game_is_on = True 

first_snake = Snake()
comida = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(first_snake.up, "Up")
screen.onkey(first_snake.down, "Down")
screen.onkey(first_snake.left, "Left")
screen.onkey(first_snake.right, "Right")

while game_is_on: 
    screen.update()
    time.sleep(0.1)
    first_snake.move()
    
    if first_snake.head.distance(comida)< 15:
        comida.refresh()
        scoreboard.increase_score()
        first_snake.add()

    if first_snake.head.xcor() > 280 or first_snake.head.xcor() < -280 or first_snake.head.ycor() > 280 or first_snake.head.ycor() < -280:
        print("OVER")
        game_is_on = False
        scoreboard.game_over()
screen.exitonclick()
